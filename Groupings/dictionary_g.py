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

for _ in range(2): ## MAKE 2 INPUTS
  student_name=input("Enter Student Name: ") 
  student_gender=input("Enter Student Gender: ")
  student_age=input("Enter Student Age: ")

  namelist = [student_name]  ## STORES THEM IN A LIST
  genderlist =[student_gender]
  agelist= [student_age]

classDetails={              # MAKES THE LIST INTO DICTIONARY
  "name"  :[namelist]  ,
  "gender" :[genderlist] ,
  "age" :[agelist]

Fclass = {}
Fclass = Fclass + classDetails #STORES THE CLASSDETAILS IN A SEPARATE DICTIONARY BEFORE ITERATION



}

