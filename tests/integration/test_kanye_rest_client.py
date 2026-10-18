import json
import socket
import threading
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from kanye_quotes.constants import USER_AGENT
from kanye_quotes.domain.errors import QuoteUnavailableError
from kanye_quotes.infrastructure.kanye_rest_client import KanyeRestClient

TIMEOUT_SECONDS = 2


class _Handler(BaseHTTPRequestHandler):
    status = 200
    body = b""
    received_headers: dict[str, str] = {}

    def do_GET(self) -> None:  # noqa: N802 (name fixed by http.server)
        type(self).received_headers = dict(self.headers.items())
        self.send_response(self.status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(self.body)))
        self.end_headers()
        self.wfile.write(self.body)

    def log_message(self, format: str, *args: object) -> None:
        """Keep the test output quiet."""


class _Api:
    """A local stand-in for the Kanye Rest API."""

    def __init__(self, handler: type[_Handler], port: int) -> None:
        self._handler = handler
        self._url = f"http://127.0.0.1:{port}/"

    @property
    def received_headers(self) -> dict[str, str]:
        return self._handler.received_headers

    def client_answering(self, body: bytes, status: int = 200) -> KanyeRestClient:
        self._handler.status = status
        self._handler.body = body
        return KanyeRestClient(self._url, TIMEOUT_SECONDS)


@pytest.fixture
def api() -> Iterator[_Api]:
    handler = type("Handler", (_Handler,), {})
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield _Api(handler, httpd.server_address[1])
    finally:
        httpd.shutdown()
        httpd.server_close()
        thread.join()


def test_fetch_quote_returns_quote_when_api_answers(api: _Api) -> None:
    client = api.client_answering(json.dumps({"quote": "I am a god"}).encode())
    assert client.fetch_quote().text == "I am a god"


def test_fetch_quote_fails_when_status_is_500(api: _Api) -> None:
    client = api.client_answering(json.dumps({"quote": "x"}).encode(), status=500)
    with pytest.raises(QuoteUnavailableError):
        client.fetch_quote()


@pytest.mark.parametrize(
    "body",
    [
        b"not json",
        b"\xff\xfe",
        json.dumps({"other": "x"}).encode(),
        json.dumps(["quote"]).encode(),
        json.dumps({"quote": 5}).encode(),
        json.dumps({"quote": "   "}).encode(),
    ],
    ids=[
        "invalid-json",
        "invalid-bytes",
        "no-quote",
        "not-object",
        "not-text",
        "blank",
    ],
)
def test_fetch_quote_fails_when_response_is_unusable(api: _Api, body: bytes) -> None:
    with pytest.raises(QuoteUnavailableError):
        api.client_answering(body).fetch_quote()


def test_fetch_quote_fails_when_connection_is_refused() -> None:
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    client = KanyeRestClient(f"http://127.0.0.1:{port}/", TIMEOUT_SECONDS)
    with pytest.raises(QuoteUnavailableError):
        client.fetch_quote()


def test_fetch_quote_sends_user_agent_when_requesting(api: _Api) -> None:
    api.client_answering(json.dumps({"quote": "x"}).encode()).fetch_quote()
    assert api.received_headers["User-Agent"] == USER_AGENT
    assert api.received_headers["Accept"] == "application/json"
