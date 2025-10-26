import numpy as np

# 1. Definisikan Data Berkelompok (dari Gambar Plot)
rentang_label = ["0-100", "100-200", "200-300", "300-400", "400-500"]
frekuensi = [2, 4, 3, 1, 2] # Sesuai dengan titik-titik di plot
batas_bawah = [0, 100, 200, 300, 400]
i = 100 # Lebar interval
n = sum(frekuensi) # Total frekuensi (12)

print(f"Data Berkelompok (n = {n} bulan):\n")

# ----------------------------------------------------
# ## Menghitung Modus (Mode)
# ----------------------------------------------------
print("Modus")
# Rumus: Modus = L + (d1 / (d1 + d2)) * i

f_modus = max(frekuensi) # Frekuensi tertinggi adalah 4
indeks_modus = frekuensi.index(f_modus) # Indeksnya adalah 1 (kelas 100-200)

L = batas_bawah[indeks_modus] # L = 100
f_sebelum = frekuensi[indeks_modus - 1] # Frekuensi sebelum = 2
f_sesudah = frekuensi[indeks_modus + 1] # Frekuensi sesudah = 3

d1 = f_modus - f_sebelum
d2 = f_modus - f_sesudah

modus = L + (d1 / (d1 + d2)) * i

print(f"Kelas Modus: {rentang_label[indeks_modus]} (Frekuensi = {f_modus})")
print(f"L = {L}, d1 = {d1}, d2 = {d2}, i = {i}")
print(f"Modus = {L} + ({d1} / ({d1} + {d2})) * {i}")
print(f"Nilai Modus: {modus:.2f} mm\n")


# ----------------------------------------------------
# ## Menghitung Median (Nilai Tengah)
# ----------------------------------------------------
print("Median")
# Rumus: Median = L + ((n/2 - F) / f) * i

posisi_median = n / 2 # Posisi = 12 / 2 = 6

frek_kumulatif = np.cumsum(frekuensi) # [2, 6, 9, 10, 12]
indeks_median = 0
for indeks, f_kum in enumerate(frek_kumulatif):
    if f_kum >= posisi_median:
        indeks_median = indeks
        break # Berhenti di indeks 1 (kelas 100-200)

L_median = batas_bawah[indeks_median] # L = 100
F = 0 if indeks_median == 0 else frek_kumulatif[indeks_median - 1] # F = 2 (frek kumulatif sebelum kelas median)
f_median = frekuensi[indeks_median] # f = 4 (frekuensi kelas median)

median = L_median + ((posisi_median - F) / f_median) * i

print(f"Posisi Median: n/2 = {posisi_median}")
print(f"Frekuensi Kumulatif: {frek_kumulatif}")
print(f"Kelas Median: {rentang_label[indeks_median]} (Data ke-{posisi_median} ada di sini)")
print(f"L = {L_median}, F = {F}, f = {f_median}, i = {i}")
print(f"Median = {L_median} + (({posisi_median} - {F}) / {f_median}) * {i}")
print(f"Nilai Median: {median:.2f} mm\n")


# ----------------------------------------------------
# ## Menghitung Mean (Rata-rata)
# ----------------------------------------------------
print("--- Mean ---")
# Rumus: Mean = Σ(f * x) / Σf

nilai_tengah = [bawah + (i / 2) for bawah in batas_bawah] # [50, 150, 250, 350, 450]
print(f"Nilai Tengah (x): {nilai_tengah}")

f_kali_x = [f * x for f, x in zip(frekuensi, nilai_tengah)]
# [2*50, 4*150, 3*250, 1*350, 2*450] = [100, 600, 750, 350, 900]
print(f"f * x: {f_kali_x}")

total_f_kali_x = sum(f_kali_x) # 100 + 600 + 750 + 350 + 900 = 2700
total_frekuensi = n # 12

mean = total_f_kali_x / total_frekuensi

print(f"Total (f * x) = {total_f_kali_x}")
print(f"Total f = {total_frekuensi}")
print(f"Mean = {total_f_kali_x} / {total_frekuensi}")
print(f"Nilai Mean: {mean:.2f} mm\n")


# ----------------------------------------------------
# ## Hasil Akhir
# ----------------------------------------------------
print("HASIL AKHIR")
print(f"Modus  : {modus:.2f} mm")
print(f"Median : {median:.2f} mm")
print(f"Mean   : {mean:.2f} mm")

print("\nPerbandingan: Modus < Median < Mean (Distribusi Miring ke Kanan)")