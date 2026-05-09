CREATE TABLE catatan_medis (
    no_catatan INT AUTO_INCREMENT PRIMARY KEY,
    waktu_pembuatan DATETIME DEFAULT CURRENT_TIMESTAMP,
    ringkasan_kondisi TEXT
)

CREATE TABLE tindakan_perawatan (
    waktu DATETIME PRIMARY KEY,
    deskripsi TEXT,
    biaya DECIMAL(11, 2) NOT NULL,
    no_catatan INT,
    id_dokter INT,
    FOREIGN KEY (no_catatan) REFERENCES catatan_medis(no_catatan) ON DELETE CASCADE,
    FOREIGN KEY (id_dokter) REFERENCES dokter_hewan(id_dokter)
)

CREATE TABLE dokter_hewan (
    id_dokter INT AUTO_INCREMENT PRIMARY KEY,
    tempat_praktik VARCHAR(100) NOT NULL,
    nama VARCHAR(100) NOT NULL
)
