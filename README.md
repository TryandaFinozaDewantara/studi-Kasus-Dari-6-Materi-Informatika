# Study Kasus 6 Materi Perkuliahan Informatika

Repository ini berisi enam study kasus yang dikembangkan dari rangkuman materi perkuliahan. Setiap folder mempunyai penjelasan masalah, tujuan, langkah menjalankan, implementasi kode, dan catatan keterbatasan.

## Daftar study kasus

1. **Make Sense of Data with Analytics and AI** — analisis penjualan, laba, biaya operasional, dan piutang.
2. **Bridging Global Infrastructure to Address Local Challenges in HPC** — simulasi pemrosesan data sensor banjir secara paralel dan contoh batch script HPC.
3. **Career and Competition in Industrial Era with GIS** — analisis lokasi pertanian sederhana berdasarkan data koordinat dan atribut wilayah.
4. **Introduction to Machine Learning** — klasifikasi risiko keterlambatan pembayaran menggunakan data contoh.
5. **Human-Computer Interaction & Data Visualization** — dashboard interaktif untuk mengeksplorasi data penjualan.
6. **Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI** — klasifikasi penyebab alert kehilangan tutupan pohon dari fitur contoh.

## Persyaratan

- Python 3.10 atau lebih baru
- pip

Instalasi paket:

```bash
pip install -r requirements.txt
```

Beberapa kasus hanya memakai pustaka standar Python, pandas, matplotlib, atau scikit-learn. Dashboard kasus 5 memakai Streamlit dan Plotly.

## Cara menjalankan

Jalankan terminal dari folder repository, lalu pilih folder studi kasus.

```bash
python 01_data_analytics/main.py
python 02_hpc_local_challenge/main.py
python 03_gis_agriculture/main.py
python 04_machine_learning/main.py
streamlit run 05_hci_data_visualization/app.py
python 06_deforestation_ai/main.py
```

Untuk menjalankan kasus 4 dan 6, pastikan dependensi pada `requirements.txt` sudah terpasang.

## Catatan penting

Data CSV yang disediakan merupakan **data sintetis/contoh untuk pembelajaran**, bukan data perusahaan, data geospasial resmi, atau citra satelit asli. Model pada kasus 6 adalah demonstrasi klasifikasi berbasis fitur tabular, bukan implementasi CNN pada citra Sentinel-1/Sentinel-2. Untuk penelitian nyata, gunakan data yang sah, label yang tervalidasi, dan pemeriksaan lapangan.

## Struktur repository

```text
Study_Kasus_6_Materi_Informatika/
├── README.md
├── requirements.txt
├── 01_data_analytics/
├── 02_hpc_local_challenge/
├── 03_gis_agriculture/
├── 04_machine_learning/
├── 05_hci_data_visualization/
└── 06_deforestation_ai/
```

## Lisensi dan etika

Materi ini dibuat untuk tugas pembelajaran. Cantumkan sumber data jika mengganti data contoh dengan data publik, lindungi data pribadi, dan jelaskan keterbatasan hasil analisis.
