import pandas as pd

FILENAME = 'surveiData.csv'
TOTAL_SAMPEL = 84

def hitung_grand_std():
    print("--- MENGHITUNG GRAND STANDARD DEVIATION (n - 1) ---")
    
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
            
            
    df['ipk'] = df['ipk'].astype(str).str.replace(',', '.')
    df['ipk'] = pd.to_numeric(df['ipk'], errors='coerce')
    df['durasi_tidur'] = pd.to_numeric(df['durasi_tidur'], errors='coerce')
    
    
    df_clean = df.dropna(subset=['ipk', 'durasi_tidur']).copy()
    if len(df_clean) > TOTAL_SAMPEL:
        df_final = df_clean.iloc[:TOTAL_SAMPEL]
    else:
        df_final = df_clean
    
    print(f"Data valid yang dihitung: {len(df_final)} responden.")
    
    
    grand_std_tidur = df_final['durasi_tidur'].std(ddof=1)
    grand_std_ipk = df_final['ipk'].std(ddof=1)
    
    
    print(f"Grand Std Dev Jam Tidur : {grand_std_tidur:.4f}")
    print(f"\nGrand Std Dev IPK       : {grand_std_ipk:.4f}")

if __name__ == "__main__":
    hitung_grand_std()