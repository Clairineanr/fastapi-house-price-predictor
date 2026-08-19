# API Prediksi Harga Rumah

Project ini berisi API FastAPI untuk memprediksi harga rumah berdasarkan beberapa fitur properti menggunakan model Machine Learning (Linear Regression).

## Struktur Direktori Project

```text
fastapi-house-price-predictor/
├── app/                        # Source code utama aplikasi FastAPI
│   ├── __init__.py
│   ├── main.py                 # FastAPI endpoints & Pydantic schema
│   └── predictor.py            # Logika preprocessing & inferensi model ML
├── data/                       # Penyimpanan dataset ML
│   ├── raw/                    # Dataset mentah (CSV/JSON)
│   └── processed/              # Dataset bersih / hasil olahan
├── models/                     # Artifacts biner ML terlatih
│   ├── model_harga_rumah.pkl   # Model Linear Regression (.pkl)
│   └── scaler_harga_rumah.pkl  # StandardScaler (.pkl)
├── notebooks/                  # Jupyter Notebook untuk eksplorasi data
│   └── notebook_latihan.ipynb  # Notebook EDA & pelatihan model
├── reports/                    # Laporan bisnis & media grafik visualisasi
│   ├── images/                 # Grafik plot hasil render (300 DPI)
│   └── laporan-productionizing-machine-learning-model-transformasi-kode-monolitik-ke-web-service-komersial-api.pdf
├── .gitignore                  # Filter file temporary / Pycache
├── requirements.txt            # Dependency Python proyek
└── README.md                   # Laporan utama & dokumentasi petunjuk API
```

---

## Install Dependency

Sebelum menjalankan API, install dependensi yang dibutuhkan:

```bash
pip install -r requirements.txt
```

---

## Menjalankan Server

Jalankan perintah berikut dari root direktori proyek:

```bash
uvicorn app.main:app --reload
```

Setelah server aktif, buka browser di alamat:
- **Root URL**: `http://127.0.0.1:8000`
- **Swagger Documentation**: `http://127.0.0.1:8000/docs`

---

## Endpoint API

### 1. `GET /`
Digunakan untuk mengecek status keaktifan server.

**Contoh Respons:**
```json
{
  "pesan": "API Prediksi Harga Rumah aktif. Gunakan endpoint POST /predict."
}
```

### 2. `POST /predict`
Mengirimkan data fitur properti dalam format JSON untuk mendapatkan estimasi harga rumah.

**URL Endpoint:** `http://127.0.0.1:8000/predict`

**Contoh Request Payload:**
```json
{
  "luas_tanah": 150,
  "luas_bangunan": 100,
  "jumlah_kamar": 3,
  "jumlah_kamar_mandi": 2,
  "jarak_pusat_kota": 5.0
}
```

**Contoh Respons Sukses:**
```json
{
  "status": "success",
  "prediksi_harga": 872500000,
  "satuan": "IDR"
}
```

**Contoh Respons Error (Misal Input Kurang / Tipe Data Salah):**
```json
{
  "status": "error",
  "pesan": "Kolom berikut tidak ditemukan dalam input: ['jumlah_kamar', 'jumlah_kamar_mandi', 'jarak_pusat_kota']"
}
```

---

## Deskripsi Field Input

| Field | Tipe Data | Keterangan |
|---|---|---|
| `luas_tanah` | `float` | Luas tanah dalam m² |
| `luas_bangunan` | `float` | Luas bangunan dalam m² |
| `jumlah_kamar` | `int` | Jumlah kamar tidur |
| `jumlah_kamar_mandi` | `int` | Jumlah kamar mandi |
| `jarak_pusat_kota` | `float` | Jarak ke pusat kota dalam km |

---

## Catatan Tambahan
- Model dan scaler tersimpan pada direktori `models/`.
- Notebook pada direktori `notebooks/` digunakan untuk eksperimen/EDA dan retraining model, bukan saat web service berjalan.
