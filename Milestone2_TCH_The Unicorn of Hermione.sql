-- CATATAN: Implementasi ini melibatkan seluruh lebih dari satu file .sql agar modular,
--          cukup jalankan file .sql ini dan pastikan direktori schema/ dan seed/ tidak diubah

DROP DATABASE IF EXISTS petcare;
CREATE DATABASE petcare;
USE petcare;

-- Schema
SOURCE ./schema/pengguna.sql;
SOURCE ./schema/hewan.sql;
SOURCE ./schema/shelter.sql;
SOURCE ./schema/staff.sql;
SOURCE ./schema/adopter.sql;
SOURCE ./schema/pembayaran.sql;
SOURCE ./schema/adopsi.sql;
SOURCE ./schema/medis.sql;

-- Seed data
SOURCE ./seed/pengguna_seed.sql;
SOURCE ./seed/shelter_seed.sql;
SOURCE ./seed/hewan_seed.sql;
SOURCE ./seed/adopter_seed.sql;
SOURCE ./seed/staff_seed.sql;
SOURCE ./seed/pembayaran_seed.sql;
SOURCE ./seed/adopsi_seed.sql;
SOURCE ./seed/medis_seed.sql;
