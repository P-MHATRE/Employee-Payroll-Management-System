from db_config import get_connection
from tables import Table
class Payroll:

    @staticmethod
    def generate(emp_id, month):
        conn = get_connection()
        cur = conn.cursor()
        
        cur.execute("""
        SELECT e.basic_salary, a.total_days, a.present_days
        FROM employees e
        JOIN attendance a ON e.emp_id = a.emp_id
        WHERE e.emp_id=%s AND a.month=%s
        """, (emp_id, month))

        data = cur.fetchone()

        if not data:
            print("Attendance not found")
            return

        salary, total, present = data
        net_salary = (salary / total) * present

        cur.execute("""
        INSERT INTO payroll (emp_id, month, net_salary, generated_date)
        VALUES (%s, %s, %s, CURDATE())
        """, (emp_id, month, net_salary))

        conn.commit()
        cur.close()
        conn.close()

        print(f"Salary Generated: ₹{net_salary:.2f}")
