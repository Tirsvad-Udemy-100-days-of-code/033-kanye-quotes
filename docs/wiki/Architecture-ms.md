[English](Architecture) · [Dansk](Architecture-da) · **Bahasa Malaysia**

# Seni bina

Kod sumber terbahagi kepada empat lapisan di bawah `src/kanye_quotes/`. Import hanya menghala ke dalam; satu ujian menyemaknya.

| Lapisan | Kandungan |
| --- | --- |
| `domain` | `Quote`, `QuoteUnavailableError` |
| `application` | `GetQuoteUseCase`, port `QuoteProvider` |
| `infrastructure` | `KanyeRestClient` (penyesuai untuk API) |
| `presentation` | `QuoteViewModel`, `QuoteView`, titik masuk `main.py` (akar komposisi) |

Antara muka pengguna mengikut MVVM: model paparan memegang teks dan mengendalikan kegagalan, paparan tkinter hanya melukisnya dan memanggil model paparan. `QuoteView.get_quote` ialah pengendali klik dan mengekalkan nama tugasan.

## Mengapa `urllib` dan bukan `requests`

Kuliah menggunakan `requests`. Projek ini memanggil API dengan pustaka standard, jadi tiada apa-apa perlu dipasang untuk menjalankannya. API membalas 403 kepada User-Agent Python lalai, jadi klien menghantar User-Agent sendiri. Keputusan ini direkodkan dalam `docs/adr/adr-0001-urllib-instead-of-requests.md`.

## Dokumen projek

Pelan, kes guna `UC-001`, semakan dan keputusan (ADR-0001, ADR-0002) berada dalam folder `docs/` repositori.
