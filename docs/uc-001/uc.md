# Read a New Kanye Quote

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [UCD-001], [US-001], [SA-001], [SSD-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [3b6e9ba] |

---

**Format:** Fully Dressed

## Fully Dressed

- **Scope:** Kanye Says... app
- **Level:** user-goal
- **Primary Actor:** Reader, as named in [UCD-001]
- **Stakeholders and Interests:**
  - S01 — a working app that follows the assignment
  - S02 — a quote shown on every click, with the assignment's function name in the code
  - S03 — a clear, dependency-free project to browse
- **Preconditions:** The app is open and shows the start screen with the placeholder text.
- **Postconditions (success guarantee):** The screen shows one quote from the quote source.

### Main Success Scenario

1. The Reader asks for a new quote.
2. The System gets a quote from the quote source.
3. The System shows the quote to the Reader.

The Reader may repeat the scenario from step 1 as often as wanted.

### Extensions (Alternative / Exception Flows)

- 2a. The quote source cannot deliver a quote (quote failure):
  1. The System tells the Reader that no quote could be fetched.
  2. The Reader may ask again from step 1.

No `<<include>>` or `<<extend>>` relationship applies.

### Special Requirements / Business Rules

| Step | Rule |
| --- | --- |
| 2 | The System waits at most 10 seconds for the quote source |
| 3 | The quote replaces the one shown before; an empty quote is a quote failure |

### Open Issues

None. The start screen layout is the assignment's starter screen: a background picture, the quote text on it, and the Kanye picture as the button below.

---

[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[SA-001]: ../stakeholder-analysis.md
[SSD-001]: ./ssd.md
[3b6e9ba]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes/commit/3b6e9ba1e8dd0e88c0013b213013e532657aff7a
