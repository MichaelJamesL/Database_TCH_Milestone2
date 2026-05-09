import subprocess
import sys
import os

seeders = [
    'adopsi_payment_seeder.py',
    'hewan_seeder.py',
    'medis_seeder.py',
    'pengguna_seeder.py',
    'shelter_seeder.py',
    'staff_adopter_seeder.py'
]


def run_seeders():
    for seeder in seeders:
        try:
            subprocess.run([sys.executable, './seeder/' + seeder], check=True)
            print(f"Berhasil melakukan seeding menggunakan '{seeder}'\n")

        except subprocess.CalledProcessError as e:
            print(f"Gagal melakukan seeding menggunakan '{seeder}': {e} \n")
            break


if __name__ == "__main__":
    os.makedirs("seed", exist_ok=True)
    run_seeders()