import random

from faker import Faker

fake = Faker("id_ID")

OUTPUT_FILE = "medis-seed.sql"

def esc(s: str) -> str:
    return s.replace("'", "''").replace("\n", " ").strip()

def generate_medical_summary():
    kondisi_umum = ["Sehat", "Lemas", "Dehidrasi ringan", "Nafsu makan menurun", "Pasca-operasi"]
    gejala = ["batuk ringan", "jamur di area telinga", "luka pada kaki kanan", "suhu tubuh tinggi", "parasit kutu"]
    tindakan_saran = ["perlu observasi", "diberikan vitamin", "jadwal vaksin ulang", "diet khusus protein tinggi"]

    return (
        f"Kondisi {random.choice(kondisi_umum)}. "
        f"Ditemukan {random.choice(gejala)}. "
        f"Rekomendasi: {random.choice(tindakan_saran)}."
    )

def seed_dokter_hewan(f, jumlah: int):
    klinik = ["Klinik Hewan Sejahtera", "Pet Care Center", "Klinik Satwa Sehat", "Animal Wellness Clinic", "Klinik Hewan Bahagia"]
    for _ in range(jumlah):
        tempat_praktik = esc(random.choice(klinik) + " - " + fake.city())
        nama = esc("drh. " + fake.name())
        f.write(f"INSERT INTO dokter_hewan (tempat_praktik, nama) VALUES ('{tempat_praktik}', '{nama}');\n")

def seed_catatan_medis(f, jumlah: int):
    for _ in range(jumlah):
        waktu = fake.date_time_this_year()
        ringkasan = esc(generate_medical_summary())
        f.write(f"INSERT INTO catatan_medis (waktu_pembuatan, ringkasan_kondisi) VALUES ('{waktu}', '{ringkasan}');\n")

def seed_tindakan_perawatan(f, jumlah: int, jumlah_catatan: int, jumlah_dokter: int):
    deskripsi_list = [
        "Pemeriksaan fisik rutin",
        "Vaksinasi tahunan",
        "Pembersihan luka dan pemberian antibiotik",
        "Pemberian obat cacing",
        "Operasi minor pengangkatan kutil",
        "Grooming medis untuk infeksi jamur",
        "Pemasangan infus untuk dehidrasi",
    ]
    waktu_terpakai = set()
    while len(waktu_terpakai) < jumlah:
        waktu = fake.date_time_this_year()
        if waktu in waktu_terpakai:
            continue
        waktu_terpakai.add(waktu)
        deskripsi = esc(random.choice(deskripsi_list))
        biaya = random.randint(100000, 500000)
        no_catatan = random.randint(1, jumlah_catatan)
        id_dokter = random.randint(1, jumlah_dokter)
        f.write(
            f"INSERT INTO tindakan_perawatan (waktu, deskripsi, biaya, no_catatan, id_dokter) "
            f"VALUES ('{waktu}', '{deskripsi}', {biaya}, {no_catatan}, {id_dokter});\n"
        )

if __name__ == "__main__":
    N_DOKTER = 30
    N_TINDAKAN = 30
    N_CATATAN = (N_DOKTER + N_TINDAKAN) * 50

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("-- dokter_hewan\n")
        seed_dokter_hewan(f, N_DOKTER)
        f.write("\n-- catatan_medis\n")
        seed_catatan_medis(f, N_CATATAN)
        f.write("\n-- tindakan_perawatan\n")
        seed_tindakan_perawatan(f, N_TINDAKAN, N_CATATAN, N_DOKTER)

    print(f"SQL Seed File: {OUTPUT_FILE}")
