class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Sorting Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        sorted_employees = sorted(employees, key=lambda emp: emp.age)
        print("\nSorted Employee Data by Age:")
        for emp in sorted_employees:
            print(f"Age: {emp.age}, {emp}")
    elif choice == 2:
        sorted_employees = sorted(employees, key=lambda emp: emp.name)
        print("\nSorted Employee Data by Name:")
        for emp in sorted_employees:
            print(f"Name: {emp.name}, {emp}")
    elif choice == 3:
        sorted_employees = sorted(employees, key=lambda emp: emp.salary)
        print("\nSorted Employee Data by Salary:")
        for emp in sorted_employees:
            print(f"Salary: {emp.salary}, {emp}")
    else:
        print("Invalid choice")
        return

if __name__ == "__main__":
    main()
