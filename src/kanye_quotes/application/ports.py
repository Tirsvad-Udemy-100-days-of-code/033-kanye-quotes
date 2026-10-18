"""@brief Ports: what the use cases need from the outside world."""

from typing import Protocol

from kanye_quotes.domain.quote import Quote


class QuoteProvider(Protocol):
    """@brief The outside service that delivers a quote when asked."""

    def fetch_quote(self) -> Quote:
        """@brief Get one quote.

        @return The quote delivered by the source.
        @throws QuoteUnavailableError When no quote can be delivered.
        """
        ...
