attendance = {}

while True:
    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        status = input("Present or Absent: ")
        attendance[name] = status
        print("Attendance marked!")

    elif choice == "2":
        if attendance:
            for name, status in attendance.items():
                print(name, ":", status)
        else:
            print("No attendance records")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")