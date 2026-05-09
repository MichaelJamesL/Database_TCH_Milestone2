import random

from faker import Faker

fake = Faker("id_ID")


def esc(s: str) -> str:
    return s.replace("'", "''").replace("\n", " ").strip()

def seed_staff(f, staff_ids, jumlah_shelter):
     for id_user in sorted(staff_ids):
        id_shelter = random.randint(1, jumlah_shelter)
        id_pegawai = 1000 + id_user  

        f.write(
            f"INSERT INTO staff "
            f"(id_user, id_pegawai, id_shelter) "
            f"VALUES ({id_user}, {id_pegawai}, {id_shelter});\n"
        )



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

        
if __name__ == "__main__":
    N_SHELTER = 10
    N_PENGGUNA = 200
    N_STAFF = N_SHELTER * 10

    staff_ids = list(range(1, N_PENGGUNA - N_STAFF + 1))
    adopter_ids = list(range(N_STAFF + 1, N_PENGGUNA + 1))

    with open("seed/staff_seed.sql", "w", encoding="utf-8") as f:
        f.write("-- staff\n")
        seed_staff(f, staff_ids, N_SHELTER)

    with open("seed/adopter_seed.sql", "w", encoding="utf-8") as f:
        f.write("-- adopter\n")
        seed_adopter(f, adopter_ids)

