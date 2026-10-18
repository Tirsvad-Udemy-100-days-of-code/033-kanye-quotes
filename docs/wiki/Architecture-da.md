[English](Architecture) · **Dansk** · [Bahasa Malaysia](Architecture-ms)

# Arkitektur

Kildekoden er i fire lag under `src/kanye_quotes/`. Importer peger kun indad; en test kontrollerer det.

| Lag | Indhold |
| --- | --- |
| `domain` | `Quote`, `QuoteUnavailableError` |
| `application` | `GetQuoteUseCase`, porten `QuoteProvider` |
| `infrastructure` | `KanyeRestClient` (adapteren til API'et) |
| `presentation` | `QuoteViewModel`, `QuoteView`, indgangen `main.py` (kompositionsroden) |

Brugerfladen følger MVVM: view-modellen holder teksten og håndterer fejlen, tkinter-viewet tegner den blot og kalder view-modellen. `QuoteView.get_quote` er klikhåndteringen og beholder opgavens navn.

## Hvorfor `urllib` og ikke `requests`

Lektionen bruger `requests`. Dette projekt kalder API'et med standardbiblioteket, så der ikke skal installeres noget for at køre det. API'et svarer 403 til Pythons standard-User-Agent, så klienten sender sin egen. Beslutningen står i `docs/adr/adr-0001-urllib-instead-of-requests.md`.

## Projektdokumenter

Planen, use casen `UC-001`, gennemgangene og beslutningerne (ADR-0001, ADR-0002) ligger i mappen `docs/` i repositoriet.
