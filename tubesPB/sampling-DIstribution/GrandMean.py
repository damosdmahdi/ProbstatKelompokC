import pandas as pd





FILENAME = 'surveiData.csv'
TOTAL_SAMPEL = 84

def hitung_grand_mean_saja():
    print("--- MENGHITUNG HANYA GRAND MEAN ---")
    try:
        df = pd.read_csv(FILENAME)
    except FileNotFoundError:
        print(f"ERROR: File '{FILENAME}' tidak ditemukan.")
        return
    
    for col in df.columns:
        col_lower = col.lower()
        if 'tidur' in col_lower and 'rata' in col_lower:
            df.rename(columns={col: 'durasi_tidur'}, inplace=True)
        elif 'ipk' in col_lower:
            df.rename(columns={col: 'ipk'}, inplace=True)
        elif 'timestamp' in col_lower:
            df.rename(columns={col: 'timestamp'}, inplace=True)
            
    df['ipk'] = df['ipk'].astype(str).str.replace(',', '.')
    df['ipk'] = pd.to_numeric(df['ipk'], errors='coerce')
    df['durasi_tidur'] = pd.to_numeric(df['durasi_tidur'], errors='coerce')
    df_clean = df.dropna(subset=['ipk', 'durasi_tidur']).copy()
    
    if 'timestamp' in df_clean.columns:
        df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce')
        df_clean = df_clean.sort_values(by='timestamp')
        
    df_final = df_clean.iloc[:TOTAL_SAMPEL]
    
    # Cek jumlah data
    print(f"Total data yang dihitung: {len(df_final)} responden.")
    
    grand_mean_tidur = df_final['durasi_tidur'].mean()
    grand_mean_ipk = df_final['ipk'].mean()
    
    
    print("   Grand mean dari seluruh sampel")
    print(f"1. Grand Mean Jam Tidur : {grand_mean_tidur:.3f} Jam")
    print(f"2. Grand Mean IPK : {grand_mean_ipk:.3f}")
    
    
if __name__ == "__main__":
    hitung_grand_mean_saja()