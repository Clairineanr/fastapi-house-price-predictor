import joblib
import pandas as pd
from pathlib import Path

# Kolom yang dibutuhkan model
REQUIRED_COLUMNS = [
    'luas_tanah',
    'luas_bangunan',
    'jumlah_kamar',
    'jumlah_kamar_mandi',
    'jarak_pusat_kota'
]

# Dapatkan direktori tempat file ini berada
SCRIPT_DIR = Path(__file__).parent

def load_model(model_path: str = None):
    if model_path is None:
        model_path = SCRIPT_DIR / 'model_harga_rumah.pkl'
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        raise FileNotFoundError(f"File model tidak ditemukan: {model_path}")
    except Exception as e:
        raise RuntimeError(f"Gagal memuat model: {str(e)}")


def load_scaler(scaler_path: str = None):
    if scaler_path is None:
        scaler_path = SCRIPT_DIR / 'scaler_harga_rumah.pkl'
    try:
        scaler = joblib.load(scaler_path)
        return scaler
    except FileNotFoundError:
        raise FileNotFoundError(f"File scaler tidak ditemukan: {scaler_path}")
    except Exception as e:
        raise RuntimeError(f"Gagal memuat scaler: {str(e)}")

# Load sekali saat server dijalankan
MODEL = load_model()
SCALER = load_scaler()

def preprocess(data: dict) -> pd.DataFrame:
    # Cek apakah semua kolom ada
    missing = [col for col in REQUIRED_COLUMNS if col not in data]
    if missing:
        raise ValueError(f"Kolom berikut tidak ditemukan dalam input: {missing}")

    # Cek apakah semua nilai bertipe numerik
    for col in REQUIRED_COLUMNS:
        try:
            float(data[col])
        except (ValueError, TypeError):
            raise TypeError(f"Nilai '{col}' harus berupa angka, bukan '{data[col]}'")

    df = pd.DataFrame([{col: float(data[col]) for col in REQUIRED_COLUMNS}])
    return df


def predict(data: dict) -> dict:
    try:
        # Preprocessing
        df = preprocess(data)

        # Scaling & prediksi
        df_scaled = SCALER.transform(df)
        hasil = MODEL.predict(df_scaled)

        return {
            "status": "success",
            "prediksi_harga": int(hasil[0]),
            "satuan": "IDR"
        }

    except (ValueError, TypeError) as e:
        return {
            "status": "error",
            "pesan": str(e)
        }

    except Exception as e:
        return {
            "status": "error",
            "pesan": f"Terjadi kesalahan pada server: {str(e)}"
        }