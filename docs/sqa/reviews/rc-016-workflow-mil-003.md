# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [MIL-003], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: Workflow of [MIL-003] (`.gitea/workflows/publish-wiki.yml`)
- Checklist used: [QC-WF-001] (`QC-WF-001`)
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none (the reviewer reads the language and knows the domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | The file meets QC-YML-001 in RC-015 |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | `.gitea/workflows/publish-wiki.yml`; no copy in `.github/workflows/` |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | `name`, `on` (push to main, paths `docs/wiki/**`) and `jobs` are present |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Header states purpose, triggers, inputs, secret, what changes outside the repository and the decision |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | The one job has a descriptive name; the caller has no steps |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | actionlint 1.7.12 passes |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | Workflow and job declare `permissions: contents: read` |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | The reusable workflow and its script are pinned to the exact tag v1.2.2 (`@v1.2.2`, `tools-ref: v1.2.2`) |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | The secret is read as `secrets.TOKEN_FOR_GITEA_WIKI` and passed through `secrets:`; never echoed |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | N-A | No `run:` step in the caller; the reusable workflow passes inputs through `env:` |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | N-A | The trigger is a push to main, not pull_request_target or workflow_run |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Pass | Starts only on a push to main; no manual run, because the reusable workflow has no dry-run input |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | N-A | The reusable workflow documents its own token scope (write:repository for the wiki) |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | `runs-on: ubuntu-latest` and `timeout-minutes: 10` are set in the reusable workflow (checked at v1.2.2) |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` group `publish-wiki` queues (`cancel-in-progress: false`) |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Filtered by `branches: [main]` and `paths` |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | N-A | The caller installs no tool; the script comes from the pinned tag |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | No install to cache |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | N-A | The failing step belongs to the reusable workflow |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | No `run:` block in the caller |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | Logic is the reusable workflow `publish-wiki-pages.yml` |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Fail | Not verified on the Gitea instance: the secret `TOKEN_FOR_GITEA_WIKI` does not exist yet and no run has happened; the header says so |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | Pass | The header names the pinned tag and the script (`tools-ref`) |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | Fail | Optional: no static test of the workflows runs on pull requests |

## Overall Verdict

Go-with-conditions — every Mandatory criterion passes except 22 (not verified on the instance): the file is correct, but the wiki cannot publish until S01 creates the organization secret and the first run is checked.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Create the organization secret `TOKEN_FOR_GITEA_WIKI` (token scope write:repository), enable the wiki, and check the first run after the merge | S01 | after the MIL-003 merge |
| Optionally add a static workflow test that runs on pull requests (criterion 24) | S01 | open |

---

[MIL-003]: ../../milestones/mil-003-documentation-release.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
