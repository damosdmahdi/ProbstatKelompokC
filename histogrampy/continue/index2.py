import numpy as np

# 1. Definisikan Data Asli (Tidak Berkelompok) Tahun 2021
curah_hujan_2021 = [
    332.4, 466.8, 190.1, 88.6, 249.7, 130.6, 47.0, 65.6,
    83.4, 247.2, 52.0, 162.9
]
n_asli = len(curah_hujan_2021)
print(f"Data Curah Hujan (n = {n_asli} bulan):\n{curah_hujan_2021}\n")

# --- Menghitung Mean ---
print("--- 1. Mean ---")
# Rumus: Mean = Σ(xi) / n
total_curah_hujan = sum(curah_hujan_2021)
mean_asli = total_curah_hujan / n_asli
print(f"Rumus: Σ(xi) / n")
print(f"Total Curah Hujan (Σxi) = {total_curah_hujan:.1f}")
print(f"Jumlah Data (n) = {n_asli}")
print(f"Mean = {total_curah_hujan:.1f} / {n_asli}")
print(f"Nilai Mean (μ): {mean_asli:.3f} mm\n")

# --- Menghitung Median ---
print("--- 2. Median ---")
# Rumus: Urutkan data, ambil nilai tengah
# Untuk n genap: (Data ke-(n/2) + Data ke-(n/2 + 1)) / 2
data_terurut = sorted(curah_hujan_2021)
posisi1_idx = int(n_asli / 2) - 1 # Indeks data ke n/2
posisi2_idx = int(n_asli / 2)     # Indeks data ke n/2 + 1
nilai1 = data_terurut[posisi1_idx]
nilai2 = data_terurut[posisi2_idx]
median_asli = (nilai1 + nilai2) / 2
print(f"Data Terurut: {data_terurut}")
print(f"Rumus (n genap): (Data ke-{posisi1_idx+1} + Data ke-{posisi2_idx+1}) / 2")
print(f"Nilai data ke-{posisi1_idx+1}: {nilai1}")
print(f"Nilai data ke-{posisi2_idx+1}: {nilai2}")
print(f"Median = ({nilai1} + {nilai2}) / 2")
print(f"Nilai Median: {median_asli:.2f} mm\n")

# --- Menghitung Variance ---
print("--- 3. Variance ---")
# Rumus: σ² = Σ(xi - μ)² / N (Population Variance)
selisih_kuadrat = [(x - mean_asli)**2 for x in curah_hujan_2021]
total_selisih_kuadrat = sum(selisih_kuadrat)
variance_asli = total_selisih_kuadrat / n_asli
print(f"Rumus: Σ(xi - μ)² / N")
print(f"Nilai Mean (μ): {mean_asli:.3f}")
# print(f"Selisih Kuadrat (xi - μ)²: {[f'{val:.3f}' for val in selisih_kuadrat]}") # Detail jika diperlukan
print(f"Total Selisih Kuadrat Σ(xi - μ)²: {total_selisih_kuadrat:.3f}")
print(f"Jumlah Data (N) = {n_asli}")
print(f"Variance (σ²) = {total_selisih_kuadrat:.3f} / {n_asli}")
print(f"Nilai Variance: {variance_asli:.3f} mm²\n")

# --- Menghitung Modus (Estimasi dari Data Berkelompok) ---
print("--- 4. Modus ---")
# Menggunakan data berkelompok untuk estimasi
rentang_label = ["0-100", "100-200", "200-300", "300-400", "400-500"]
frekuensi = [5, 3, 2, 1, 1] # Frekuensi sesuai tabel 2021
batas_bawah = [0, 100, 200, 300, 400]
i = 100
n_kelompok = sum(frekuensi)

# Perhitungan Modus
f_modus = max(frekuensi)
indeks_modus = frekuensi.index(f_modus)
L = batas_bawah[indeks_modus]
f_sebelum = 0 if indeks_modus == 0 else frekuensi[indeks_modus - 1]
f_sesudah = frekuensi[indeks_modus + 1]
d1 = f_modus - f_sebelum
d2 = f_modus - f_sesudah
modus_kelompok = L + (d1 / (d1 + d2)) * i
print("Estimasi dari Data Berkelompok:")
print(f"Rumus: L + (d1 / (d1 + d2)) * i")
print(f"Kelas Modus: {rentang_label[indeks_modus]} (f={f_modus})")
print(f"L = {L}, d1 = {d1}, d2 = {d2}, i = {i}")
print(f"Modus = {L} + ({d1} / ({d1} + {d2})) * {i}")
print(f"Nilai Modus: {modus_kelompok:.2f} mm\n") # Hasil estimasi

# --- Hasil Akhir ---
print("========== HASIL AKHIR ==========")
print(f"Mean          : {mean_asli:.3f} mm")
print(f"Median        : {median_asli:.2f} mm")
print(f"Variance      : {variance_asli:.3f} mm²")
std_dev_asli = np.sqrt(variance_asli)
print(f"Standard Dev  : {std_dev_asli:.3f} mm")
print(f"Modus         : {modus_kelompok:.2f} mm")
print("=================================")