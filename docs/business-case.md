# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [1a0e653] |

---

## Executive Summary

Lecture 033 of Udemy's 100 Days of Code asks the participant to build a small desktop app, "Kanye Says...", that shows a random Kanye West quote each time a button is clicked. The quote comes from the public Kanye Rest application programming interface (API) at https://api.kanye.rest/. This project delivers that app as a clean, tested and documented Python repository that other course participants can read and run, and that GitHub visitors can browse for ideas.

## Methodological and Standards Foundation

The project follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/`: artifacts are reviewed against their QC checklists, and quality is stated with ISO/IEC 25010:2023 characteristics. Code follows the `coding-conventions` and `clean-architecture` skills; the user interface uses the Model-View-ViewModel (MVVM) presentation pattern.

## Problem Statement

The assignment ships only a starter `main.py` with an empty `get_quote()` function. Participants who share their solutions often publish a single untested script with no instructions, so peers cannot easily run, compare or learn from it.

## Business Opportunity

A small, well-structured solution with the assignment's function names, run instructions, tests and multilingual documentation becomes a reference other participants and repository visitors can reuse.

## Objectives

1. Deliver a tkinter app that shows a new Kanye quote from the Kanye Rest API on every button click.
2. Keep the assignment's function name (`get_quote`) so peers can compare solutions.
3. Provide tests that run offline, a README, and a wiki in English, Danish and Bahasa Malaysia, with screenshots.
4. Publish the repository with a clear description and topics.

## Scope

### In Scope

- The tkinter app with the starter images, the API call and the quote display.
- Error handling for a failed API call, shown in the UI.
- `src/`, `tests/`, `docs/` layout, `pyproject.toml`, `constants.py`, Python `.gitignore`, `Doxyfile`, Doxygen comments.
- README from the framework template, with `.venv` and `pip` instructions and how to run the app and its tests.
- Wiki in en, da and ms, and screenshots for the README and the wiki.
- Repository description and topics on the git host.

### Out of Scope

- Runtime dependencies. The API is called with the standard library, so the project has none.
- Packaging for PyPI, installers, a web or mobile front end.
- Caching, history or favourites of quotes.

## Expected Benefits

### Tangible Benefits

- A runnable, tested repository with run instructions.
- Documentation in three languages with screenshots.

### Intangible Benefits

- Practice of the framework's plan-first workflow.
- A reusable template for the next 100 Days of Code assignment.

## Strategic Alignment

The project supports the participant's learning goal (S01) and the sharing goal of the course community (S02, S03) with no runtime dependencies.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | App shows a quote per click | 100 % of clicks update the text or show an error message | Manual run and unit tests with the API mocked |
| 2 | Tests pass offline | 0 failures, 0 network calls | `python -m pytest` |
| 3 | Fresh setup works from the README | Setup and run in under 10 minutes | Follow the README on a clean clone |
| 4 | Wiki languages | 3 of 3 (en, da, ms) with screenshots | Wiki page list |
| 5 | Repository metadata | Description and at least 5 topics set | Repository page |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Kanye Rest API is down or changes | App shows no quote | Catch request errors and show a readable message; tests mock the API |
| tkinter missing from the user's Python | App cannot start | README states the requirement and how to check it |
| Token in `.env` leaks into the repository | Credential exposure | `.env` is git-ignored, never read by the code, used only for repository setup |
| Screenshots need a display | README and wiki lack images | Capture them from the running app on the author's desktop |
| Translation quality in da and ms | Misleading wiki text | English is written first; da and ms are reviewed by S01 |

## Assumptions

- The Product Owner, developer and reviewer is S01.
- The Kanye Rest API stays free and unauthenticated.
- The user can reach the people the project is for (S02, S03), but no interviews are needed for this small project.
- The project is a prototype-stage learning project.

## Constraints

- Python 3.13 or newer, `venv`, `pytest`, `pyproject.toml`.
- Constants live in `constants.py`; source comments use Doxygen syntax.
- Folders `src/`, `tests/`, `docs/`.
- Work goes through branches and pull requests, one per milestone.
- Tokens in `.env` are for personal use only and are not used or tested by the project.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one day of author time; no money | Reusable reference repository, practice with the framework, a shareable learning result (qualitative; a prototype has no revenue) |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Learns, builds and reviews; owns the product |
| S02 | Wants readable, runnable code with the assignment's names |
| S03 | Wants a clear description, topics and README, without runtime dependencies |

## Recommendation

Proceed — the scope is small, the risks are mitigated and the result serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[1a0e653]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes/commit/1a0e653399f6762271c3695596dd2675af61120b
