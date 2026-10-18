import pytest

from kanye_quotes.application.get_quote import GetQuoteUseCase
from kanye_quotes.domain.errors import QuoteUnavailableError
from kanye_quotes.domain.quote import Quote


class FakeQuoteProvider:
    def __init__(self, quote: Quote | None) -> None:
        self._quote = quote

    def fetch_quote(self) -> Quote:
        if self._quote is None:
            raise QuoteUnavailableError("fake failure")
        return self._quote


def test_execute_returns_quote_when_provider_succeeds() -> None:
    quote = Quote("Sometimes you have to get rid of everything")
    assert GetQuoteUseCase(FakeQuoteProvider(quote)).execute() is quote


def test_execute_propagates_error_when_provider_fails() -> None:
    with pytest.raises(QuoteUnavailableError):
        GetQuoteUseCase(FakeQuoteProvider(None)).execute()
