-- Creating table with forieign key constraint

-- cREATING Database
CREATE DAtABASE IF NOT EXISTS hbtn_0d_usa;

-- switching to db
USE hbtn_0d_usa

-- creating table
CREATE TABLE IF NOT EXISTS cities
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id)
    REFERENCES states(id)
);