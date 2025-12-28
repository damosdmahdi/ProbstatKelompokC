#!/bin/bash

# Pastikan script dijalankan dari folder tubesPB
echo "--- Memulai Proses Setup Virtual Environment ---"

# 1. Hapus venv lama jika ada (biar bersih)
if [ -d "venv" ]; then
    echo "[1/4] Menghapus venv lama..."
    rm -rf venv
else
    echo "[1/4] Tidak ada venv lama, lanjut..."
fi

# 2. Buat venv baru
echo "[2/4] Membuat venv baru..."
python3 -m venv venv

# 3. Aktivasi venv
echo "[3/4] Mengaktifkan venv..."
source venv/bin/activate

# 4. Install Library (Pandas, Matplotlib, Scipy, Numpy)
echo "[4/4] Menginstall library yang dibutuhkan..."
pip install --upgrade pip
pip install pandas matplotlib scipy numpy

echo "--- SELESAI! ---"
echo "Sekarang jalankan perintah ini di terminal untuk mengaktifkan environment:"
echo "source venv/bin/activate"