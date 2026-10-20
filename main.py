from pathlib import Path
import pandas as pd

DATA = Path(__file__).with_name("sales.csv")
df = pd.read_csv(DATA)
df["laba"] = df["pendapatan"] - df["biaya_operasional"]
df["saldo_piutang_bersih_bulan"] = df["piutang_baru"] - df["pembayaran_piutang"]

print("=== Ringkasan Analisis Penjualan ===")
print(df.to_string(index=False))
print("\nTotal pendapatan :", f"Rp{df['pendapatan'].sum():,.0f}")
print("Total biaya      :", f"Rp{df['biaya_operasional'].sum():,.0f}")
print("Total laba       :", f"Rp{df['laba'].sum():,.0f}")
print("Akumulasi saldo piutang bersih bulanan:",
      f"Rp{df['saldo_piutang_bersih_bulan'].sum():,.0f}")

awal, akhir = df.iloc[0], df.iloc[-1]
print("\nInsight:")
print(f"- Pendapatan berubah dari Rp{awal.pendapatan:,.0f} menjadi Rp{akhir.pendapatan:,.0f}.")
print(f"- Laba berubah dari Rp{awal.laba:,.0f} menjadi Rp{akhir.laba:,.0f}.")
if akhir.laba < awal.laba:
    print("- Laba turun walaupun pendapatan naik; evaluasi biaya operasional.")
else:
    print("- Laba tidak turun pada periode awal-akhir, tetapi biaya tetap perlu dipantau.")
if (df["saldo_piutang_bersih_bulan"] > 0).any():
    print("- Ada bulan ketika piutang baru lebih besar daripada pembayaran piutang.")
print("\nRekomendasi awal: periksa komponen biaya, umur piutang, dan pola pembayaran.")
print("Catatan: akumulasi saldo bulanan bukan saldo piutang aktual jika saldo awal tidak tersedia.")
