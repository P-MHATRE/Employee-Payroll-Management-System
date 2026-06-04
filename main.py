from employee import Employee
from attendance import Attendance
from payroll import Payroll
from record import Record
while True:
    print("""
1. Add Employee
2. Update Salary
3. Delete Employee
4. Mark Attendance
5. Generate Payroll
6. Show Employees
7. Exit
""")

    ch = input("Choose option: ")

    if ch == "1":
        emp = Employee(
            input("Name: "),
            input("Department: "),
            input("Designation: "),
            float(input("Basic Salary: "))
        )
        emp.save()

    elif ch == "2":
        Employee.update_salary(
            int(input("Emp ID: ")),
            float(input("New Salary: "))
        )

    elif ch == "3":
        Employee.delete(int(input("Emp ID: ")))

    elif ch == "4":
        att = Attendance(
            int(input("Emp ID: ")),
            input("Month (YYYY-MM): "),
            int(input("Total Days: ")),
            int(input("Present Days: "))
        )
        att.mark()

    elif ch == "5":
        Payroll.generate(
            int(input("Emp ID: ")),
            input("Month (YYYY-MM): ")
        )

    elif ch == "6":
        Record.show()

    elif ch == "7":
        print('System closed sucessfully')
        break

    else:
        print("Invalid choice")