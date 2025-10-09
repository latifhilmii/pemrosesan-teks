import pandas as pd
from google_play_scraper import Sort, reviews

# 1. Tentukan ID aplikasi 
app_id = 'com.mobile.legends'

# --- PASTIKAN BAGIAN INI DIJALANKAN DULU UNTUK MEMBUAT df_reviews ---
# 2. Lakukan Scrapping (target 1000 ulasan)
print("Memulai scrapping data...")
result, continuation_token = reviews(
    app_id,
    lang='id', # Bahasa Indonesia
    country='id', # Indonesia
    sort=Sort.NEWEST, # Mengurutkan berdasarkan yang terbaru
    count=1000, # Target 1000 ulasan
    filter_score_with=None # Mengambil semua rating (1 sampai 5)
)

# 3. Konversi hasil ke DataFrame pandas
df_reviews = pd.DataFrame(result)
print(f"✅ Data berhasil di-scrapping: {len(df_reviews)} ulasan.")
# ---------------------------------------------------------------------

# =================================================================
# === PENAMBAHAN TAHAP 4: CASE FOLDING ===
# =================================================================

# 4. Lakukan Case Folding pada kolom 'content'
# Hasilnya disimpan di kolom baru bernama 'content_clean'
df_reviews['content_clean'] = df_reviews['content'].str.lower()
print("✅ Tahap 4: Case Folding pada kolom 'content' selesai.")

# =================================================================
# === TAHAP 5: PENGHAPUSAN KOLOM & FINALISASI DATA ===
# =================================================================

columns_to_drop_recommended = [
    'reviewId', 
    'userImage', 
    'thumbsUpCount', 
    'reviewCreatedVersion',
    'replyContent',
    'repliedAt'
]

# Terapkan penghapusan kolom
# Kita mulai dengan df_reviews yang sudah ada kolom 'content_clean'-nya
df_reviews_clean = df_reviews.drop(columns=columns_to_drop_recommended, errors='ignore')

print("✅ Tahap 5: Penghilangan Kolom Selesai.")
print(f"Kolom yang tersisa: {df_reviews_clean.columns.tolist()}")

# --- 6. Simpan Dataset Hasil Pembersihan dan Case Folding ---
file_name_final = 'mlbb_reviews_clean.csv'
df_reviews_clean.to_csv(file_name_final, index=False)
print(f"✅ Tahap 6: Data akhir disimpan sebagai: {file_name_final}")

print("\nContoh Data Setelah Pembersihan dan Case Folding:")
print(df_reviews_clean[['userName', 'score', 'at', 'content_clean']].head())