-- Connect as the MySQL root user or a user with administrative privileges.

-- Create the user 'holberton_user' with the host set to localhost and the specified password.
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- Grant the required permissions to check the primary/replica status.
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

-- Flush the privileges to apply the changes immediately.
FLUSH PRIVILEGES;
