-- A script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- states description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail

-- CREATING DATABSE
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- SWITCHING TO THE DATABASE hbtn_0d_usa
USE hbtn_0d_usa;

-- Creating the tavle states
CREATE TABLE IF NOT EXISTS states
(
    id INT NOT NULL UNIQUE AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id)
);
