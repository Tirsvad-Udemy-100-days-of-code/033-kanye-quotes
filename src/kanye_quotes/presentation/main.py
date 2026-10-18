"""@brief Entry point and composition root: builds every layer, starts the app."""

from kanye_quotes.application.get_quote import GetQuoteUseCase
from kanye_quotes.infrastructure.kanye_rest_client import KanyeRestClient
from kanye_quotes.presentation.quote_view import QuoteView
from kanye_quotes.presentation.quote_view_model import QuoteViewModel


def main() -> None:
    """@brief Start the Kanye Says app."""
    use_case = GetQuoteUseCase(KanyeRestClient())
    QuoteView(QuoteViewModel(use_case)).run()


if __name__ == "__main__":
    main()
