# 🚀 Kanye Says...

A small desktop app that shows a random Kanye West quote from the [Kanye Rest API][kanye-rest] every time you click the Kanye button. It is the solution to day 33 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*, written for fellow course participants and for anyone browsing for ideas.

![The start screen of the app][img-start] ![The app showing a quote][img-quote]

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

Click the Kanye picture and the text on the speech bubble is replaced by a new quote. If the API cannot be reached, the bubble says so and the app stays open.

The code keeps the assignment's function name `get_quote` (the click handler in `QuoteView`). Instead of the `requests` library of the lecture it calls the API with the standard library (`urllib`), so the project has **no runtime dependencies** ([ADR-0001][ADR-0001]).

| Part | What it is for |
| --- | --- |
| `src/kanye_quotes/domain/` | The `Quote` value object and `QuoteUnavailableError` |
| `src/kanye_quotes/application/` | The use case `GetQuoteUseCase` and the `QuoteProvider` port |
| `src/kanye_quotes/infrastructure/` | `KanyeRestClient`, the API client |
| `src/kanye_quotes/presentation/` | The MVVM view model, the tkinter view, the images and the entry point |
| `src/kanye_quotes/constants.py` | Every constant, defined once |
| `tests/` | Unit, integration and end-to-end tests; none calls the real API |
| `docs/` | The project documents, the screenshots and the wiki (English, Danish, Bahasa Malaysia) |

## 📋 Requirements

- Python 3.13 or newer (`pyproject.toml` says `requires-python = ">=3.13"`).
- `tkinter`, which comes with the python.org installers. Check it with `python -m tkinter`: a small test window must open. On Debian or Ubuntu install it with `sudo apt install python3-tk`.
- Internet access to run the app (the tests need none).
- Optional: [Doxygen][doxygen] to build the API documentation from the source comments.

## 🛠️ Setup

Create and use a local virtual environment named `.venv` in the project folder, then update `pip` and install the project with its test tools.

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

The `dev` extra installs `pytest`, `ruff` and `mypy`. The app itself needs none of them; to only run it, `python -m pip install -e .` is enough. Leave the environment with `deactivate`.

## ▶️ Run

With the environment active:

```bash
python -m kanye_quotes
```

or use the command that the install created:

```bash
kanye-quotes
```

## 🧪 Tests

```bash
python -m pytest
```

The end-to-end tests open a tkinter window and are skipped when no display is available. Optional checks:

```bash
python -m ruff check .
python -m mypy src
doxygen Doxyfile
```

Doxygen writes the HTML documentation to `docs/doxygen/`.

## 📄 License

See the [LICENSE][license] file.

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Domain dictionary][DICT-001] | The PO terms and the IT terms |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[kanye-rest]: https://kanye.rest/
[doxygen]: https://www.doxygen.nl/
[img-start]: ./docs/images/start-screen.png
[img-quote]: ./docs/images/quote-screen.png
[license]: ./LICENSE
[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes/issues
[agents]: ./AGENTS.md
[ADR-0001]: ./docs/adr/adr-0001-urllib-instead-of-requests.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[DICT-001]: ./docs/dictionary.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
