-- Creates a table user, add country enumeration

CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(256) NOT NULL UNIQUE,
	name VARCHAR(256),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
