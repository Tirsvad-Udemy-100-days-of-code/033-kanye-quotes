# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [UC-001], [QC-UC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [UC-001]
- Checklist used: [QC-UC-001] (`QC-UC-001`)
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads the language and knows the domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Consists of a single, concise paragraph summarizing only the primary success scenario | N-A | Format is Fully Dressed, not Brief |
| 2 | Written as an informal multi-paragraph narrative; may mention some alternate flows without formal structure | N-A | Format is Fully Dressed, not Casual |
| 3 | All standard sections are present: actors, preconditions, postconditions, main success scenario, alternative/exception flows | Pass | Sections present: scope, level, actor, stakeholders, pre- and postconditions, main scenario, extensions, rules, open issues |
| 4 | Preconditions and postconditions are explicitly defined | Pass | Preconditions and postconditions are stated |
| 5 | Primary actor is explicitly stated | Pass | Primary actor Reader is stated |
| 6 | Stakeholders and their interests are stated | Pass | S01, S02, S03 with their interests |
| 7 | Main success scenario is written as clear, numbered steps | Pass | Main scenario has three numbered steps |
| 8 | Alternative/exception flows correctly reference `<<include>>`/`<<extend>>` use cases where relevant, per UML 2.5.1 | N-A | No include or extend relationship applies; the extension is a plain alternative flow |
| 9 | Explicit business rules are captured per step where applicable, rather than embedded loosely in narrative text | Pass | Business rules table has one row per applicable step |
| 10 | Naming of actors and use case title is consistent with the corresponding Use Case Diagram and User Stories | Pass | Title and actor equal UCD-001 and US-001 |
| 11 | Scope/level (e.g. summary, user-goal, subfunction) is explicitly stated | Pass | Scope and level (user-goal) are stated |
| 12 | Use case is written from the actor's goal perspective, free of UI or implementation detail | Pass | Written from the Reader's goal; no widget or library named |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | UC-001 Metadata has `Language` = en and `Domain` = it |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register fits the registry's row for the type (IT Professional English) |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The document uses `quote` and `quote source` as DICT-001 defines them |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists in `docs/` |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | Initial version; language and domain never changed |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Reviewer is the AI as stand-in for S01 (not independent); English and the IT domain are read without a second reviewer |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out or are named standards |

## Overall Verdict

Go — all Mandatory criteria pass; the review is autonomous and not independent, so S01 can challenge it in the final summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[UC-001]: ../../uc-001/uc.md
[QC-UC-001]: ../../../framework/qc/artifacts/qc-use-case.md
