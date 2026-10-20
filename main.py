from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv(Path(__file__).with_name("payments.csv"))
X = df[["tagihan_ribu", "hari_menuju_jatuh_tempo", "riwayat_telat"]]
y = df["terlambat"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Akurasi contoh:", round(accuracy_score(y_test, pred), 3))
print("\nConfusion matrix:\n", confusion_matrix(y_test, pred))
print("\nLaporan klasifikasi:\n", classification_report(y_test, pred, zero_division=0))

contoh_baru = pd.DataFrame([{
    "tagihan_ribu": 650,
    "hari_menuju_jatuh_tempo": 2,
    "riwayat_telat": 2
}])
prediksi = int(model.predict(contoh_baru)[0])
print("Contoh prediksi:", "berpotensi terlambat" if prediksi else "tidak terindikasi terlambat")
print("Jangan gunakan data sintetis ini untuk keputusan keuangan nyata.")
