# Quote app

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the Kanye Quotes app works: one click shows a new quote from the Kanye Rest API, an API failure shows a readable message, and the tests pass offline.

## Deliverable

The tkinter app under `src/kanye_quotes/` with the starter images, the `get_quote` function, the quote client, the view model and the view, with Doxygen comments and unit tests that mock the API, merged through one pull request.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Running the app opens the "Kanye Says..." window | Window shows the background and the button | App fails to start |
| 2 | A click replaces the placeholder with a quote | Text equals the `quote` value of the API response | Text unchanged |
| 3 | A failed API call shows a message and does not crash | Error text shown, window stays open | Traceback or freeze |
| 4 | `python -m pytest` passes with no network access | Exit code 0 | Any failure or real request |
| 5 | Layers depend inward only | No domain or application import of infrastructure or tkinter | Violation |
| 6 | Every public function has a Doxygen comment | `doxygen Doxyfile` has no warning | Warning |
| 7 | The code review `RC-*` is `Go` | `qc-programming-python` checklist passed | `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Configuration, skeleton and ADR-0001 |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1: a quote on every click | Success criterion 1 in [BC-001] |
| Objective 2: assignment function name | `get_quote` |
| Offline tests | Success criterion 2 in [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-19 — within the Business Case's one-day effort plus review time.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Show a new quote on each click | The user clicks the Kanye button and sees a new quote. Write UC-001 and its SSD-001 first, with the starter screen as the wireframe, then implement it through the tasks below. | Yes | UC-001 |
| 2 | Add the quote client | Implement the infrastructure adapter that calls `https://api.kanye.rest/` with `urllib`, checks the HTTP status and reads the `quote` key from the JSON. Test it with a faked response. | No | |
| 3 | Add the quote use case | Implement the application use case and the port it needs, with the domain `Quote` value object. Test it with a fake port. | No | |
| 4 | Add the view model and view | Implement the MVVM presentation: a view model holding the quote text and the error message, and the tkinter view built from the starter `main.py` and assets. `get_quote` keeps the assignment's name. | No | |
| 5 | Add the entry point and error handling | Compose the layers in a composition root, start the window, and show a readable message when the API call fails. | No | |
| 6 | Add Doxygen comments and run the code review | Document every public item with Doxygen comments, run `doxygen` and `pytest`, and review the code against `qc-programming-python`. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-repository-setup.md
