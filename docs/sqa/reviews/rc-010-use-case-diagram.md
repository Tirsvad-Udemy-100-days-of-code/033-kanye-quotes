# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [UCD-001], [QC-UCD-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [3b6e9ba] |

---

## Artifact Under Review

- Instance reviewed: [UCD-001]
- Checklist used: [QC-UCD-001] (`QC-UCD-001`)
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads the language and knows the domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Actors are defined with correct UML stereotypes (e.g. `<<System>>`, `<<Actor>>`) | Pass | Actor has `<<Actor>>`, the system has `<<System>>` |
| 2 | System boundary is clearly drawn and labeled | Pass | The boundary rectangle is labelled `Kanye Says...` |
| 3 | Include/extend relationships are used correctly per UML 2.5.1, not as generic "uses" arrows | Pass | No include or extend is used; the table says why |
| 4 | Every actor participates in at least one use case (no orphan actors) | Pass | The only actor, Reader, takes part in the only use case |
| 5 | Diagram is traceable to a documented stakeholder need | Pass | Reader traces to S01 and S02 in [SA-001] |
| 6 | Use case names are verb phrases describing actor goals, not internal system operations | Pass | `Read a New Kanye Quote` is a verb phrase and a goal |
| 7 | Diagram is free of implementation detail (e.g. UI widgets, database tables) | Pass | No widget or storage is named |
| 8 | Actor and use case naming is consistent with corresponding Use Case and User Story documents | Pass | Names equal those in UC-001 and US-001 |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | UCD-001 Metadata has `Language` = en and `Domain` = it |
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

[UCD-001]: ../../use-case-diagram.md
[QC-UCD-001]: ../../../framework/qc/artifacts/qc-use-case-diagram.md
[3b6e9ba]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes/commit/3b6e9ba1e8dd0e88c0013b213013e532657aff7a
