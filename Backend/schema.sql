DROP DATABASE IF EXISTS snapwork_db;


CREATE DATABASE IF NOT EXISTS snapwork_db;

USE snapwork_db;


-- =====================
-- USER TABLE
-- =====================

CREATE TABLE user (

    id INT AUTO_INCREMENT PRIMARY KEY,

    email VARCHAR(100) UNIQUE,

    password VARCHAR(100),

    role VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- =====================
-- STUDENT TABLE
-- =====================

CREATE TABLE student (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    first_name VARCHAR(50),

    last_name VARCHAR(50),

    college VARCHAR(100),

    skill VARCHAR(100),

    country VARCHAR(50),

    FOREIGN KEY (user_id)
    REFERENCES user(id)
    ON DELETE CASCADE

);


-- =====================
-- CLIENT TABLE
-- =====================

CREATE TABLE client (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    first_name VARCHAR(50),

    last_name VARCHAR(50),

    country VARCHAR(50),

    password VARCHAR(100),

    FOREIGN KEY (user_id)
    REFERENCES user(id)
    ON DELETE CASCADE

);