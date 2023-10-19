-- Script convert given database to UTF8
USE testDB2;
ALTER TABLE First_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
