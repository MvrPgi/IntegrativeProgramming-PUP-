# Write A Program that will continously input names of students, gender and 
# age until "none" is inputted. Store the inputted details in a dictionary name classDetails
# and output each student record

#student_name=input("Enter Student Name: ")
#student_gender=input("Enter Student Gender: ")
#student_age=input("Enter Student Age: ")


#classDetails ={
#"Name": [], 
#"Gender": [], 
#"Age":[]
#}

#classDetails["Name"] = student_name
#classDetails["Gender"] = student_gender
#classDetails["Age"] = student_age
#print(classDetails)
classDetails = []
while True : 
  student_name=input("Enter Student Name: ") 
  student_name == 'none';
  student_gender=input("Enter Student Gender: ")
  student_age=input("Enter Student Age: ")

  student_details={              # MAKES THE LIST INTO DICTIONARY
  "name"  : student_name  ,
  "gender" :student_gender ,
  "age" : student_age
  
  }
  classDetails.append(student_details)

  for idx, student in enumerate(classDetails, 1):
      print(f"Student {idx}: {student}")







