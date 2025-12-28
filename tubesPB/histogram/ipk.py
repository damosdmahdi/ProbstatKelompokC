import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# ==========================================
# KONFIGURASI
# ==========================================
FILENAME = 'surveiData.csv'
JUDUL_GRAFIK = "Distribusi IPK Mahasiswa"
LABEL_X = "Rentang IPK"

def plot_ipk():
    # 1. LOAD DATA
    try:
        df = pd.read_csv(FILENAME)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    # Cleaning
    for col in df.columns:
        if 'ipk' in col.lower():
            df.rename(columns={col: 'ipk'}, inplace=True)
            
    df['ipk'] = df['ipk'].astype(str).str.replace(',', '.')
    df['ipk'] = pd.to_numeric(df['ipk'], errors='coerce')
    data = df.dropna(subset=['ipk'])['ipk']
    if len(data) > 84: data = data.iloc[:84]

    # 2. HITUNG STATISTIK
    mean_val = data.mean()
    median_val = data.median()
    mode_val = data.mode()[0]

    # 3. BINNING (Interval 0.4)
    bins = np.arange(2.0, 4.2, 0.4) 
    freq, bin_edges = np.histogram(data, bins=bins)
    
    x_posisi = np.arange(len(freq))
    labels = [f"{b:.1f}-{bins[i+1]:.1f}" for i, b in enumerate(bins[:-1])]

    # 4. SPLINE CURVE
    f_spline = CubicSpline(x_posisi, freq)
    x_smooth = np.linspace(x_posisi.min(), x_posisi.max(), 300)
    y_smooth = f_spline(x_smooth)
    y_smooth = [y if y > 0 else 0 for y in y_smooth]

    # 5. MAPPING POSISI
    def get_plot_pos(val):
        bin_width = bins[1] - bins[0]
        return (val - bins[0]) / bin_width - 0.5

    mean_plot = get_plot_pos(mean_val)
    med_plot = get_plot_pos(median_val)
    mode_plot = get_plot_pos(mode_val)

    # 6. PLOTTING
    plt.figure(figsize=(10, 6))
    
    plt.plot(x_smooth, y_smooth, 'r-', linewidth=2.5, alpha=0.6, label='Spline Curve')
    plt.plot(x_posisi, freq, 'bo', markersize=8, label='Data Asli')
    
    # --- BAGIAN REVISI (WARNA BEDA & LEGEND) ---
    plt.axvline(x=mode_plot, color='blue', linestyle='--', linewidth=2, label=f'Mode ({mode_val})')
    plt.axvline(x=med_plot, color='orange', linestyle='-.', linewidth=2, label=f'Median ({median_val})')
    plt.axvline(x=mean_plot, color='green', linestyle='-', linewidth=2, label=f'Mean ({mean_val:.2f})')

    y_max = max(freq)
    
    # Label Teks dengan Warna Senada
    plt.text(mode_plot, y_max * 1.05, 'MODE', rotation=90, va='bottom', ha='center', 
             color='blue', fontweight='bold', fontsize=10)
    plt.text(med_plot, y_max * 0.95, 'MEDIAN', rotation=90, va='top', ha='center', 
             color='orange', fontweight='bold', fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
    plt.text(mean_plot, y_max * 1.05, 'MEAN', rotation=90, va='bottom', ha='center', 
             color='green', fontweight='bold', fontsize=10)

    # Formatting
    plt.title(f"{JUDUL_GRAFIK}", fontsize=14)
    plt.xlabel(LABEL_X, fontsize=12)
    plt.ylabel("Frekuensi", fontsize=12)
    plt.xticks(x_posisi, labels)
    plt.grid(True, alpha=0.3)
    
    # Tampilkan Legend
    plt.legend(loc='upper left', shadow=True)
    plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":
    plot_ipk()