# Study Kasus 2 — HPC untuk Tantangan Lokal

## Permasalahan
Data sensor curah hujan dan tinggi sungai dapat bertambah cepat ketika banyak sensor mengirimkan data. Sebagai latihan, kita menghitung indeks risiko sederhana untuk setiap catatan sensor secara paralel pada komputer lokal.

## Hubungan dengan HPC
Contoh ini memperagakan pembagian pekerjaan ke beberapa proses. Ini bukan akses ke superkomputer sungguhan. `slurm_job.sh` disertakan sebagai contoh format batch job SLURM yang bisa disesuaikan di klaster yang mendukung SLURM.

## Menjalankan
```bash
python main.py
```
