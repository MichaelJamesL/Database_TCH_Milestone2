CREATE DATABASE IF NOT EXISTS petcare;
USE petcare;

-- Schema
SOURCE pengguna.sql;
SOURCE medis.sql;
SOURCE adopsi.sql;
SOURCE pembayaran.sql;

-- Seed data
SOURCE medis-seed.sql;