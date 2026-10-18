[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

## Keperluan

- Python 3.13 atau lebih baharu.
- `tkinter`. Semaknya dengan `python -m tkinter`: tetingkap ujian kecil mesti terbuka. Pada Debian atau Ubuntu jalankan `sudo apt install python3-tk`.

## Cipta persekitaran maya tempatan

Windows (PowerShell):

```powershell
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Tambahan `dev` memasang `pytest`, `ruff` dan `mypy`. Jika anda hanya mahu menjalankan aplikasi, `python -m pip install -e .` sudah cukup. Keluar daripada persekitaran dengan `deactivate`.

## Seterusnya

Pergi ke [Penggunaan](Usage-ms) untuk memulakan aplikasi.
