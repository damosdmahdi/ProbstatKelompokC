import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# 1. Siapkan Data Frekuensi (dari gambar histogram [2, 4, 3, 1, 2]) dan Posisi X
frekuensi = [2, 4, 3, 1, 2]
x_posisi = np.arange(len(frekuensi)) # [0, 1, 2, 3, 4]
x_labels = ["0-100", "100-200", "200-300", "300-400", "400-500"]

# 2. Hitung Nilai Mean, Median, Modus, Std Dev (sesuai frekuensi [2, 4, 3, 1, 2])
modus_val = 166.67
median_val = 200.00
mean_val = 225.00
# --- Perhitungan Variance/Std Dev untuk frekuensi [2, 4, 3, 1, 2] ---
n = sum(frekuensi) # 12
nilai_tengah = [50, 150, 250, 350, 450]
f_kali_x2 = [f * (x**2) for f, x in zip(frekuensi, nilai_tengah)]
# [2*2500, 4*22500, 3*62500, 1*122500, 2*202500] = [5000, 90000, 187500, 122500, 405000]
E_X2 = sum(f_kali_x2) / n # 810000 / 12 = 67500
variance_val = E_X2 - (mean_val**2) # 67500 - (225**2) = 67500 - 50625 = 16875
std_dev_val = np.sqrt(variance_val) # sqrt(16875) ≈ 129.90
# --------------------------------------------------------------------

# 3. Hitung Posisi X di Plot untuk Garis
skala_x = 4 / 500 # Faktor skala
modus_x_plot = modus_val * skala_x
median_x_plot = median_val * skala_x
mean_x_plot = mean_val * skala_x
mean_minus_std_dev_x_plot = (mean_val - std_dev_val) * skala_x # Posisi μ - σ
mean_plus_std_dev_x_plot = (mean_val + std_dev_val) * skala_x  # Posisi μ + σ


# 4. Proses Spline
f = CubicSpline(x_posisi, frekuensi)
x_smooth = np.linspace(x_posisi.min(), x_posisi.max(), 300)
y_smooth = f(x_smooth)

# 5. Mulai membuat plot
plt.figure(figsize=(12, 7)) # Sedikit lebarkan agar label muat

# Plot garis spline dan titik data
plt.plot(x_smooth, y_smooth, 'r-', label="Garis Distribusi (Spline)")
plt.plot(x_posisi, frekuensi, 'bo', label="Frekuensi Asli")

# Menambahkan Garis Mean, Median, Modus
plt.axvline(x=mean_x_plot, color='black', linestyle='-', linewidth=2)
plt.axvline(x=median_x_plot, color='black', linestyle='-', linewidth=2)
plt.axvline(x=modus_x_plot, color='black', linestyle='-', linewidth=2)

# =========================================================
# MENAMBAHKAN KEMBALI GARIS STANDARD DEVIATION (μ ± σ)
plt.axvline(x=mean_minus_std_dev_x_plot, color='orange', linestyle='--', linewidth=1.5, label=f'μ±σ ({std_dev_val:.2f})')
plt.axvline(x=mean_plus_std_dev_x_plot, color='orange', linestyle='--', linewidth=1.5) # Tidak perlu label ganda
# =========================================================

# Menambahkan teks label vertikal
# Posisikan sedikit lebih ke kiri/kanan agar tidak tertabrak garis std dev
plt.text(modus_x_plot - 0.15, 1.5, 'MODE', rotation=90,
         verticalalignment='center', fontsize=12, weight='bold')
plt.text(median_x_plot - 0.15, 1.5, 'MEDIAN', rotation=90,
         verticalalignment='center', fontsize=12, weight='bold')
plt.text(mean_x_plot + 0.08, 1.5, 'MEAN', rotation=90,
         verticalalignment='center', fontsize=12, weight='bold')

# 6. Kustomisasi plot
plt.title("Distribusi Curah Hujan Tanjung Priok (2021)")
plt.ylabel("Frekuensi (Jumlah Bulan)")
plt.xlabel("Curah Hujan (mm)")
plt.xticks(x_posisi, x_labels)
plt.yticks(np.arange(0, 5, 1)) # Sumbu Y sampai 4
plt.grid(True)
plt.legend() # Tampilkan legenda (termasuk label μ±σ)
plt.tight_layout()

# 7. Simpan & Tampilkan
plt.savefig("plot_distribusi_lengkap_label_vertikal_2021.png")
plt.show()