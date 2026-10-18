"""@brief Use case UC-001: read a new Kanye quote."""

from kanye_quotes.application.ports import QuoteProvider
from kanye_quotes.domain.quote import Quote


class GetQuoteUseCase:
    """@brief Gets a new quote from the quote source."""

    def __init__(self, quote_provider: QuoteProvider) -> None:
        """@brief Build the use case.

        @param quote_provider The source that delivers quotes.
        """
        ## The source that delivers quotes.
        self._quote_provider = quote_provider

    def execute(self) -> Quote:
        """@brief Get a new quote.

        @return The new quote.
        @throws QuoteUnavailableError When the source cannot deliver one.
        """
        return self._quote_provider.fetch_quote()
