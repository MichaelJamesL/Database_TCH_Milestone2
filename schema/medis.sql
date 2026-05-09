CREATE TABLE IF NOT EXISTS catatan_medis (
    no_catatan INT AUTO_INCREMENT PRIMARY KEY,
    waktu_pembuatan DATETIME DEFAULT CURRENT_TIMESTAMP,
    ringkasan_kondisi TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dokter_hewan (
    id_dokter INT AUTO_INCREMENT PRIMARY KEY,
    tempat_praktik VARCHAR(100) NOT NULL,
    nama VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS tindakan_perawatan (
    waktu DATETIME,
    deskripsi TEXT,
    biaya DECIMAL(11, 2) NOT NULL,
    no_catatan INT NOT NULL,
    id_dokter INT NOT NULL,
    FOREIGN KEY (no_catatan) REFERENCES catatan_medis(no_catatan) ON DELETE CASCADE,
    FOREIGN KEY (id_dokter) REFERENCES dokter_hewan(id_dokter),
    PRIMARY KEY (waktu, no_catatan)
);

