from db_config import get_connection

conn = get_connection()
cur = conn.cursor()
class Table:
    def addemp():
        cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
        emp_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        department VARCHAR(50),
        designation VARCHAR(50),
        basic_salary DECIMAL(10,2),
        joining_date DATE)
        """)
        print("Employees table created")

    def attendance():
        cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
        attendance_id INT AUTO_INCREMENT PRIMARY KEY,
        emp_id INT,
        month VARCHAR(7),
        total_days INT,
        present_days INT,
        FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        )
        """)
        print("Attendance table created")

    def payroll():
        cur.execute("""
        CREATE TABLE IF NOT EXISTS payroll (
        payroll_id INT AUTO_INCREMENT PRIMARY KEY,
        emp_id INT,
        month VARCHAR(7),
        net_salary DECIMAL(10,2),
        generated_date DATE,
        FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        )
        """)
        print("Payroll table created")

    conn.commit()
    cur.close()
    conn.close()
    print("All tables created successfully")


