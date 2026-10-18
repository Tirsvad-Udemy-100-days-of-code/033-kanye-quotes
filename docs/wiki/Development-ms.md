[English](Development) · [Dansk](Development-da) · **Bahasa Malaysia**

# Pembangunan

Semua arahan dijalankan dengan `.venv` aktif (lihat [Bermula](Getting-Started-ms)).

## Ujian

```bash
python -m pytest
```

Ujian mencerminkan `src/`: `tests/unit`, `tests/integration` dan `tests/e2e`. Tiada satu pun memanggil API sebenar; ujian integrasi menggunakan pelayan tempatan pada `127.0.0.1`. Ujian hujung ke hujung membuka tetingkap tkinter dan dilangkau apabila tiada paparan.

## Semakan

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy src
```

## Dokumentasi API

Kod sumber menggunakan komen Doxygen (`@brief`, `@param`, `@return`, `@throws`). Bina HTML dengan [Doxygen](https://www.doxygen.nl/):

```bash
doxygen Doxyfile
```

Hasilnya berada dalam `docs/doxygen/`.

## Pemalar

Setiap pemalar (alamat API, had masa, teks, saiz) ditakrifkan sekali dalam `src/kanye_quotes/constants.py`.
