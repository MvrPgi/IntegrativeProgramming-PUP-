FirstName = input("Enter First Name: ")
LastName = input("Enter Last Name: ")
print("Welcome ", FirstName, LastName)
print("How Many Amazing Facts About Yourself You Can Share?")


N = int(input(""))
facts = []
for i in range(N):
    fact = input(f"Fact{i+1}: ")
    facts.append(fact)
print("", len(facts))
for i, fact in enumerate(facts, 1):
    print(f"Fact{i}:{fact}")

















