"""@brief Constants of the Kanye Quotes app, defined once for every layer."""

## The Kanye Rest API endpoint that returns one random quote as JSON.
API_URL = "https://api.kanye.rest/"

## Seconds to wait for the API before giving up.
REQUEST_TIMEOUT_SECONDS = 10

## The JSON key that holds the quote text in the API response.
QUOTE_KEY = "quote"

## Title of the application window.
WINDOW_TITLE = "Kanye Says..."

## Padding in pixels around the window content.
WINDOW_PADDING = 50

## Text on the canvas before the first click.
PLACEHOLDER_QUOTE = "Kanye Quote Goes HERE"

## Text on the canvas when no quote could be fetched.
ERROR_QUOTE = "Could not get a quote. Check your connection and try again."

## Canvas width in pixels, matching the background image.
CANVAS_WIDTH = 300

## Canvas height in pixels, matching the background image.
CANVAS_HEIGHT = 414

## Wrap width in pixels of the quote text.
QUOTE_TEXT_WIDTH = 250

## Font of the quote text: family, size, weight.
QUOTE_FONT = ("Arial", 30, "bold")

## Colour of the quote text.
QUOTE_COLOR = "white"

## File name of the background image in the presentation assets folder.
BACKGROUND_IMAGE = "background.png"

## File name of the button image in the presentation assets folder.
KANYE_IMAGE = "kanye.png"
