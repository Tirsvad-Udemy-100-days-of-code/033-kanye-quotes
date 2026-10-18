"""@brief View model of the quote screen (MVVM)."""

from kanye_quotes.application.get_quote import GetQuoteUseCase
from kanye_quotes.constants import ERROR_QUOTE, PLACEHOLDER_QUOTE
from kanye_quotes.domain.errors import QuoteUnavailableError


class QuoteViewModel:
    """@brief Holds the text the quote screen shows."""

    def __init__(self, use_case: GetQuoteUseCase) -> None:
        """@brief Build the view model.

        @param use_case The use case that gets a new quote.
        """
        ## The use case that gets a new quote.
        self._use_case = use_case
        ## The text to show now.
        self._text = PLACEHOLDER_QUOTE

    @property
    def text(self) -> str:
        """@brief The text to show: the placeholder, a quote or the error."""
        return self._text

    def load_quote(self) -> None:
        """@brief Replace the text with a new quote, or with the error text."""
        try:
            self._text = self._use_case.execute().text
        except QuoteUnavailableError:
            self._text = ERROR_QUOTE
