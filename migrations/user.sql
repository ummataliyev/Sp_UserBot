-- Active: 1676276314698@@127.0.0.1@3306
/* create user informations table*/
CREATE TABLE IF NOT EXISTS user_info (
    user_id INT NOT NULL PRIMARY KEY,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NULL,
    username VARCHAR(32) NULL,
    is_premium BOOLEAN DEFAULT FALSE
);


/* Dropping tables */
DROP TABLE user_info;
