-- MySQL setup development
-- database => hbnb_test_db
-- user_name => hbnb_test in localhost
-- password => hbnb_test_pwd
-- hbnb_test has all privileges on hbnb_test_db
-- hbnb_test => selects privilege on db performance_schema
-- if db or user already exists, script shouldn't fail

-- db creation if non-existant
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- user creation if non-existant
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- privileges to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- privileges selection on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- delete privileges
FLUSH PRIVILEGES;
