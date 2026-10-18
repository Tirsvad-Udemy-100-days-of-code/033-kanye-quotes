**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

## Requirements

- Python 3.13 or newer.
- `tkinter`. Check it with `python -m tkinter`: a small test window must open. On Debian or Ubuntu run `sudo apt install python3-tk`.

## Create the local virtual environment

Windows (PowerShell):

```powershell
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The `dev` extra installs `pytest`, `ruff` and `mypy`. To only run the app, `python -m pip install -e .` is enough. Leave the environment with `deactivate`.

## Next

Go to [Usage](Usage) to start the app.
