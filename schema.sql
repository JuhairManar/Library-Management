CREATE DATABASE IF NOT EXISTS library;
USE library;

CREATE TABLE users (
    roll INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE books (
    title VARCHAR(100) PRIMARY KEY,
    quantity INT NOT NULL
);

CREATE TABLE borrow (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll INT,
    book_title VARCHAR(100),
    FOREIGN KEY (roll) REFERENCES users(roll),
    FOREIGN KEY (book_title) REFERENCES books(title)
);