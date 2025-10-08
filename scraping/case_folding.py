import pandas as pd

# --- Konfigurasi ---
# Nama file CSV input (hasil dari scraping sebelumnya)
FILE_INPUT = 'mlbb_reviews.csv'
# Nama kolom yang akan dilakukan Case Folding
KOLOM_REVIEW = 'content'
# Nama file CSV output setelah Case Folding
FILE_OUTPUT_CLEAN = 'mlbb_reviews_casefolded.csv'

try:
    # 1. Memuat Data dari CSV
    print(f"Memuat data dari file: {FILE_INPUT}")
    df = pd.read_csv(FILE_INPUT)
    
    # Memeriksa apakah kolom 'content' ada di DataFrame
    if KOLOM_REVIEW not in df.columns:
        raise ValueError(f"Kolom '{KOLOM_REVIEW}' tidak ditemukan dalam file CSV.")

    # 2. Case Folding
    print(f"Melakukan Case Folding pada kolom '{KOLOM_REVIEW}'...")
    
    # Mengganti nilai NaN (Not a Number) atau kosong dengan string kosong
    # Ini memastikan metode .str.lower() dapat diterapkan pada semua baris
    df[KOLOM_REVIEW] = df[KOLOM_REVIEW].fillna('')
    
    # Menerapkan Case Folding: mengubah semua teks menjadi huruf kecil
    df[KOLOM_REVIEW] = df[KOLOM_REVIEW].str.lower()

    # 3. Menyimpan Hasil ke CSV Baru
    print(f"Menyimpan data hasil Case Folding ke file: {FILE_OUTPUT_CLEAN}")
    
    # Memilih kolom asli dan kolom baru untuk disimpan
    kolom_output = list(df.columns)
    # Anda bisa memilih untuk menyimpan hanya kolom yang telah diproses:
    # kolom_output = ['userName', 'score', 'at', 'thumbsUpCount', 'reviewCreatedVersion', 'content_casefolded']
    
    df[kolom_output].to_csv(FILE_OUTPUT_CLEAN, index=False, encoding='utf-8')

    print("---")
    print("Case Folding Selesai!")
    print(f"Data tersimpan di: {FILE_OUTPUT_CLEAN}")
    print("\nContoh Hasil:")
    print(df[['content']].head())

except FileNotFoundError:
    print(f"\nERROR: File '{FILE_INPUT}' tidak ditemukan. Pastikan Anda telah menjalankan script scraping data Mobile Legends terlebih dahulu.")
except ValueError as e:
    print(f"\nERROR: {e}")
except Exception as e:
    print(f"\nTerjadi kesalahan: {e}")