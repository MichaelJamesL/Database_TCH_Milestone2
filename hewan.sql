CREATE TABLE hewan (
    id_hewan INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    tanggal_lahir DATE NOT NULL,
    jenis_kelamin ENUM('Jantan', 'Betina') NOT NULL,
    ketersediaan ENUM('tersedia', 'diadopsi', 'perawatan') NOT NULL DEFAULT 'tersedia',
    id_shelter INT NOT NULL,
    no_catatan INT NOT NULL UNIQUE
);

CREATE TABLE anjing (
    id_hewan INT PRIMARY KEY,
    ras VARCHAR(100) NOT NULL
);

CREATE TABLE kucing (
    id_hewan INT PRIMARY KEY,
    tipe_tinggal VARCHAR(50) NOT NULL
);

CREATE TABLE hewan_eksotis (
    id_hewan INT PRIMARY KEY,
    jenis VARCHAR(100) NOT NULL
);
