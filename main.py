from pathlib import Path
from multiprocessing import Pool, cpu_count
import pandas as pd

def hitung_risiko(record):
    # Skor ilustratif, bukan standar peringatan resmi.
    hujan = float(record["curah_hujan_mm"])
    tinggi = float(record["tinggi_sungai_m"])
    skor = 0.4 * min(hujan / 150, 1) + 0.6 * min(tinggi / 5, 1)
    level = "TINGGI" if skor >= 0.65 else "SEDANG" if skor >= 0.4 else "RENDAH"
    return {"sensor": record["sensor"], "skor_risiko": round(skor, 3), "level": level}

if __name__ == "__main__":
    data = pd.read_csv(Path(__file__).with_name("sensor_data.csv"))
    records = data.to_dict(orient="records")
    jumlah_proses = min(4, cpu_count(), len(records))
    with Pool(processes=jumlah_proses) as pool:
        hasil = pool.map(hitung_risiko, records)
    output = pd.DataFrame(hasil)
    print("Pemrosesan sensor dengan multiprocessing")
    print(f"Jumlah catatan: {len(records)} | proses digunakan: {jumlah_proses}")
    print(output.to_string(index=False))
    print("\nCatatan: skor hanya demonstrasi. Ambang resmi harus ditentukan oleh ahli dan data lokal.")
