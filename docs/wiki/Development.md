**English** · [Dansk](Development-da) · [Bahasa Malaysia](Development-ms)

# Development

All commands run with the `.venv` active (see [Getting started](Getting-Started)).

## Tests

```bash
python -m pytest
```

The tests mirror `src/`: `tests/unit`, `tests/integration` and `tests/e2e`. None of them calls the real API; the integration tests use a local server on `127.0.0.1`. The end-to-end tests open a tkinter window and are skipped when there is no display.

## Checks

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy src
```

## API documentation

The source uses Doxygen comments (`@brief`, `@param`, `@return`, `@throws`). Build the HTML with [Doxygen](https://www.doxygen.nl/):

```bash
doxygen Doxyfile
```

The output is in `docs/doxygen/`.

## Constants

Every constant (the API URL, the timeout, texts, sizes) is defined once in `src/kanye_quotes/constants.py`.
