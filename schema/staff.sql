CREATE TABLE IF NOT EXISTS  staff (
    id_user INT PRIMARY KEY,  
    id_pegawai INT UNIQUE NOT NULL,
    id_shelter INT NOT NULL,
    FOREIGN KEY (id_user) REFERENCES pengguna(id_user) ON DELETE CASCADE,
    FOREIGN KEY (id_shelter) REFERENCES shelter(id_shelter)
);