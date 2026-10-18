# Layers and MVVM for a small app

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [MIL-001], [MIL-002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [cb17f31] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The app is small: one use case, one outside service, one window. The `clean-architecture` skill gives four layers and allows a small project to merge `adapters` and `infrastructure`, never `domain`. A user interface uses MVVM by default. The project has no Design Class Diagram, since the design is three classes and a function.

Options evaluated:

1. One script like the starter `main.py`: fastest, but the code cannot be tested without a window or the network.
2. Four layers with MVVM presentation and a merged adapters and infrastructure layer: testable, small.
3. Four separate layers with separate adapters: more folders than code.

## Decision

The source is in `src/kanye_quotes/` with the packages `domain`, `application`, `infrastructure` (the adapters and infrastructure merged) and `presentation` (MVVM: view model and tkinter view); tests are in `tests/unit`, `tests/integration` and `tests/e2e`; the design is recorded in use case UC-001 and this ADR, with no DCD.

## Consequences

**Positive:**

- The use case and the view model are tested without tkinter or the network.
- The layout is the one other framework projects use, so it is familiar to S02.

**Negative:**

- More files than the starter script for a small behaviour.
- Without a DCD, the code review checks the classes against this ADR instead.

## Affected Artifacts

- [BC-001] — objective 1 and the testing criterion
- [MIL-001] — task 5 creates the skeleton
- [MIL-002] — tasks 2 to 5 implement the layers

---

[BC-001]: ../business-case.md
[MIL-001]: ../milestones/mil-001-repository-setup.md
[MIL-002]: ../milestones/mil-002-quote-app.md
[cb17f31]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes/commit/cb17f312c33552dcff957cfe50ffa2b69249d737
