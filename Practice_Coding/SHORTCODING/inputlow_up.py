
while True:
  name =(input("Enter Your Name: "))
 
  if name.islower():
    print (name.upper())
    print("-----------------------------------")
  elif name.isupper():
    print(name.lower())
    print("-----------------------------------")
  else:
    print(" BOBO KA BA MAG TYPE!?")
    break