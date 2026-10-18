[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

## Krav

- Python 3.13 eller nyere.
- `tkinter`. Tjek det med `python -m tkinter`: et lille testvindue skal åbne. På Debian eller Ubuntu kører du `sudo apt install python3-tk`.

## Opret det lokale virtuelle miljø

Windows (PowerShell):

```powershell
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Tilvalget `dev` installerer `pytest`, `ruff` og `mypy`. Hvis du kun vil køre appen, er `python -m pip install -e .` nok. Forlad miljøet med `deactivate`.

## Videre

Gå til [Brug](Usage-da) for at starte appen.
