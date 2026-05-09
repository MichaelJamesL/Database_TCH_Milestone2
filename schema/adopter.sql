CREATE TABLE IF NOT EXISTS adopter (
    id_user INT PRIMARY KEY, 
    preferensi VARCHAR(100), 
    FOREIGN KEY (id_user) REFERENCES pengguna(id_user) ON DELETE CASCADE
);