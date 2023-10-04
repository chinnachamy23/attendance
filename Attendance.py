present = 0
absent = 0
present_students = []
absent_students = []

for student in ["Raju", "Kamal", "samy", "nesan", "raja"]:
    print(student)
    
    attendance = input("Enter your attendance (P for present, A for absent): ").upper()
    
    if attendance == "P":
        present_students.append(student)
        present += 1
    else:
        absent_students.append(student)
        absent += 1

percentage = (present / 5 * 100)

print("Number of students present: ", present)
print("Number of students absent: ", absent)
print("Today's attendance percentage: ", percentage)

# Print the present students with serial numbers
print("Students Present List:")
for idx, student in enumerate(present_students, start=1):
    print(f"{idx}. {student}")

# Print the absent students with serial numbers
print("Students Absent List:")
for idx, student in enumerate(absent_students, start=1):
    print(f"{idx}. {student}")
