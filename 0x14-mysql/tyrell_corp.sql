-- Create the database tyrell_corp
CREATE DATABASE tyrell_corp;

-- Switch to the tyrell_corp database
USE tyrell_corp;

-- Create the table nexus6 with a column "name" of type VARCHAR(50)
CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

-- Insert an entry with name "Leo" into the nexus6 table
INSERT INTO nexus6 (name) VALUES ('Leo');

-- Grant SELECT permission on the nexus6 table to holberton_user
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
