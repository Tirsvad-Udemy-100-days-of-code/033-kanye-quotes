import tkinter
from collections.abc import Callable, Iterator

import pytest

from kanye_quotes.application.get_quote import GetQuoteUseCase
from kanye_quotes.constants import ERROR_QUOTE, PLACEHOLDER_QUOTE
from kanye_quotes.domain.errors import QuoteUnavailableError
from kanye_quotes.domain.quote import Quote
from kanye_quotes.presentation.quote_view import QuoteView
from kanye_quotes.presentation.quote_view_model import QuoteViewModel

ViewFactory = Callable[..., QuoteView]


class FakeQuoteProvider:
    """Delivers the given quotes in order; None means a failure."""

    def __init__(self, *results: str | None) -> None:
        self._results: Iterator[str | None] = iter(results)

    def fetch_quote(self) -> Quote:
        text = next(self._results)
        if text is None:
            raise QuoteUnavailableError("fake failure")
        return Quote(text)


@pytest.fixture
def make_view() -> Iterator[ViewFactory]:
    views: list[QuoteView] = []

    def create(*results: str | None) -> QuoteView:
        use_case = GetQuoteUseCase(FakeQuoteProvider(*results))
        try:
            view = QuoteView(QuoteViewModel(use_case))
        except tkinter.TclError:
            pytest.skip("no display available for tkinter")
        views.append(view)
        return view

    try:
        yield create
    finally:
        for view in views:
            view.window.destroy()


def _shown(view: QuoteView) -> str:
    return str(view.canvas.itemcget(view.quote_text, "text"))


def test_view_shows_placeholder_when_opened(make_view: ViewFactory) -> None:
    assert _shown(make_view("a")) == PLACEHOLDER_QUOTE


def test_click_shows_quote_when_api_answers(make_view: ViewFactory) -> None:
    view = make_view("I am a god")
    view.kanye_button.invoke()
    assert _shown(view) == "I am a god"


def test_second_click_replaces_quote_when_clicked_again(
    make_view: ViewFactory,
) -> None:
    view = make_view("first", "second")
    view.kanye_button.invoke()
    view.kanye_button.invoke()
    assert _shown(view) == "second"


def test_click_shows_error_when_quote_unavailable(make_view: ViewFactory) -> None:
    view = make_view(None)
    view.kanye_button.invoke()
    assert _shown(view) == ERROR_QUOTE
