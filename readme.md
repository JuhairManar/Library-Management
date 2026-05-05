Library Management System (Python + MySQL)

A console-based Library Management System built using Python (OOP + Service Layer Architecture) and MySQL database integration.
The project demonstrates real-world backend design principles like separation of concerns, repositories, and service layers.

🚀 Features
👤 User Management
Register new users
Login authentication
Persistent user data using MySQL

📖 Book Management
View available books
Borrow books
Return books
Automatic quantity update in database

🔁 Borrow System
Tracks borrowed books per user
Tracks returned books
Prevents borrowing unavailable books
Waiting queue system (FIFO) for unavailable books

🎁 Donation System
Users can donate new books
Updates existing book quantity or adds new book

🗃 Database Integration
Fully connected with MySQL
Stores:
Users
Books
Borrow records
Returned records

Technologies Used
Python 3
MySQL
mysql-connector-python
OOP Principles
Repository Pattern
Service Layer Architecture

Database Setup

Run the following SQL in MySQL Workbench:

