import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('id_ID')

animal_availability = {i: datetime(2025, 1, 1) for i in range(1, 151)}
adopter_ids = list(range(101, 201))
animal_ids = list(range(1, 151))

pembayaran_queries = []
adopsi_queries = []


if __name__ == '__main__':
    for i in range(1, 151):
        id_hewan = random.choice(animal_ids)
        start_search = animal_availability[id_hewan]
        
        waktu_pembayaran = fake.date_time_between(start_date=start_search, end_date='+30d')
        waktu_adopsi = waktu_pembayaran + timedelta(minutes=random.randint(10, 120))
        
        is_returned = random.random() < 0.2
        if is_returned:
            waktu_kembali = waktu_adopsi + timedelta(days=random.randint(1, 30))
            animal_availability[id_hewan] = waktu_kembali + timedelta(days=random.randint(1, 5))
            waktu_kembali_val = f"'{waktu_kembali.strftime('%Y-%m-%d %H:%M:%S')}'"
        else:
            animal_availability[id_hewan] = datetime(2030, 1, 1)
            animal_ids.remove(id_hewan)
            waktu_kembali_val = "NULL"

        id_user = random.choice(adopter_ids)
        amount = round(random.uniform(100000, 5000000), 3)
        metode = random.choice(['Transfer Bank', 'E-Wallet', 'Kartu Kredit', 'Tunai'])
        
        pembayaran_queries.append(
            f"INSERT INTO pembayaran (id_pembayaran, amount, metode, waktu) VALUES "
            f"({i}, {amount:.3f}, '{metode}', '{waktu_pembayaran.strftime('%Y-%m-%d %H:%M:%S')}');"
        )
        
        adopsi_queries.append(
            f"INSERT INTO adopsi (id_user, id_hewan, waktu_adopsi, waktu_kembali, id_pembayaran) VALUES "
            f"({id_user}, {id_hewan}, '{waktu_adopsi.strftime('%Y-%m-%d %H:%M:%S')}', {waktu_kembali_val}, {i});"
        )

    with open('seed/adopsi_seed.sql', 'w') as f:
        for q in adopsi_queries:
            f.write(q + "\n")

    with open('seed/pembayaran_seed.sql', 'w') as f:
        for q in pembayaran_queries:
            f.write(q + "\n")
    
