from pydantic import BaseModel
from fastapi import FastAPI

try:
    from .predictor import predict
except ImportError:
    from predictor import predict

app = FastAPI(
    title="API Prediksi Harga Rumah",
    description="Web service untuk memprediksi harga rumah berdasarkan fitur properti.",
    version="1.0.0"
)

class RumahInput(BaseModel):
    luas_tanah: float
    luas_bangunan: float
    jumlah_kamar: int
    jumlah_kamar_mandi: int
    jarak_pusat_kota: float


@app.get("/")
def root():
    return {"pesan": "API Prediksi Harga Rumah aktif. Gunakan endpoint POST /predict."}


@app.post("/predict")
def predict_harga(data: RumahInput):
    input_dict = data.dict()
    hasil = predict(input_dict)
    return hasil