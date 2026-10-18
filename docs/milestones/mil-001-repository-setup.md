# Repository setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [1a0e653] |

---

## Purpose

Decide whether the repository is ready for development: published with a description and topics, and holding the project configuration (Python 3.13+, venv, pytest, Doxygen, `.gitignore`) and the layer skeleton under `src/` and `tests/`.

## Deliverable

A repository on the git host with its description and topics set, plus `.gitignore`, `pyproject.toml`, `Doxyfile`, `constants.py`, the empty layer skeleton, a runnable `pytest` and the ADR for the standard-library HTTP choice, merged through one pull request.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The repository has a description and at least 5 topics | Visible on the repository page | Either missing |
| 2 | `.env` is ignored and no token is in the tree | `git check-ignore .env` succeeds; no secret in `git grep` | `.env` tracked or secret found |
| 3 | `pyproject.toml` requires Python 3.13+ and lists no runtime dependency | `requires-python = ">=3.13"`, empty `dependencies` | Otherwise |
| 4 | `python -m pytest` runs in a fresh `.venv` | Exit code 0 | Non-zero |
| 5 | `doxygen Doxyfile` runs | Exit code 0 with no warning | Error |
| 6 | The review `RC-*` of the code is `Go` | `qc-programming-python` checklist passed | `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [BC-001] and [SA-001] Accepted | The plan-first gate |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4: publish with description and topics | Success criterion 5 in [BC-001] |
| Constraints: Python 3.13+, venv, pytest, `pyproject.toml`, `constants.py` | Constraints in [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-18 — within the one-day effort stated in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set a one-sentence description and at least 5 topics (python, tkinter, api, udemy, 100-days-of-code) on the git host repository through its API, reading the token from the git-ignored `.env`. Serves S03. | No | |
| 2 | Add Python .gitignore | Add the standard Python `.gitignore`, extended with `.venv/`, `.env`, Doxygen output and screenshots' scratch files, so no secret or build output is committed. | No | |
| 3 | Add pyproject.toml | Configure the project: `requires-python >=3.13`, no runtime dependencies, an optional `dev` extra with `pytest`, pytest `pythonpath` and `testpaths`. | No | |
| 4 | Add Doxyfile | Add a Doxyfile that documents `src/` and writes to `docs/doxygen/`, so the Doxygen comments in the source can be built. | No | |
| 5 | Create the layer skeleton and constants.py | Create the `src/kanye_quotes` package layers (domain, application, infrastructure, presentation) and `tests/` mirror when each layer receives its first file, plus `constants.py` for the API URL, window and text constants, per the clean-architecture skill. | No | |
| 6 | Record the standard-library HTTP decision | Write ADR-0001: call the Kanye Rest API with `urllib` instead of `requests`, so the project has no runtime dependency (S03) while keeping the assignment's `get_quote` name (S02). | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[1a0e653]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes/commit/1a0e653399f6762271c3695596dd2675af61120b
