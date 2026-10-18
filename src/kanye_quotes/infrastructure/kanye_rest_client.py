"""@brief Client of the Kanye Rest API, using only the standard library."""

import http.client
import json
import urllib.request

from kanye_quotes.constants import (
    API_URL,
    QUOTE_KEY,
    REQUEST_TIMEOUT_SECONDS,
    USER_AGENT,
)
from kanye_quotes.domain.errors import QuoteUnavailableError
from kanye_quotes.domain.quote import Quote


class KanyeRestClient:
    """@brief Delivers quotes from the Kanye Rest API (see ADR-0001)."""

    def __init__(
        self,
        url: str = API_URL,
        timeout_seconds: float = REQUEST_TIMEOUT_SECONDS,
    ) -> None:
        """@brief Build the client.

        @param url The endpoint that returns one quote as JSON.
        @param timeout_seconds Seconds to wait for the endpoint.
        """
        ## The endpoint that returns one quote as JSON.
        self._url = url
        ## Seconds to wait for the endpoint.
        self._timeout_seconds = timeout_seconds

    def fetch_quote(self) -> Quote:
        """@brief Get one quote from the API.

        @return The quote in the quote key of the JSON response.
        @throws QuoteUnavailableError On a network error, a bad HTTP status,
            invalid JSON or a response without a usable quote.
        """
        try:
            request = urllib.request.Request(
                self._url,
                headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
            )
            with urllib.request.urlopen(
                request, timeout=self._timeout_seconds
            ) as response:
                payload = json.load(response)
        except (OSError, ValueError, http.client.HTTPException) as error:
            raise QuoteUnavailableError(f"No quote from {self._url}") from error
        text = payload.get(QUOTE_KEY) if isinstance(payload, dict) else None
        if not isinstance(text, str) or not text.strip():
            raise QuoteUnavailableError(f"No {QUOTE_KEY} in the response")
        return Quote(text)
