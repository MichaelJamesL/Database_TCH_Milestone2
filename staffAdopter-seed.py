import random

from faker import Faker

fake = Faker("id_ID")

OUTPUT_FILE = "staffAdopter.sql"

def esc(s: str) -> str:
    return s.replace("'", "''").replace("\n", " ").strip()

def seed_adopter(f, adopter_ids):
    preferensi_list = [
        "Kucing",
        "Anjing besar",
        "Anjing kecil",
        "Reptil",
        "Unggas",
        "Hewan ras",
        "Hewan eksotis",
        "Hewan tidak berbulu"
    ]

    for id_user in sorted(adopter_ids):
        if random.random() < 0.2:
            preferensi = "NULL"
        else:
            preferensi = f"'{esc(random.choice(preferensi_list))}'"

        f.write(
            f"INSERT INTO adopter (id_user, preferensi) "
            f"VALUES ({id_user}, {preferensi});\n"
        )

def seed_staff(f, staff_ids, jumlah_shelter):
     for id_user in sorted(staff_ids):
        id_shelter = random.randint(1, jumlah_shelter)
        id_pegawai = 1000 + id_user  

        f.write(
            f"INSERT INTO staff "
            f"(id_user, id_pegawai, id_shelter) "
            f"VALUES ({id_user}, {id_pegawai}, {id_shelter});\n"
        )


if __name__ == "__main__":
    N_SHELTER = 30
    N_PENGGUNA = 3000
    N_STAFF = N_SHELTER * 50

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        all_user_ids = list(range(1, N_PENGGUNA + 1))
        staff_ids = set(random.sample(all_user_ids, N_STAFF))
        adopter_ids = set(all_user_ids) - staff_ids

        f.write("-- staff\n")
        seed_staff(f, staff_ids, N_SHELTER)
        f.write("-- adopter\n")
        seed_adopter(f, adopter_ids)


    print(f"SQL Seed File: {OUTPUT_FILE}")