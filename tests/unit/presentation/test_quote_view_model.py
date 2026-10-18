from collections.abc import Iterator

from kanye_quotes.application.get_quote import GetQuoteUseCase
from kanye_quotes.constants import ERROR_QUOTE, PLACEHOLDER_QUOTE
from kanye_quotes.domain.errors import QuoteUnavailableError
from kanye_quotes.domain.quote import Quote
from kanye_quotes.presentation.quote_view_model import QuoteViewModel


class FakeQuoteProvider:
    """Delivers the given quotes in order; None means a failure."""

    def __init__(self, *results: str | None) -> None:
        self._results: Iterator[str | None] = iter(results)

    def fetch_quote(self) -> Quote:
        text = next(self._results)
        if text is None:
            raise QuoteUnavailableError("fake failure")
        return Quote(text)


def _view_model(*results: str | None) -> QuoteViewModel:
    return QuoteViewModel(GetQuoteUseCase(FakeQuoteProvider(*results)))


def test_text_is_placeholder_when_nothing_loaded() -> None:
    assert _view_model("a").text == PLACEHOLDER_QUOTE


def test_text_is_quote_after_load() -> None:
    view_model = _view_model("first")
    view_model.load_quote()
    assert view_model.text == "first"


def test_text_is_error_when_quote_unavailable() -> None:
    view_model = _view_model(None)
    view_model.load_quote()
    assert view_model.text == ERROR_QUOTE


def test_text_is_replaced_when_loaded_a_second_time() -> None:
    view_model = _view_model("first", "second")
    view_model.load_quote()
    view_model.load_quote()
    assert view_model.text == "second"
