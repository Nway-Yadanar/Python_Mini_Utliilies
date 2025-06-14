students = []

print("-----------------------------------")
print("Welcome to school management system")
print("-----------------------------------")

print("1. Add Student")
print("2. List Students")
print("3. Edit Students' Information")
print("4. Remove Student")
print("5. Exit")

while True:
    option = input("Enter the option: ")
    if option == "1":
        new = input("Enter the name of new student : ")
        students.append(new)
        print(f"New student , {new} , is added successfully")

    elif option =="2":
        print("\n---Student List---")
        for student in students:
            index_num = students.index(student) # to show numbers
            print(f"{index_num +1} . {student}")

    elif option == "3":
        pass

    elif option == "4":
        student_name = input ("Enter the student's name you want to delete : ")
        students.remove(student_name)
        print(f"{student_name} is removed successfully.")


    elif option == "5":
        print("Thank you for using our system")
        break

    else:
        print("Invaild option")