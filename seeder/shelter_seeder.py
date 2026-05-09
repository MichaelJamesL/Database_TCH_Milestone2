import random

from faker import Faker

fake = Faker("id_ID")

OUTPUT_FILE = "seed/shelter_seed.sql"

def esc(s: str) -> str:
    return s.replace("'", "''").replace("\n", " ").strip()

def seed_shelter(f, jumlah: int):
    prefix = [
        "Shelter",
        "Rumah Singgah",
        "Pusat Adopsi",
        "Yayasan",
        "Animal Rescue"
    ]

    nama_hewan = [
        "Kucing",
        "Anjing",
        "Satwa",
        "Paws",
        "Meong",
        "Pawtopia",
        "PetCare",
        "Animalia"
    ]

    suffix = [
        "Harapan",
        "Bahagia",
        "Nusantara",
        "Sejahtera",
        "Bandung",
        "Indonesia",
        "Care",
        "Rescue"
    ]
    for _ in range(jumlah):
        nama = nama = esc(
            f"{random.choice(prefix)} "
            f"{random.choice(nama_hewan)} "
            f"{random.choice(suffix)}"
        )
        kota = esc(fake.city())
        negara = "Indonesia"
        f.write(f"INSERT INTO shelter (nama, kota, negara) VALUES ('{nama}', '{kota}', '{negara}');\n")


if __name__ == "__main__":
    N_SHELTER = 30

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("-- shelter\n")
        seed_shelter(f, N_SHELTER)

    print(f"SQL Seed File: {OUTPUT_FILE}")