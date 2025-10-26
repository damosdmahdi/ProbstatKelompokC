import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# 1. Siapkan Data Frekuensi (DARI TABEL 2021 - BENAR) dan Posisi X
frekuensi = [
    5,  # untuk keranjang 0-100
    3,  # untuk keranjang 100-200
    2,  # untuk keranjang 200-300
    1,  # untuk keranjang 300-400
    1   # untuk keranjang 400-500
]
x_posisi = np.arange(len(frekuensi)) # [0, 1, 2, 3, 4]
x_labels = ["0-100", "100-200", "200-300", "300-400", "400-500"]

# 2. Hitung Nilai Mean, Median, Modus, Std Dev (BERDASARKAN FREKUENSI BENAR)
# --- Modus ---
batas_bawah = [0, 100, 200, 300, 400]
i = 100
n = sum(frekuensi) # 12

f_modus = max(frekuensi) # 5
indeks_modus = frekuensi.index(f_modus) # 0
L_mod = batas_bawah[indeks_modus] # 0
f_seb_mod = 0 if indeks_modus == 0 else frekuensi[indeks_modus - 1] # 0
f_ses_mod = frekuensi[indeks_modus + 1] # 3
d1_mod = f_modus - f_seb_mod # 5
d2_mod = f_modus - f_ses_mod # 2
modus_val = L_mod + (d1_mod / (d1_mod + d2_mod)) * i # ≈ 71.43

# --- Median ---
pos_med = n / 2 # 6
frek_kumulatif = np.cumsum(frekuensi) # [5, 8, 10, 11, 12]
indeks_median = 0
for indeks, f_kum in enumerate(frek_kumulatif):
    if f_kum >= pos_med:
        indeks_median = indeks
        break # Berhenti di indeks 1 (kelas 100-200)
L_med = batas_bawah[indeks_median] # 100
F_med = 0 if indeks_median == 0 else frek_kumulatif[indeks_median - 1] # 5
f_med = frekuensi[indeks_median] # 3
median_val = L_med + ((pos_med - F_med) / f_med) * i # ≈ 133.33

# --- Mean ---
nilai_tengah_mean = [bawah + (i / 2) for bawah in batas_bawah] # [50, 150, 250, 350, 450]
f_kali_x_mean = [f * x for f, x in zip(frekuensi, nilai_tengah_mean)] # [250, 450, 500, 350, 450]
mean_val = sum(f_kali_x_mean) / n # 2000 / 12 ≈ 166.67

# --- Variance & Std Dev ---
f_kali_x2 = [f * (x**2) for f, x in zip(frekuensi, nilai_tengah_mean)]
# [5*2500, 3*22500, 2*62500, 1*122500, 1*202500] = [12500, 67500, 125000, 122500, 202500]
E_X2 = sum(f_kali_x2) / n # 530000 / 12
variance_val = E_X2 - (mean_val**2) # (530000/12) - (2000/12)**2 ≈ 16388.89
std_dev_val = np.sqrt(variance_val) # ≈ 128.02
# --------------------------------------------------------------------

# 3. Hitung Posisi X di Plot untuk Garis (BERDASARKAN NILAI BARU)
skala_x = 4 / 500 # Faktor skala
modus_x_plot = modus_val * skala_x     # ≈ 0.57
median_x_plot = median_val * skala_x   # ≈ 1.07
mean_x_plot = mean_val * skala_x       # ≈ 1.33
mean_minus_std_dev_x_plot = (mean_val - std_dev_val) * skala_x # ≈ 0.31
mean_plus_std_dev_x_plot = (mean_val + std_dev_val) * skala_x  # ≈ 2.36

# 4. Proses Spline (Menggunakan frekuensi BENAR)
f = CubicSpline(x_posisi, frekuensi)
x_smooth = np.linspace(x_posisi.min(), x_posisi.max(), 300)
y_smooth = f(x_smooth)

# 5. Mulai membuat plot
plt.figure(figsize=(12, 7))

# Plot garis spline dan titik data (sesuai frekuensi BENAR)
plt.plot(x_smooth, y_smooth, 'r-', label="Garis Distribusi (Spline)")
plt.plot(x_posisi, frekuensi, 'bo', label="Frekuensi Asli (Tabel)")

# Menambahkan Garis Mean, Median, Modus (di posisi BENAR)
plt.axvline(x=mean_x_plot, color='black', linestyle='-', linewidth=2)
plt.axvline(x=median_x_plot, color='black', linestyle='-', linewidth=2)
plt.axvline(x=modus_x_plot, color='black', linestyle='-', linewidth=2)

# Menambahkan Garis Standard Deviation (μ ± σ) (di posisi BENAR)
plt.axvline(x=mean_minus_std_dev_x_plot, color='orange', linestyle='--', linewidth=1.5, label=f'μ±σ ({std_dev_val:.2f})')
plt.axvline(x=mean_plus_std_dev_x_plot, color='orange', linestyle='--', linewidth=1.5)

# Menambahkan teks label vertikal (di posisi BENAR)
# Sesuaikan posisi Y karena puncak sekarang di Y=5
plt.text(modus_x_plot - 0.15, 2.5, 'MODE', rotation=90,
         verticalalignment='center', fontsize=12, weight='bold')
plt.text(median_x_plot - 0.15, 2.5, 'MEDIAN', rotation=90,
         verticalalignment='center', fontsize=12, weight='bold')
plt.text(mean_x_plot + 0.08, 2.5, 'MEAN', rotation=90,
         verticalalignment='center', fontsize=12, weight='bold')

# 6. Kustomisasi plot
plt.title("Distribusi Curah Hujan Tanjung Priok (2021) - Data Tabel")
plt.ylabel("Frekuensi (Jumlah Bulan)")
plt.xlabel("Curah Hujan (mm)")
plt.xticks(x_posisi, x_labels)
# Sesuaikan batas atas yticks karena frekuensi tertinggi sekarang 5
plt.yticks(np.arange(0, 6, 1)) # Tanda 0, 1, 2, 3, 4, 5
plt.grid(True)
plt.legend()
plt.tight_layout()

# 7. Simpan & Tampilkan
plt.savefig("plot_distribusi_tabel_lengkap_2021.png") # Nama file baru
plt.show()