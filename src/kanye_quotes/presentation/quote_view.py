"""@brief The tkinter view of the quote screen (MVVM)."""

import tkinter
from pathlib import Path

from kanye_quotes.constants import (
    BACKGROUND_IMAGE,
    CANVAS_HEIGHT,
    CANVAS_WIDTH,
    KANYE_IMAGE,
    QUOTE_COLOR,
    QUOTE_FONT,
    QUOTE_TEXT_WIDTH,
    WINDOW_PADDING,
    WINDOW_TITLE,
)
from kanye_quotes.presentation.quote_view_model import QuoteViewModel

## Folder with the images of the window.
_ASSETS = Path(__file__).parent / "assets"


class QuoteView:
    """@brief The Kanye Says window: a quote on a picture and a button."""

    def __init__(self, view_model: QuoteViewModel) -> None:
        """@brief Build the window.

        @param view_model The view model whose text the window shows.
        """
        ## The view model whose text the window shows.
        self._view_model = view_model
        ## The top-level window.
        self.window = tkinter.Tk()
        self.window.title(WINDOW_TITLE)
        self.window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING)

        ## The canvas that draws the picture and the quote.
        self.canvas = tkinter.Canvas(
            self.window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT
        )
        ## Background picture; kept so tkinter does not drop it.
        self._background_image = tkinter.PhotoImage(
            master=self.window, file=str(_ASSETS / BACKGROUND_IMAGE)
        )
        self.canvas.create_image(
            CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=self._background_image
        )
        ## Canvas item id of the quote text.
        self.quote_text = self.canvas.create_text(
            CANVAS_WIDTH / 2,
            CANVAS_HEIGHT / 2,
            text=view_model.text,
            width=QUOTE_TEXT_WIDTH,
            font=QUOTE_FONT,
            fill=QUOTE_COLOR,
        )
        self.canvas.grid(row=0, column=0)

        ## Button picture; kept so tkinter does not drop it.
        self._kanye_image = tkinter.PhotoImage(
            master=self.window, file=str(_ASSETS / KANYE_IMAGE)
        )
        ## The button that asks for a new quote.
        self.kanye_button = tkinter.Button(
            self.window,
            image=self._kanye_image,
            highlightthickness=0,
            command=self.get_quote,
        )
        self.kanye_button.grid(row=1, column=0)

    def get_quote(self) -> None:
        """@brief Show a new quote; the click handler of the Kanye button."""
        self._view_model.load_quote()
        self.canvas.itemconfig(self.quote_text, text=self._view_model.text)

    def run(self) -> None:
        """@brief Open the window and handle clicks until it is closed."""
        self.window.mainloop()
