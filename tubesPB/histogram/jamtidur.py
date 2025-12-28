import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# ==========================================
# KONFIGURASI
# ==========================================
FILENAME = 'surveiData.csv' # Pastikan nama file sesuai
JUDUL_GRAFIK = "Distribusi Durasi Tidur"
LABEL_X = "Durasi Tidur (Jam)"

def plot_jam_tidur_diskrit():
    # 1. LOAD DATA
    try:
        df = pd.read_csv(FILENAME)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    # Cleaning
    for col in df.columns:
        if 'tidur' in col.lower() and 'rata' in col.lower():
            df.rename(columns={col: 'durasi_tidur'}, inplace=True)
            
    df['durasi_tidur'] = pd.to_numeric(df['durasi_tidur'], errors='coerce')
    data = df.dropna(subset=['durasi_tidur'])['durasi_tidur']
    if len(data) > 84: data = data.iloc[:84]

    # 2. HITUNG STATISTIK
    mean_val = data.mean()
    median_val = data.median()
    mode_val = float(data.mode()[0])
    
    # 3. PERSIAPAN DATA X DAN Y (TANPA PENGELOMPOKAN/BINNING)
    # Kita cari nilai minimum dan maksimum jam tidur yang ada di data
    min_val = int(data.min())
    max_val = int(data.max())
    
    # Kita buat sumbu X berupa urutan angka bulat dari min ke max (misal 3, 4, 5, ... 10)
    x_posisi = np.arange(min_val, max_val + 1)
    
    # Hitung frekuensi untuk setiap angka tersebut
    # (Berapa orang yang tidur 3 jam, berapa yang 4 jam, dst)
    freq = []
    for x in x_posisi:
        freq.append(len(data[data == x]))
    
    freq = np.array(freq)

    # 4. SPLINE CURVE
    # Langsung menggunakan x_posisi (angka jam asli)
    f_spline = CubicSpline(x_posisi, freq)
    
    # Membuat titik x yang lebih rapat untuk kurva halus
    x_smooth = np.linspace(x_posisi.min(), x_posisi.max(), 300)
    y_smooth = f_spline(x_smooth)
    y_smooth = [y if y > 0 else 0 for y in y_smooth] # Hilangkan nilai negatif jika ada

    # 5. PLOTTING
    plt.figure(figsize=(10, 6))
    
    # Plot Kurva & Titik
    plt.plot(x_smooth, y_smooth, 'r-', linewidth=2.5, alpha=0.6, label='Spline Curve')
    plt.plot(x_posisi, freq, 'bo', markersize=8, label='Data Asli')
    
    # --- GARIS STATISTIK ---
    # Perhatikan: Disini kita LANGSUNG pakai nilai mean_val, tidak perlu dimapping/dikonversi
    # karena sumbu X kita sekarang adalah angka jam tidur itu sendiri.
    
    plt.axvline(x=mode_val, color='blue', linestyle='--', linewidth=2, label=f'Mode ({mode_val})')
    plt.axvline(x=median_val, color='orange', linestyle='-.', linewidth=2, label=f'Median ({median_val})')
    plt.axvline(x=mean_val, color='green', linestyle='-', linewidth=2, label=f'Mean ({mean_val:.2f})')

    # Label Teks Vertikal
    y_max = max(freq) if len(freq) > 0 else 1
    
    # Teks Modus (Biru)
    plt.text(mode_val, y_max * 1.05, 'MODE', rotation=90, va='bottom', ha='center', 
             color='blue', fontweight='bold', fontsize=10)
    # Teks Median (Oranye)
    plt.text(median_val, y_max * 0.95, 'MEDIAN', rotation=90, va='top', ha='center', 
             color='orange', fontweight='bold', fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
    # Teks Mean (Hijau)
    plt.text(mean_val, y_max * 1.05, 'MEAN', rotation=90, va='bottom', ha='center', 
             color='green', fontweight='bold', fontsize=10)

    # Formatting
    plt.title(f"{JUDUL_GRAFIK}", fontsize=14)
    plt.xlabel(LABEL_X, fontsize=12)
    plt.ylabel("Frekuensi (Jumlah Mahasiswa)", fontsize=12)
    
    # Set X Ticks sesuai angka jam yang ada (biar sumbu X tidak menampilkan koma)
    plt.xticks(x_posisi) 
    
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper right', shadow=True)
    plt.tight_layout()
    
    plt.savefig("Grafik_JamTidur_Diskrit.png")
    print("Grafik disimpan: Grafik_JamTidur_Diskrit.png")
    plt.show()

if __name__ == "__main__":
    plot_jam_tidur_diskrit()