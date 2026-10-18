# Use urllib instead of requests

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001], [MIL-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The course lecture tells the participant to import the `requests` library to call the Kanye Rest API. The Business Case asks to avoid runtime dependencies unless they are needed (S03), while S02 wants code that matches the assignment. The app needs one HTTP GET of a small JSON document.

Options evaluated:

1. `requests`: matches the lecture, adds a runtime dependency to install in every `.venv`.
2. `urllib.request` from the standard library: no dependency, a few more lines of code, same behaviour for one GET.
3. `httpx`: a dependency with no benefit for one GET.

## Decision

The quote client calls the API with `urllib.request` and `json` from the standard library; the project has no runtime dependency.

## Consequences

**Positive:**

- The project installs nothing at run time; `pip install` is only needed for the optional `dev` tools.
- S03 sees no runtime dependency; the tests need no network.

**Negative:**

- The code differs from the lecture's `requests.get()` call; the README explains the mapping for S02.
- Status and error handling is written by hand (`HTTPError`, `URLError`, `json.JSONDecodeError`).

## Affected Artifacts

- [BC-001] — meets the constraint to avoid runtime dependencies
- [SA-001] — resolves the conflict between S02 and S03
- [MIL-001] — task 6 records this decision

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-001]: ../milestones/mil-001-repository-setup.md
