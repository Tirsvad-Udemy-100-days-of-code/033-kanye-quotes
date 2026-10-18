# Documentation and release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [1a0e653] |

---

## Purpose

Decide whether the project is ready to share: a README that a newcomer can follow, and a wiki in English, Danish and Bahasa Malaysia, both with screenshots of the running app.

## Deliverable

`README.md` built from the framework template, the screenshots, and the wiki pages under `docs/wiki/` in three languages, merged through one pull request.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `check-readme.sh` reports no finding | Exit code 0 | Finding |
| 2 | The README setup, run and test commands work on a clean clone | Followed once, app and tests run | A command fails |
| 3 | The README documents creating `.venv` and `python -m pip install --upgrade pip` | Both present | Missing |
| 4 | The wiki has the same pages in en, da and ms | `Home.md`, `Home-da.md`, `Home-ms.md` and each other page in all three | A page missing in a language |
| 5 | README and wiki include a screenshot of the app | Image files exist and render | Missing or broken image |
| 6 | `check-languages.sh` reports no finding | Exit code 0 | Finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The app must exist to be screenshotted and documented |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3: README and three-language wiki with screenshots | Success criteria 3 and 4 in [BC-001] |
| S02 and S03 concerns | Communication Requirements in [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-20 — within the Business Case's one-day effort plus review time.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture screenshots of the app | Run the app and capture the start screen and a screen with a quote into `docs/images/`, for the README and the wiki (S02, S03). | No | |
| 2 | Write the README | Build `README.md` from the framework template: overview, requirements, creating and using a local `.venv`, `python -m pip install --upgrade pip`, running the app and the tests, license and links, with the screenshots. | No | |
| 3 | Write the English wiki | Write `docs/wiki/` pages in English (Home, Getting started, Usage, Development, Architecture) with the screenshots, `_Sidebar.md` and `_Footer.md`. English is the authoritative text. | No | |
| 4 | Translate the wiki to Danish | Add the same page set as `<Page>-da.md`, each starting with the language line; code and commands stay in English. | No | |
| 5 | Translate the wiki to Bahasa Malaysia | Add the same page set as `<Page>-ms.md`, each starting with the language line; code and commands stay in English. | No | |
| 6 | Add the wiki publish workflow | Copy `templates/ci/publish-wiki.yml` from the framework so the wiki reaches the git host's wiki by merge. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-002]: ./mil-002-quote-app.md
[1a0e653]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-kanye-quotes/commit/1a0e653399f6762271c3695596dd2675af61120b
