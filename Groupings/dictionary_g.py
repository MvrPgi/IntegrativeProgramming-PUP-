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
  if student_name.lower() == 'none':
    break
  student_gender=input("Enter Student Gender: ")
  student_age=input("Enter Student Age: ")

  student_details={              # MAKES THE INPUT INTO DICTIONARY
  "name"  : student_name  ,
  "gender" :student_gender ,
  "age" : student_age
  
  }

  ## THE LOOP THAT SHOWS THE STORED DICTIONARY THAT APPENDS THE STUDENT DETAILS DICTIONARY TO CLASS DETAILS 
 
  classDetails.append(student_details) 
  for idx, student in enumerate(classDetails, 1):  #ITERATES THE CLASS DETAILS AND PRINTS THE EQUIVALENT INDEX OF EACH DATA
      print(f"Student {idx}: {student}")

  values = [ 
  list(d.values()) for d in classDetails if isinstance(d,dict)  ## ITERATES WITHIN THE LOOP THAT GETS THE VALUES OF THE INPUT
  ]
  print(values)


##  Ascending Format(age) 
##  Ascending Alphabethical(name) 







