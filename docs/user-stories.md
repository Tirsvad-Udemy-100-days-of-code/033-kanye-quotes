# User Story

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [UCD-001], [UC-001], [BC-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [3b6e9ba] |

---

## Purpose and Scope

Epic: the Quote app gateway ([MIL-002]), objective 1 of [BC-001]. One story covers the only goal of the app.

## Story List

### US-001.01

- **Statement:** As a Reader, I want to see a new Kanye quote when I click the Kanye button, so that I can read a different quote each time.
- **Acceptance Criteria:**
  - Given the app is open, when the Reader clicks the button, then the text shows a quote from the quote source.
  - Given a quote is shown, when the Reader clicks again, then the text is replaced by a new quote.
  - Given the quote source is unavailable, when the Reader clicks, then the text says no quote could be fetched and the app stays open.
- **Traces to:** [UC-001], [MIL-002]
- **Size:** fits one iteration (about half a day).

## INVEST Check

Independent, Negotiable, Valuable, Estimable, Small and Testable: all hold; there is no exception.

---

[UCD-001]: ./use-case-diagram.md
[UC-001]: ./uc-001/uc.md
[BC-001]: ./business-case.md
[MIL-002]: ./milestones/mil-002-quote-app.md
[3b6e9ba]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes/commit/3b6e9ba1e8dd0e88c0013b213013e532657aff7a
