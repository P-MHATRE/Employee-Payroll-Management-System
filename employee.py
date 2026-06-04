from db_config import get_connection
from tables import Table

class Employee:

    def __init__(self, name, department, designation, basic_salary, emp_id=None):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.basic_salary = basic_salary

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
    
        cur.execute("""
        INSERT INTO employees
        (name, department, designation, basic_salary, joining_date)
        VALUES (%s, %s, %s, %s, CURDATE())
        """, (self.name, self.department, self.designation, self.basic_salary))

        conn.commit()
        cur.close()
        conn.close()
        print("Employee added")

    @staticmethod
    def update_salary(emp_id, new_salary):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "UPDATE employees SET basic_salary=%s WHERE emp_id=%s",
            (new_salary, emp_id)
        )

        conn.commit()
        cur.close()
        conn.close()
        print("Salary updated")

    @staticmethod
    def delete(emp_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM attendance WHERE emp_id=%s", (emp_id,))
        cur.execute("DELETE FROM payroll WHERE emp_id=%s", (emp_id,))
        cur.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
        conn.commit()

        cur.close()     
        conn.close()
        print("Employee deleted")