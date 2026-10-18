# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [cb17f31] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001], [DICT-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | - (accepted by S01 with the plan) |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-003] |
| [MIL-002] | MIL | en | it | [BC-001], [MIL-001] | [MIL-003] | [RC-004] |
| [MIL-003] | MIL | en | it | [BC-001], [MIL-002] | - | [RC-005] |
| [DICT-001] | DICT | en | it | [BC-001], [SA-001] | - | [RC-006] |
| [ADR-0001] | ADR | - | - | [BC-001], [SA-001], [MIL-001] | source code | [RC-007] |
| [ADR-0002] | ADR | - | - | [BC-001], [MIL-001], [MIL-002] | source code | [RC-008] |
| [UCD-001] | UCD | en | it | [SA-001], [BC-001] | [US-001], [UC-001] | [RC-010] |
| [US-001] | US | en | it | [UCD-001], [BC-001] | [UC-001] | [RC-011] |
| [UC-001] | UC | en | it | [UCD-001], [US-001] | [SSD-001] | [RC-012] |
| [SSD-001] | SSD | en | it | [UC-001] | source code | [RC-013] |
| YAML files of MIL-003 | YML | - | - | [MIL-003] | - | [RC-015] |
| Workflow of MIL-003 | WF | - | - | [MIL-003], YML files of MIL-003 | - | [RC-016] (Go-with-conditions) |
| src/ and tests/ of MIL-002 | PY | - | - | [MIL-002], [UC-001], [ADR-0002] | - | [RC-014] |
| src/ and tests/ of MIL-001 | PY | - | - | [MIL-001], [ADR-0002] | - | [RC-009] |

## Coverage Notes

- Types with no instance yet: DM (concepts are in [DICT-001]), OC, SD, DCD, ERD (not needed by this small app, see [ADR-0002]).
- No DM exists: the three domain concepts are recorded in [DICT-001].
- In Upstream `-` means foundational; in Downstream `-` means nothing is built on it yet; in Last Reviewed `-` means no `RC-*` exists yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-repository-setup.md
[MIL-002]: ../milestones/mil-002-quote-app.md
[MIL-003]: ../milestones/mil-003-documentation-release.md
[DICT-001]: ../dictionary.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
[RC-006]: ./reviews/rc-006-dictionary.md
[RC-007]: ./reviews/rc-007-adr-0001.md
[RC-008]: ./reviews/rc-008-adr-0002.md
[RC-009]: ./reviews/rc-009-code-mil-001.md
[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[UC-001]: ../uc-001/uc.md
[SSD-001]: ../uc-001/ssd.md
[RC-010]: ./reviews/rc-010-use-case-diagram.md
[RC-011]: ./reviews/rc-011-user-story.md
[RC-012]: ./reviews/rc-012-use-case.md
[RC-013]: ./reviews/rc-013-ssd.md
[RC-014]: ./reviews/rc-014-code-mil-002.md
[RC-015]: ./reviews/rc-015-yaml-mil-003.md
[RC-016]: ./reviews/rc-016-workflow-mil-003.md
[ADR-0001]: ../adr/adr-0001-urllib-instead-of-requests.md
[ADR-0002]: ../adr/adr-0002-layers-and-mvvm.md
[cb17f31]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes/commit/cb17f312c33552dcff957cfe50ffa2b69249d737
