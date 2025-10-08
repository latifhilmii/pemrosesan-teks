import pandas as pd
from google_play_scraper import Sort, reviews_all

# --- Konfigurasi Scraping ---
APP_ID = 'com.levelinfinite.sgameGlobal' 
FILE_OUTPUT = 'hok_reviews.csv'
# Ambil 1000 ulasan terbaru (Anda bisa mengubah angka ini)
MAX_Ulasan = 1000 
BAHASA = 'id'
NEGARA = 'id'
# PENTING: Mengurutkan berdasarkan yang TERBARU
SORT_ORDER = Sort.NEWEST 

print(f"Memulai scraping {MAX_Ulasan} ulasan TERBARU untuk APP ID: {APP_ID}...")

# 1. Scraping Ulasan Terbaru
try:
    result = reviews_all(
        APP_ID,
        lang=BAHASA, 
        country=NEGARA,
        sort=SORT_ORDER,
        count=MAX_Ulasan, 
        filter_score_with=None
    )
    
    print(f"Total {len(result)} ulasan berhasil diambil.")

    # Mengubah hasil menjadi Pandas DataFrame
    df = pd.DataFrame(result)

except Exception as e:
    print(f"ERROR saat scraping: {e}")
    exit()

# --- Konfigurasi Filtering ---
KOLOM_REVIEW = 'content'

# 2. Case Folding (Opsional, tapi disarankan untuk konsistensi)
# Ini penting karena tanda petik bisa berupa karakter berbeda (" atau “ atau ”), 
# tetapi dalam konteks ini, kita fokus pada tanda petik ganda standar ASCII.
df[KOLOM_REVIEW] = df[KOLOM_REVIEW].fillna('')

# 3. Filtering: Memilih ulasan yang TIDAK memiliki tanda petik ganda ("")
print("Melakukan filtering: Menghapus ulasan yang mengandung tanda petik ganda (\")...")

# Membuat kolom boolean: True jika TIDAK mengandung tanda petik, False jika mengandung
mask_tanpa_petik = ~df[KOLOM_REVIEW].str.contains('"', na=False)

# Menerapkan filter
df_filtered = df[mask_tanpa_petik].copy()

print(f"Total ulasan setelah filtering: {len(df_filtered)} ulasan.")

# 4. Menyimpan Hasil ke CSV
kolom_dipilih = ['userName', 'score', 'content', 'at', 'thumbsUpCount', 'reviewCreatedVersion']
df_final = df_filtered[kolom_dipilih]

print(f"Menyimpan data ulasan yang difilter ke file: {FILE_OUTPUT}")
df_final.to_csv(FILE_OUTPUT, index=False, encoding='utf-8')

print("---")
print("Proses Selesai!")
print(f"Data tersimpan di: {FILE_OUTPUT}")
print("\nContoh Hasil:")
print(df_final.head())