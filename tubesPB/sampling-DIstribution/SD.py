import pandas as pd

FILENAME = 'surveiData.csv'
TOTAL_TARGET = 84
SAMPLES_PER_WEEK = 21

def process_sampling_data():
    try:
        df = pd.read_csv(FILENAME)
    except FileNotFoundError:
        print(f"ERROR: File '{FILENAME}' tidak ditemukan.")
        return
    
    
    for col in df.columns:
        col_lower = col.lower()
        if 'timestamp' in col_lower:
            df.rename(columns={col: 'timestamp'}, inplace=True)
        elif 'tidur' in col_lower and 'rata' in col_lower:
            df.rename(columns={col: 'durasi_tidur'}, inplace=True)
        elif 'ipk' in col_lower:
            df.rename(columns={col: 'ipk'}, inplace=True)
            
            
    if 'durasi_tidur' not in df.columns or 'ipk' not in df.columns:
        print("ERROR: Kolom Durasi Tidur atau IPK tidak terdeteksi otomatis.")
        return
    
    # data cleaning;
    df['durasi_tidur'] = pd.to_numeric(df['durasi_tidur'], errors='coerce')
    
    
    df_clean = df.dropna(subset=['ipk', 'durasi_tidur']).copy()
    if 'timestamp' in df_clean.columns:
        df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce')
        df_clean = df_clean.sort_values(by='timestamp')
        
        
        
    if len(df_clean) >= TOTAL_TARGET:
        df_final = df_clean.iloc[:TOTAL_TARGET].copy()
    else:
        print(f"WARNING: Data valid hanya {len(df_clean)} (Kurang dari {TOTAL_TARGET}).")
        df_final = df_clean.copy()
    results = []
    
    for i in range(4):
        start = i * SAMPLES_PER_WEEK
        end = start + SAMPLES_PER_WEEK
        
        batch = df_final.iloc[start:end]
        
        row = {
            'Eksperimen': f'Minggu {i+1}',
            'Sampel (n)': len(batch),
            'Rata-rata Tidur (x̄)': round(batch['durasi_tidur'].mean(), 2),
            'Std Dev Tidur (sx)': round(batch['durasi_tidur'].std(ddof=1), 2),
            'Rata-rata IPK (ȳ)': round(batch['ipk'].mean(), 2),
            'Std Dev IPK (sy)': round(batch['ipk'].std(ddof=1), 2)
        }
        results.append(row)
        
        
    # OUTPUT
    output_df = pd.DataFrame(results)
    print("\n hasil")
    print(output_df.to_string(index=False))


if __name__ == "__main__": process_sampling_data()