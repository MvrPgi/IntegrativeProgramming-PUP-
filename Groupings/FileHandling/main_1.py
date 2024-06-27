import method as m



def main():
  while True:
    print("A. Add a new product")
    print("D. Delete a product")
    print("E. Edit a product")
    print("T. Transaction")
    print("X. Quit")


    choice = input("Enter your choice: ")
    if choice == 'A':
        m.add()
    elif choice == 'D':
        m.delete()
    elif choice == 'E':
        m.edit()
    elif choice == 'T':
        m.trans()
    elif choice == 'X':
        m.exit()
        break
    else:
        m.print("Invalid choice. Please enter a letter from A-X.")  

if __name__ == "__main__":
    main()




