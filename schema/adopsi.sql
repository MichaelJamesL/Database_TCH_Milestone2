CREATE TABLE IF NOT EXISTS adopsi (
    id_user INT NOT NULL,
    id_hewan INT NOT NULL,
    waktu_adopsi DATETIME NOT NULL,
    waktu_kembali DATETIME NULL,
    id_pembayaran INT UNIQUE NOT NULL,
    
    PRIMARY KEY (id_user, id_hewan, waktu_adopsi),

    FOREIGN KEY (id_user) REFERENCES adopter(id_user) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_hewan) REFERENCES hewan(id_hewan) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_pembayaran) REFERENCES pembayaran(id_pembayaran) ON DELETE RESTRICT ON UPDATE CASCADE,

    CONSTRAINT check_waktu_adopsi CHECK (waktu_kembali IS NULL OR waktu_kembali >= waktu_adopsi)
);