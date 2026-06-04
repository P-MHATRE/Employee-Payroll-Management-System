from db_config import get_connection
from tables import Table
class Attendance:

    def __init__(self, emp_id, month, total_days, present_days):
        self.emp_id = emp_id
        self.month = month
        self.total_days = total_days
        self.present_days = present_days

    def mark(self):
        conn = get_connection()
        cur = conn.cursor()
        
        cur.execute("""
        INSERT INTO attendance (emp_id, month, total_days, present_days)
        VALUES (%s, %s, %s, %s)
        """, (self.emp_id, self.month, self.total_days, self.present_days))

        conn.commit()
        cur.close()
        conn.close()
        print("Attendance marked")