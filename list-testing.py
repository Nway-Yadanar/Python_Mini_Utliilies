# pop method

person_info = ["Nway", 19, "girl"]
removed = person_info.pop(1)
print(f"After pop: {person_info}")
print(f"Value removed: {removed}")

#  Remove Method
person_info = ["Nway", 19, "girl"]
removed = person_info.remove("Nway")
print(f"After removing gender : {person_info}")

# .extend()
students = ['Nway', 'Yadanar', 'Aung']
new_students = ['Min' , 'Mattral' ]
students.extend(new_students)
print(students)

# .append()
students = ['Nway', 'Yadanar', 'Aung']
new_students = ['Min' , 'Mattral' ]
students.append(new_students)
print(students)
