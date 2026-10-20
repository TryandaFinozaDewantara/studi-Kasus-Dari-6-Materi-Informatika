from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard Penjualan", layout="wide")
st.title("Dashboard Analisis Penjualan")
st.caption("Demo interaktif — data sintetis untuk pembelajaran")

df = pd.read_csv(Path(__file__).resolve().parent.parent / "01_data_analytics" / "sales.csv")
df["laba"] = df["pendapatan"] - df["biaya_operasional"]

pilihan = st.multiselect("Pilih bulan yang ingin ditampilkan", df["bulan"].tolist(),
                         default=df["bulan"].tolist())
filtered = df[df["bulan"].isin(pilihan)]

if filtered.empty:
    st.info("Pilih setidaknya satu bulan untuk menampilkan analisis.")
else:
    c1, c2, c3 = st.columns(3)
    c1.metric("Total pendapatan", f"Rp{filtered['pendapatan'].sum():,.0f}")
    c2.metric("Total biaya", f"Rp{filtered['biaya_operasional'].sum():,.0f}")
    c3.metric("Total laba", f"Rp{filtered['laba'].sum():,.0f}")

    left, right = st.columns(2)
    with left:
        st.subheader("Tren pendapatan")
        fig1 = px.line(filtered, x="bulan", y="pendapatan", markers=True,
                       labels={"bulan": "Bulan", "pendapatan": "Pendapatan (Rp)"})
        st.plotly_chart(fig1, use_container_width=True)
    with right:
        st.subheader("Biaya dan laba")
        long_df = filtered.melt(id_vars="bulan",
                                value_vars=["biaya_operasional", "laba"],
                                var_name="kategori", value_name="rupiah")
        fig2 = px.bar(long_df, x="bulan", y="rupiah", color="kategori", barmode="group",
                      labels={"bulan": "Bulan", "rupiah": "Nilai (Rp)", "kategori": "Kategori"})
        st.plotly_chart(fig2, use_container_width=True)

    with st.expander("Lihat data tabel"):
        st.dataframe(filtered, use_container_width=True)
