**English** · [Dansk](Architecture-da) · [Bahasa Malaysia](Architecture-ms)

# Architecture

The source is in four layers under `src/kanye_quotes/`. Imports point inward only; a test checks it.

| Layer | Holds |
| --- | --- |
| `domain` | `Quote`, `QuoteUnavailableError` |
| `application` | `GetQuoteUseCase`, the `QuoteProvider` port |
| `infrastructure` | `KanyeRestClient` (the adapter for the API) |
| `presentation` | `QuoteViewModel`, `QuoteView`, the entry point `main.py` (the composition root) |

The user interface follows MVVM: the view model holds the text and handles the failure, the tkinter view only draws it and calls the view model. `QuoteView.get_quote` is the click handler and keeps the assignment's name.

## Why `urllib` and not `requests`

The lecture uses `requests`. This project calls the API with the standard library, so nothing has to be installed to run it. The API answers 403 to the default Python User-Agent, so the client sends its own. The decision is recorded in `docs/adr/adr-0001-urllib-instead-of-requests.md`.

## Project documents

The plan, the use case `UC-001`, the reviews and the decisions (ADR-0001, ADR-0002) are in the `docs/` folder of the repository.
