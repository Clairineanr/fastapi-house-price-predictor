import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "aktif" in response.json().get("pesan", "")

def test_predict_endpoint():
    payload = {
        "luas_tanah": 150.0,
        "luas_bangunan": 100.0,
        "jumlah_kamar": 3,
        "jumlah_kamar_mandi": 2,
        "jarak_pusat_kota": 5.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "success"
    assert "prediksi_harga" in data
    assert data["prediksi_harga"] > 0
