CREATE TABLE IF NOT EXISTS pengguna (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    jalan VARCHAR(200) NOT NULL,
    kota VARCHAR(100) NOT NULL,
    provinsi VARCHAR(100) NOT NULL,
    negara VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS pengguna_telp (
    id_user INT NOT NULL,
    nomor_telepon VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_user, nomor_telepon),
    FOREIGN KEY (id_user) REFERENCES pengguna(id_user)
);