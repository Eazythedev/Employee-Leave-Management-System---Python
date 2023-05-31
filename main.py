class Employee:
    def __init__(self, emp_id, name, leave_balance):
        self.emp_id = emp_id
        self.name = name
        self.leave_balance = leave_balance


employees = {}


def add_employee(emp_id, name, leave_balance):
    if emp_id not in employees:
        employees[emp_id] = Employee(emp_id, name, leave_balance)
        print("Employee added successfully.")
    else:
        print("Employee already exists.")


def remove_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed successfully.")
    else:
        print("Employee does not exist.")


def update_leave_balance(emp_id, new_leave_balance):
    if emp_id in employees:
        employees[emp_id].leave_balance = new_leave_balance
        print("Leave balance updated successfully.")
    else:
        print("Employee does not exist.")


def main():
    while True:
        print("Leave Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Leave Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            leave_balance = int(input("Enter Leave Balance: "))
            add_employee(emp_id, name, leave_balance)

        elif choice == "2":
            emp_id = input("Enter Employee ID: ")
            remove_employee(emp_id)

        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            new_leave_balance = int(input("Enter New Leave Balance: "))
            update_leave_balance(emp_id, new_leave_balance)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
