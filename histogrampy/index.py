import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# 1. Siapkan Data Frekuensi dan Posisi X
frekuensi = [2, 4, 3, 1, 2]
x_posisi = np.arange(len(frekuensi)) # [0, 1, 2, 3, 4]
x_labels = ["0-100", "100-200", "200-300", "300-400", "400-500"]

# 2. Hitung Nilai Mean, Median, Modus (Hasil Perhitungan Kita)
modus_val = 166.67
median_val = 200.00
mean_val = 225.00

# 3. Hitung Posisi X di Plot untuk Garis
skala_x = 4 / 500 # Faktor skala
modus_x_plot = modus_val * skala_x
median_x_plot = median_val * skala_x
mean_x_plot = mean_val * skala_x

# 4. Proses Spline
f = CubicSpline(x_posisi, frekuensi)
x_smooth = np.linspace(x_posisi.min(), x_posisi.max(), 300)
y_smooth = f(x_smooth)

# 5. Mulai membuat plot
plt.figure(figsize=(10, 7))

# Plot garis spline dan titik data
plt.plot(x_smooth, y_smooth, 'r-', label="Garis Distribusi (Spline)")
plt.plot(x_posisi, frekuensi, 'bo', label="Frekuensi Asli")

# =========================================================
# MENAMBAHKAN GARIS MEAN, MEDIAN, MODUS
# axvline menggambar garis vertikal
plt.axvline(x=modus_x_plot, color='black', linestyle='-', linewidth=2)
plt.axvline(x=median_x_plot, color='black', linestyle='-', linewidth=2)
plt.axvline(x=mean_x_plot, color='black', linestyle='-', linewidth=2)

# Menambahkan teks label (atur posisi y agar tidak tumpang tindih)
plt.text(modus_x_plot - 0.1, 1.5, 'MODE', rotation=90, verticalalignment='center', fontsize=12, weight='bold')
plt.text(median_x_plot - 0.1, 1.5, 'MEDIAN', rotation=90, verticalalignment='center', fontsize=12, weight='bold')
plt.text(mean_x_plot + 0.05, 1.5, 'MEAN', rotation=90, verticalalignment='center', fontsize=12, weight='bold')

plt.title("Distribusi Curah Hujan Tanjung Priok (2021)")
plt.ylabel("Frekuensi (Jumlah Bulan)") 
plt.xlabel("Curah Hujan (mm)")        
plt.xticks(x_posisi, x_labels)
plt.yticks(np.arange(0, 5, 1))
plt.grid(True)
plt.legend() 
plt.tight_layout()

plt.savefig("plot_distribusi_dengan_mmm_2021.png")
plt.show()