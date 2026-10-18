# System Sequence Diagram

## Metadata
| Key | Value |
| --- | --- |
| ID | SSD-001 |
| CrossReference | [UC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Source Use Case

Read a New Kanye Quote ([UC-001]) — scenario: main success scenario. The quote failure (extension 2a) is the second diagram below.

## Diagram

```plantuml
@startuml
actor Reader as A
participant ":System" as S
A -> S : getQuote()
S --> A : quote
@enduml
```

Extension 2a, quote failure:

```plantuml
@startuml
actor Reader as A
participant ":System" as S
A -> S : getQuote()
S --> A : failure message
@enduml
```

## System Operations

| Step | Message | Parameters | Return | Use case step |
| --- | --- | --- | --- | --- |
| 1 | getQuote | none | quote (text), or a failure message in extension 2a | 1 (ask), 3 (show); step 2 is internal to the System |

## Lifecycle Notes

The System instance lives as long as the window is open; it keeps no state between calls except the quote shown.

---

[UC-001]: ./uc.md
