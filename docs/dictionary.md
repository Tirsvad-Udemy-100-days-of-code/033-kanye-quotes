# Domain Dictionary (PO and IT terms)

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional IT term. PO language: English (`en`), domain `it`. The dictionary covers the words of the Kanye Quotes app: use case UC-001 and the source code.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| quote | en | Quote | A sentence attributed to Kanye West that the app shows. | UC, SSD | source code |
| quote source | en | QuoteProvider | The outside service that delivers a quote when asked. | UC, SSD | source code |
| quote failure | en | QuoteUnavailableError | The situation in which the quote source cannot deliver a quote. | UC | source code |

## Rules

- The Domain Model, use cases and user stories use the PO term; the Operation
  Contract, Sequence Diagram, Design Class Diagram and ERD use the IT term.
  This project has no Domain Model: the three concepts are recorded here.
- One IT term per PO term and one PO term per IT term; no synonyms.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
