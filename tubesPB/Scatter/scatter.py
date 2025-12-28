import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

FILENAME = 'surveiData.csv'
JUDUL = "Scatter Plot: Durasi Tidur vs IPK"
LABEL_X = "Durasi Tidur (Jam)"
LABEL_Y = "Indeks Prestasi Kumulatif (IPK)"

def buat_scatter_plot():
    # 1. LOAD DATA
    try:
        df = pd.read_csv(FILENAME)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return
    
    # Cleaning Column Names
    for col in df.columns:
        if 'tidur' in col.lower() and 'rata' in col.lower():
            df.rename(columns={col: 'durasi_tidur'}, inplace=True)
        elif 'ipk' in col.lower():
            df.rename(columns={col: 'ipk'}, inplace=True)
            
    # Cleaning Values
    df['ipk'] = df['ipk'].astype(str).str.replace(',', '.')
    df['ipk'] = pd.to_numeric(df['ipk'], errors='coerce')
    df['durasi_tidur'] = pd.to_numeric(df['durasi_tidur'], errors='coerce')
    
    # Ambil Data Valid (84 Data)
    df = df.dropna(subset=['ipk', 'durasi_tidur'])
    if len(df) > 84:
        df = df.iloc[:84]
    
    x = df['durasi_tidur']
    y = df['ipk']

    # 2. HITUNG KORELASI & REGRESI
    # Slope (m) dan Intercept (c) untuk garis y = mx + c
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    # Buat garis regresi
    line_x = np.array([x.min(), x.max()])
    line_y = slope * line_x + intercept

    # 3. PLOTTING
    plt.figure(figsize=(10, 6))
    
    # A. Scatter Points (Titik Data)
    # alpha=0.6 biar kalau ada titik numpuk kelihatan lebih gelap
    plt.scatter(x, y, color='blue', alpha=0.6, label='Data Mahasiswa', s=50, edgecolors='w')

    # B. Regression Line (Garis Tren)
    plt.plot(line_x, line_y, color='red', linewidth=2, linestyle='--', label=f'Trendline (r = {r_value:.2f})')

    # C. Formatting
    plt.title(f"{JUDUL}\n(Korelasi r: {r_value:.3f})", fontsize=14)
    plt.xlabel(LABEL_X, fontsize=12)
    plt.ylabel(LABEL_Y, fontsize=12)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(loc='upper left')

    # Tambahkan teks persamaan garis di pojok
    persamaan = f"y = {slope:.2f}x + {intercept:.2f}"
    plt.text(x.max(), y.min(), persamaan, fontsize=10, color='red', ha='right', va='bottom', bbox=dict(facecolor='white', alpha=0.8, edgecolor='red'))

    plt.tight_layout()
    print(f"Nilai Korelasi (r): {r_value}")
    plt.show()

if __name__ == "__main__":
    buat_scatter_plot()