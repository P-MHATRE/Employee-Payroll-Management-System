from db_config import get_connection


class Record:
    def show():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT emp_id, name, department , designation , basic_salary , joining_date FROM employees")

        # Fetch column names dynamically
        columns = [col[0] for col in cur.description]

        # Fetch all rows
        rows = cur.fetchall()

        # Column widths (adjustable)
        widths = [7, 12, 13, 14, 13, 13]

        # Print header
        header = "".join(f"{columns[i]:<{widths[i]}}" for i in range(len(columns)))
        print(header)
        print("-" * sum(widths))

        # Print rows
        for row in rows:
            print("".join(f"{str(row[i]):<{widths[i]}}" for i in range(len(row))))

        cur.close()
        conn.close()