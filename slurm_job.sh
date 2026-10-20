#!/bin/bash
#SBATCH --job-name=contoh_sensor
#SBATCH --output=hasil_%j.out
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=2G

# Contoh untuk klaster yang menggunakan SLURM.
# Sesuaikan modul/lingkungan Python dengan panduan administrator klaster.
python main.py
