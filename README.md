# Employee-Payroll-Management-System
this is a employee payroll management system  created using python annd mysql 
# Employee Payroll Management System

## 📌 Overview

Employee Payroll Management System is a console-based application developed using Python and MySQL. The system helps manage employee records, attendance, and payroll generation through a simple menu-driven interface.

This project demonstrates the use of Object-Oriented Programming (OOP), MySQL database operations, and modular Python programming.

---

## 🚀 Features

- Add Employee
- Update Employee Salary
- Delete Employee
- Mark Employee Attendance
- Generate Payroll Based on Attendance
- View Employee Records
- MySQL Database Integration
- Menu-Driven Interface

---

## 🛠 Technologies Used

- Python
- MySQL
- mysql-connector-python
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```
Employee-Payroll-Management-System/
│
├── main.py
├── employee.py
├── attendance.py
├── payroll.py
├── record.py
├── tables.py
├── db_config.py
│
├── database.sql
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🗄 Database Tables

### Employees
Stores employee information.

| Column | Type |
|----------|----------|
| emp_id | INT (PK) |
| name | VARCHAR(100) |
| department | VARCHAR(50) |
| designation | VARCHAR(50) |
| basic_salary | DECIMAL(10,2) |
| joining_date | DATE |

### Attendance
Stores employee attendance records.

| Column | Type |
|----------|----------|
| attendance_id | INT (PK) |
| emp_id | INT (FK) |
| month | VARCHAR(7) |
| total_days | INT |
| present_days | INT |

### Payroll
Stores generated salary details.

| Column | Type |
|----------|----------|
| payroll_id | INT (PK) |
| emp_id | INT (FK) |
| month | VARCHAR(7) |
| net_salary | DECIMAL(10,2) |
| generated_date | DATE |

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Employee-Payroll-Management-System.git
```

### 2. Install Required Package

```bash
pip install -r requirements.txt
```

### 3. Create Database

Import the provided `database.sql` file into MySQL.

```sql
CREATE DATABASE emp_payroll;
USE emp_payroll;
```

### 4. Configure Database Connection

Update database credentials in `db_config.py`.

```python
host="localhost"
user="root"
password="YOUR_PASSWORD"
database="emp_payroll"
```

### 5. Run Application

```bash
python main.py
```

---

## 📋 Main Menu

```
1. Add Employee
2. Update Salary
3. Delete Employee
4. Mark Attendance
5. Generate Payroll
6. Show Employees
7. Exit
```

---

## 💰 Payroll Calculation

Salary is calculated based on attendance:

```
Net Salary = (Basic Salary / Total Working Days) × Present Days
```

---

## 📚 Concepts Used

- Classes and Objects
- Constructors
- Static Methods
- Database Connectivity
- CRUD Operations
- Foreign Key Relationships
- Modular Programming
- Business Logic Implementation

---

## 🎯 Learning Outcome

Through this project I learned:

- Python OOP Concepts
- MySQL Database Design
- SQL Queries
- CRUD Operations
- Python-MySQL Integration
- Project Structure and Code Organization

---

## 👨‍💻 Author

**Pranay Mhatre**

BCA Graduate | Python Backend Developer

Skills:
- Python
- SQL
- MySQL
- OOP
- Problem Solving

---

## ⭐ Future Enhancements

- GUI using Tkinter
- Flask Web Application
- REST API Development
- User Authentication
- Report Generation
- Dashboard & Analytics
