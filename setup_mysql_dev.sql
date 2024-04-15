-- MySQL setup development
-- database => hbnb_dev_b
-- user_name => hbnb_dev in localhost
-- password => hbnb_dev_pwd
-- hbnb_dev has all privileges on hbnb_dev_db
-- hbnb_dev => selects privilege on db performance_schema
-- if db or user already exists, script shouldn't fail

-- db creation if non-existant
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- user creation if non-existant
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- privileges to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- privileges selection on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- delete privileges
FLUSH PRIVILEGES;
