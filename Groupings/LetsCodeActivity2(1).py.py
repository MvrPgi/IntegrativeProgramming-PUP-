classDetails = []
student_count = 1

while True:
    student_name = input("Enter Student Name (type 'none' to stop): ")
    if student_name.lower() == 'none':
        break

    student_gender = input("Enter Student Gender: ")
    student_age = input("Enter Student Age: ")

    # Format the student details as a dictionary and append it to the classDetails list
    student_details = {'name': student_name, 'gender': student_gender, 'age': student_age}
    classDetails.append(student_details)

    # Print the details of the student that was just entered with student count
    print(f"Student {student_count}: {student_details}")
    student_count += 1
    print()

print("\nStudent records (sorted by name):")
sorted_classDetails = sorted(classDetails, key=lambda x: x['name'])
for index, details in enumerate(sorted_classDetails, start=1):
    print(f"Student {index}: {details}")
    