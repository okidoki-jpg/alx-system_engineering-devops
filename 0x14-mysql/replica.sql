-- Connect as the MySQL root user or a user with administrative privileges.

-- Create the user 'replica_user' with the host set to '%' and a password of your choice.
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'okidoki';

-- Grant the appropriate replication privileges to replica_user.
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Grant SELECT privilege on the mysql.user table to holberton_user.
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

-- Flush the privileges to apply the changes immediately.
FLUSH PRIVILEGES;

