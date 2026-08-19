# API Prediksi Harga Rumah (FastAPI & Machine Learning)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green.svg)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-orange.svg)](https://docs.pydantic.dev/)
[![Tests](https://img.shields.io/badge/Tests-Pytest%20Passing-brightgreen.svg)](#)

Project ini berisi web service API berbasis **FastAPI** untuk memprediksi harga properti/rumah menggunakan model Machine Learning (Linear Regression) dengan validasi data *strict* Pydantic v2.

---

## 1. Struktur Direktori Project

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
│   └── images/                 # Grafik plot hasil render (300 DPI)
├── tests/                      # Automated unit testing (Pytest)
├── .gitignore                  # Filter file temporary / Pycache
├── requirements.txt            # Dependency Python proyek
└── README.md                   # Laporan utama & dokumentasi petunjuk API
```

---

## 2. Install Dependency

Sebelum menjalankan API, install dependensi yang dibutuhkan:

```bash
pip install -r requirements.txt
```

---

## 3. Menjalankan Server & Dokumentasi Interaktif

Jalankan perintah berikut dari root direktori proyek:

```bash
uvicorn app.main:app --reload
```

Setelah server aktif, akses melalui browser:
- **Root URL**: `http://127.0.0.1:8000`
- **Interactive Swagger Documentation**: `http://127.0.0.1:8000/docs`
- **Alternative Redoc Documentation**: `http://127.0.0.1:8000/redoc`

---

## 4. Endpoint API

### A. `GET /`
Mengecek status keaktifan web service API.

**Contoh Respons:**
```json
{
  "pesan": "API Prediksi Harga Rumah aktif. Gunakan endpoint POST /predict."
}
```

### B. `POST /predict`
Mengirimkan data fitur properti dalam format JSON untuk mendapatkan estimasi harga rumah.

**Contoh Request Payload:**
```json
{
  "luas_tanah": 150.0,
  "luas_bangunan": 100.0,
  "jumlah_kamar": 3,
  "jumlah_kamar_mandi": 2,
  "jarak_pusat_kota": 5.0
}
```

**Contoh Respons Sukses:**
```json
{
  "status": "success",
  "prediksi_harga": 872500000.0,
  "satuan": "IDR"
}
```

---

## 5. Deskripsi Fitur Input

| Field | Tipe Data | Keterangan |
| :--- | :--- | :--- |
| `luas_tanah` | `float` | Luas tanah dalam $m^2$ |
| `luas_bangunan` | `float` | Luas bangunan dalam $m^2$ |
| `jumlah_kamar` | `int` | Jumlah kamar tidur |
| `jumlah_kamar_mandi` | `int` | Jumlah kamar mandi |
| `jarak_pusat_kota` | `float` | Jarak ke pusat kota dalam km |

---

## 6. Pengujian Otomatis (Pytest)

Jalankan suite pengujian otomatis untuk memvalidasi endpoint dan logika inferensi:

```bash
pytest tests/
```

---
*FastAPI House Price Predictor Project.*
