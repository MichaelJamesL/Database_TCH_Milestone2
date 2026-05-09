import random
from datetime import date, timedelta

OUTPUT_FILE = "hewan-seed.sql"

random.seed(24)

nama_hewan = [
    "Milo",
    "Luna",
    "Mochi",
    "Bimo",
    "Kopi",
    "Nala",
    "Oreo",
    "Coco",
    "Bola",
    "Ruby",
    "Kiko",
    "Momo",
    "Toby",
    "Bella",
    "Leo",
    "Mika",
    "Chiko",
    "Daisy",
    "Rocky",
    "Niko",
]

ras_anjing = [
    "Golden Retriever",
    "Labrador Retriever",
    "Beagle",
    "Pomeranian",
    "Shih Tzu",
    "Siberian Husky",
    "German Shepherd",
    "Dachshund",
    "Poodle",
    "Mixed Breed",
]

tipe_tinggal_kucing = [
    "indoor",
    "outdoor",
    "indoor-outdoor",
]

jenis_eksotis = [
    "Iguana",
    "Kura-kura",
    "Sugar Glider",
    "Hamster",
    "Landak Mini",
    "Kelinci",
    "Burung Parkit",
    "Gecko",
    "Ular Jagung",
    "Chinchilla",
]

jenis_kelamin = ["Jantan", "Betina"]
ketersediaan = ["tersedia", "diadopsi", "perawatan"]


def esc(value):
    return value.replace("'", "''")


def tanggal_lahir():
    awal = date(2017, 1, 1)
    akhir = date(2026, 4, 30)
    return awal + timedelta(days=random.randint(0, (akhir - awal).days))


def tulis_hewan(f, id_hewan):
    nama = esc(f"{random.choice(nama_hewan)} {id_hewan:03d}")
    lahir = tanggal_lahir()
    kelamin = random.choice(jenis_kelamin)
    status = random.choice(ketersediaan)
    id_shelter = random.randint(1, 20)
    f.write(
        "INSERT INTO hewan (id_hewan, nama, tanggal_lahir, jenis_kelamin, ketersediaan, id_shelter, no_catatan) "
        f"VALUES ({id_hewan}, '{nama}', '{lahir}', '{kelamin}', '{status}', {id_shelter}, {id_hewan});\n"
    )


with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for id_hewan in range(1, 151):
        tulis_hewan(f, id_hewan)

    for id_hewan in range(1, 51):
        ras = esc(random.choice(ras_anjing))
        f.write(f"INSERT INTO anjing (id_hewan, ras) VALUES ({id_hewan}, '{ras}');\n")

    for id_hewan in range(51, 101):
        tipe_tinggal = esc(random.choice(tipe_tinggal_kucing))
        f.write(f"INSERT INTO kucing (id_hewan, tipe_tinggal) VALUES ({id_hewan}, '{tipe_tinggal}');\n")

    for id_hewan in range(101, 151):
        jenis = esc(random.choice(jenis_eksotis))
        f.write(f"INSERT INTO hewan_eksotis (id_hewan, jenis) VALUES ({id_hewan}, '{jenis}');\n")
