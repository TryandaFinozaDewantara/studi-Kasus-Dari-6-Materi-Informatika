from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).with_name("lokasi_pertanian.csv"))

# Skor latihan: tanah sesuai (50%), curah hujan moderat (30%), lereng landai (20%).
df["skor_hujan"] = (1 - (df["curah_hujan_mm"] - 1800).abs() / 1800).clip(0, 1)
df["skor_lereng"] = (1 - df["kemiringan_derajat"] / 30).clip(0, 1)
df["skor_kesesuaian"] = (
    0.5 * df["tanah_sesuai"] +
    0.3 * df["skor_hujan"] +
    0.2 * df["skor_lereng"]
).round(3)
df = df.sort_values("skor_kesesuaian", ascending=False)

print("Kandidat lokasi pertanian (data sintetis)")
print(df[["lokasi", "latitude", "longitude", "curah_hujan_mm",
          "kemiringan_derajat", "skor_kesesuaian"]].to_string(index=False))
print("\nLokasi dengan skor tertinggi:", df.iloc[0]["lokasi"])
print("Gunakan hasil hanya sebagai latihan. Penilaian nyata perlu data tanah, topografi,")
print("iklim, status lahan, validasi lapangan, dan masukan ahli.")
