CREATE TABLE pembayaran (
    id_pembayaran INT NOT NULL,
    amount DECIMAL(12, 3) NOT NULL,
    metode VARCHAR(50) NOT NULL,
    waktu DATETIME NOT NULL,
    
    PRIMARY KEY (id_pembayaran)
);