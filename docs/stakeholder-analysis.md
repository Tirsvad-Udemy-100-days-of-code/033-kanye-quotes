# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Identify who is affected by the Kanye Quotes project and what each needs. Stakeholders are classified on the Power/Interest grid (Mendelow) and concerns are mapped to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Learn, finish the assignment and keep a clean repository |
| S02 | Udemy coursists | Fellow course participants | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README run instructions |
| S03 | GitHub viewers | Repository visitors | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides the scope, writes and reviews everything.
- **Keep Informed (S02):** cannot change the project but reads and compares the code closely.
- **Monitor (S03):** browses occasionally; good repository metadata meets their needs.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | A working app that follows the assignment | Functionality |
| S01 | Clean structure, tests, conventions | Supportability |
| S02 | Readable code with the assignment's function names | Supportability |
| S02 | Instructions that work the first time | Usability |
| S03 | Description, topics, README, no runtime dependencies | Usability, Implementation |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull requests | Per milestone | Plan, reviews, pull request | All |
| S02 | README and wiki | Once, at release | Run instructions, wiki in en, da, ms | MIL-003 |
| S03 | Repository page | Once | Description, topics, README | MIL-001, MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| The course uses the `requests` library, S03 wants no runtime dependencies | S02, S03 | Call the API with the standard library (`urllib`); keep the assignment's function name `get_quote` |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Working app | Objective 1 in [BC-001] |
| S02 | Assignment function names, run instructions | Objectives 2 and 3 in [BC-001] |
| S03 | Description and topics | Objective 4 in [BC-001] |

## Sign-Off

Reviewed in RC-002 (AI as stand-in for S01); the plan was accepted by S01 in chat.

---

[BC-001]: ./business-case.md
