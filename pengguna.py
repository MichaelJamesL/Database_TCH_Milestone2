from faker import Faker
import random

fake = Faker('id_ID')

kota_provinsi = {
    'Banda Aceh': 'Aceh',
    'Langsa': 'Aceh',
    'Lhokseumawe': 'Aceh',
    'Sabang': 'Aceh',
    'Subulussalam': 'Aceh',
    'Medan': 'Sumatera Utara',
    'Binjai': 'Sumatera Utara',
    'Padang': 'Sumatera Barat',
    'Bukittinggi': 'Sumatera Barat',
    'Pekanbaru': 'Riau',
    'Dumai': 'Riau',
    'Tanjungpinang': 'Kepulauan Riau',
    'Batam': 'Kepulauan Riau',
    'Jambi': 'Jambi',
    'Sungai Penuh': 'Jambi',
    'Palembang': 'Sumatera Selatan',
    'Pangkalpinang': 'Kepulauan Bangka Belitung',
    'Bengkulu': 'Bengkulu',
    'Bandar Lampung': 'Lampung',
    'Metro': 'Lampung',
    'Jakarta': 'DKI Jakarta',
    'Bandung': 'Jawa Barat',
    'Bekasi': 'Jawa Barat',
    'Bogor': 'Jawa Barat',
    'Cimahi': 'Jawa Barat',
    'Cirebon': 'Jawa Barat',
    'Depok': 'Jawa Barat',
    'Sukabumi': 'Jawa Barat',
    'Tasikmalaya': 'Jawa Barat',
    'Serang': 'Banten',
    'Tangerang': 'Banten',
    'Semarang': 'Jawa Tengah',
    'Magelang': 'Jawa Tengah',
    'Pekalongan': 'Jawa Tengah',
    'Purwokerto': 'Jawa Tengah',
    'Salatiga': 'Jawa Tengah',
    'Solo': 'Jawa Tengah',
    'Tegal': 'Jawa Tengah',
    'Yogyakarta': 'DI Yogyakarta',
    'Surabaya': 'Jawa Timur',
    'Batu': 'Jawa Timur',
    'Blitar': 'Jawa Timur',
    'Kediri': 'Jawa Timur',
    'Madiun': 'Jawa Timur',
    'Malang': 'Jawa Timur',
    'Mojokerto': 'Jawa Timur',
    'Denpasar': 'Bali',
    'Mataram': 'Nusa Tenggara Barat',
    'Kupang': 'Nusa Tenggara Timur',
    'Pontianak': 'Kalimantan Barat',
    'Singkawang': 'Kalimantan Barat',
    'Palangkaraya': 'Kalimantan Tengah',
    'Banjarmasin': 'Kalimantan Selatan',
    'Samarinda': 'Kalimantan Timur',
    'Balikpapan': 'Kalimantan Timur',
    'Bontang': 'Kalimantan Timur',
    'Tanjung Selor': 'Kalimantan Utara',
    'Tarakan': 'Kalimantan Utara',
    'Manado': 'Sulawesi Utara',
    'Bitung': 'Sulawesi Utara',
    'Palu': 'Sulawesi Tengah',
    'Makassar': 'Sulawesi Selatan',
    'Palopo': 'Sulawesi Selatan',
    'Parepare': 'Sulawesi Selatan',
    'Kendari': 'Sulawesi Tenggara',
    'Gorontalo': 'Gorontalo',
    'Mamuju': 'Sulawesi Barat',
    'Ambon': 'Maluku',
    'Sofifi': 'Maluku Utara',
    'Ternate': 'Maluku Utara',
    'Tidore': 'Maluku Utara',
    'Manokwari': 'Papua Barat',
    'Sorong': 'Papua Barat',
    'Jayapura': 'Papua',
}

kota_list = list(kota_provinsi.keys())

users = []
for i in range(200):
    kota = random.choice(kota_list)
    users.append({
        'nama': fake.name(),
        'email': fake.unique.email(),
        'jalan': fake.street_address(),
        'kota': kota,
        'provinsi': kota_provinsi[kota],
        'negara': 'Indonesia'
    })

telp_rows = []
for i, u in enumerate(users, start=1):  
    jumlah = random.randint(1, 3)
    nomor_used = set()
    for _ in range(jumlah):
        nomor = fake.phone_number()
        while nomor in nomor_used:
            nomor = fake.phone_number()
        nomor_used.add(nomor)
        telp_rows.append({
            'id_user': i,
            'nomor_telepon': nomor
        })

with open('pengguna.sql', 'w') as f:

    f.write("""CREATE TABLE IF NOT EXISTS pengguna (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    jalan VARCHAR(200) NOT NULL,
    kota VARCHAR(100) NOT NULL,
    provinsi VARCHAR(100) NOT NULL,
    negara VARCHAR(100) NOT NULL
);\n\n""")

    f.write("""CREATE TABLE IF NOT EXISTS pengguna_telp (
    id_user INT NOT NULL,
    nomor_telepon VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_user, nomor_telepon),
    FOREIGN KEY (id_user) REFERENCES pengguna(id_user)
);\n\n""")

    for u in users:
        nama = u['nama'].replace("'", "''")
        jalan = u['jalan'].replace("'", "''")
        kota = u['kota'].replace("'", "''")
        provinsi = u['provinsi'].replace("'", "''")
        f.write(
            f"INSERT INTO pengguna (nama, email, jalan, kota, provinsi, negara) VALUES ("
            f"'{nama}', '{u['email']}', '{jalan}', '{kota}', '{provinsi}', 'Indonesia');\n"
        )

    for t in telp_rows:
        nomor = t['nomor_telepon'].replace("'", "''")
        f.write(
            f"INSERT INTO pengguna_telp (id_user, nomor_telepon) VALUES "
            f"({t['id_user']}, '{nomor}');\n"
        )

print(f"Selesai: {len(users)} pengguna, {len(telp_rows)} nomor telepon")