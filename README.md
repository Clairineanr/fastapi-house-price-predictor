# API Prediksi Harga Rumah

Project ini berisi API FastAPI sederhana untuk memprediksi harga rumah dari beberapa fitur properti. Model yang dipakai adalah Linear Regression.

## File penting

```text
├── main.py                # Aplikasi FastAPI
├── predictor.py           # Load model, preprocessing, dan prediksi
├── model_harga_rumah.pkl  # Model terlatih
├── scaler_harga_rumah.pkl # Scaler untuk data input
├── notebook_latihan.ipynb # Notebook untuk training
└── README.md
```

## Install dependency

Kalau Python sudah siap, install paket ini dulu:

```bash
pip install fastapi uvicorn scikit-learn pandas numpy joblib
```

## Menjalankan server

Jalankan perintah berikut dari folder `final`:

```bash
uvicorn main:app --reload
```

Kalau server sudah hidup, buka:

`http://127.0.0.1:8000`

## Endpoint

### `GET /`

Dipakai untuk cek apakah server sudah aktif.

Contoh respons:

```json
{
  "pesan": "API Prediksi Harga Rumah aktif. Gunakan endpoint POST /predict."
}
```

### `POST /predict`

Kirim data properti dalam format JSON, lalu API akan mengembalikan hasil prediksi.

URL:

`http://127.0.0.1:8000/predict`

Contoh request:

```json
{
  "luas_tanah": 150,
  "luas_bangunan": 100,
  "jumlah_kamar": 3,
  "jumlah_kamar_mandi": 2,
  "jarak_pusat_kota": 5.0
}
```

Contoh respons sukses:

```json
{
  "status": "success",
  "prediksi_harga": 872500000,
  "satuan": "IDR"
}
```

Kalau ada field yang kurang, hasilnya akan seperti ini:

```json
{
  "status": "error",
  "pesan": "Kolom berikut tidak ditemukan dalam input: ['jumlah_kamar', 'jumlah_kamar_mandi', 'jarak_pusat_kota']"
}
```

Kalau ada isi yang bukan angka, API juga akan menolak input tersebut.

## Field yang dipakai

|Field|Tipe|Keterangan|
|---|---|---|
|`luas_tanah`|float|Luas tanah dalam m²|
|`luas_bangunan`|float|Luas bangunan dalam m²|
|`jumlah_kamar`|int|Jumlah kamar tidur|
|`jumlah_kamar_mandi`|int|Jumlah kamar mandi|
|`jarak_pusat_kota`|float|Jarak ke pusat kota dalam km|

## Dokumentasi API

FastAPI sudah menyediakan Swagger UI bawaan. Buka:

`http://127.0.0.1:8000/docs`

Di sana kamu bisa coba endpoint langsung lewat browser.

`notebook_latihan.ipynb` hanya dipakai saat training model, bukan saat menjalankan API.
