FirstName = input("Enter First Name: ")
LastName = input ("Enter Your Last Name: ")
print("Welcome ", FirstName,LastName)
print("How Many Amazing Facts About Yourself You Can Share?")


N = int(input(""))
facts = [] # To Store The Facts
for i in range(N):
    facts = input(f"Fact{i+1}: ")
    break

print("",len(facts))
for i, fact in enumerate(facts):
  print(f"Fact{i+1}:{fact}")