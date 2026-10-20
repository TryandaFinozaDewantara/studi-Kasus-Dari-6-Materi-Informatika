from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv(Path(__file__).with_name("deforestation_samples.csv"))
features = ["area_ha", "rasio_panjang_lebar", "jalan_km",
            "perubahan_vegetasi", "indikasi_panas"]
X, y = df[features], df["penyebab"]

# Dataset sengaja kecil untuk demo; hasil evaluasi tidak mewakili kinerja lapangan.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=7
)
model = RandomForestClassifier(n_estimators=100, random_state=7, class_weight="balanced")
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Akurasi demo:", round(accuracy_score(y_test, pred), 3))
print("\nLaporan klasifikasi:\n", classification_report(y_test, pred, zero_division=0))

alert_baru = pd.DataFrame([{
    "area_ha": 25,
    "rasio_panjang_lebar": 1.7,
    "jalan_km": 0.4,
    "perubahan_vegetasi": 0.85,
    "indikasi_panas": 0.15
}])
print("Perkiraan penyebab untuk alert contoh:", model.predict(alert_baru)[0])
print("\nPeringatan: ini hanya prediksi dari fitur sintetis, bukan bukti penyebab deforestasi.")
print("Perlu citra satelit, data berlabel berkualitas, dan validasi lapangan.")
