[English](Development) · **Dansk** · [Bahasa Malaysia](Development-ms)

# Udvikling

Alle kommandoer køres med `.venv` aktivt (se [Kom i gang](Getting-Started-da)).

## Tests

```bash
python -m pytest
```

Testene afspejler `src/`: `tests/unit`, `tests/integration` og `tests/e2e`. Ingen af dem kalder det rigtige API; integrationstestene bruger en lokal server på `127.0.0.1`. End-to-end-testene åbner et tkinter-vindue og springes over, når der ikke er en skærm.

## Kontroller

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy src
```

## API-dokumentation

Kildekoden bruger Doxygen-kommentarer (`@brief`, `@param`, `@return`, `@throws`). Byg HTML med [Doxygen](https://www.doxygen.nl/):

```bash
doxygen Doxyfile
```

Resultatet ligger i `docs/doxygen/`.

## Konstanter

Hver konstant (API-adressen, timeout, tekster, størrelser) er defineret ét sted i `src/kanye_quotes/constants.py`.
