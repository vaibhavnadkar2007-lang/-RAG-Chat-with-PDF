# School Catalog Program
# Takes student details and prints in catalog format

students = []

def add_student():
    print("\n--- Enter Student Details ---")
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll No: ")
    grade = input("Enter Grade: ")
    div = input("Enter Division: ")
    
    student = {
        "Name": name,
        "Roll No": roll_no,
        "Grade": grade,
        "Division": div
    }
    students.append(student)
    print("Student added successfully!")

def display_catalog():
    if len(students) == 0:
        print("\nNo students in catalog yet!")
    else:
        print("\n=====================================")
        print("           SCHOOL CATALOG            ")
        print("=====================================")
        print(f"{'Roll No':<10} {'Name':<20} {'Grade':<8} {'Div':<5}")
        print("-------------------------------------")
        for s in students:
            print(f"{s['Roll No']:<10} {s['Name']:<20} {s['Grade']:<8} {s['Division']:<5}")
        print("=====================================")

def main():
    while True:
        print("\n1. Add Student")
        print("2. Display School Catalog")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_catalog()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2 or 3")

main()
