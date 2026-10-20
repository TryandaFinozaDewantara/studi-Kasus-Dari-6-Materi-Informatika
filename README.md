# Study Kasus 6 — Deforestation Alerts with Satellite Imagery and AI

## Permasalahan
Alert kehilangan tutupan pohon menunjukkan lokasi perubahan, tetapi tidak otomatis menjelaskan penyebab langsungnya. Materi menyebut kemungkinan penyebab seperti pertanian, pembangunan jalan, penebangan, pertambangan, dan kebakaran.

## Implementasi demonstrasi
Script melatih Random Forest pada fitur tabular sintetis (ukuran area, bentuk area, kedekatan jalan, perubahan vegetasi, dan gangguan panas) untuk memperkirakan kelas penyebab. Ini sengaja dibuat ringan agar bisa dijalankan tanpa citra satelit.

## Menjalankan
```bash
python main.py
```

## Keterbatasan
Script ini **bukan** model CNN citra Sentinel-1/Sentinel-2 dan tidak menggunakan data satelit nyata. Untuk penerapan sesungguhnya dibutuhkan citra yang sesuai, label terverifikasi, evaluasi spasial, validasi lapangan, serta penilaian kesalahan klasifikasi. Prediksi tidak boleh dipakai sendirian untuk menuduh pihak tertentu atau menetapkan penyebab resmi.
