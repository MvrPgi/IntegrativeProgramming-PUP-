#DEF ADD
def add():
    try:
        with open('product.txt', 'a') as file:
            while True:
                productCode = int(input("Enter Product Code: "))
                productName = input("Enter Product Name: ")
                productQuantity = int(input("Enter Product Quantity: "))
                file.write(f"{productCode},{productName},{productQuantity}\n")

                choice = input("Do you want to add more products? (y/n): ")
                if choice.lower() != 'y':
                    break
    except Exception as e:
        print(f"An error occurred: {e}")
   
#DEF DELETE
def delete():
    try:
        with open('product.txt', 'r') as file:
            lines = file.readlines()
        with open('product.txt', 'w') as file:
            productCode = int(input("Enter Product Code to delete: "))
            for line in lines:
                code, name, quantity = line.strip().split(',')
                if int(code) != productCode:
                    file.write(f"{code},{name},{quantity}\n")
    except Exception as e:
        print(f"An error occurred: {e}")
   

#DEF EDIT
def edit():
    try:
        with open('product.txt', 'r') as file:
            lines = file.readlines()
        with open('product.txt', 'w') as file:
            productCode = int(input("Enter Product Code to edit: "))
            for line in lines:
                code, name, quantity = line.strip().split(',')
                if int(code) == productCode:
                    newName = input("Enter new Product Name: ")
                    newQuantity = int(input("Enter new Product Quantity: "))
                    file.write(f"{code},{newName},{newQuantity}\n")
                else:
                    file.write(f"{code},{name},{quantity}\n")
    except Exception as e:
        print(f"An error occurred: {e}")
    if not type(productCode) is int:
        raise TypeError("Only integers are allowed")
 

#DEF TRANSACT

# def trans():
#     try:
#         product_code = input("Enter the product code: ").strip().upper()
#         found = False
#         with open("Products.txt", "r") as file:
#             lines = file.readlines()

#         with open("Products.txt", "w") as file:
#             for line in lines:
#                 if line.startswith(product_code + ","):
#                     found = True
#                     data = line.strip().split(',')
#                     current_quantity = int(data[2])
                    
#                     while True:
#                         transaction_code = input("Enter transaction code ('P' for Purchase, 'S' for Sold): ").strip().upper()
#                         if transaction_code in ['P', 'S']:
#                             break
#                         else:
#                             print("Invalid transaction code. Please enter 'P' or 'S'.")

#                     quantity = int(input("Enter the quantity: ").strip())
#                     if quantity <= 0:
#                         print("Quantity must be a positive integer.")
#                         file.write(line)
#                         continue

#                     if transaction_code == 'P':
#                         current_quantity += quantity
#                     elif transaction_code == 'S':
#                         if current_quantity < quantity:
#                             print(f"Insufficient quantity. Available stock: {current_quantity}.")
#                             file.write(line)
#                             continue
#                         current_quantity -= quantity

#                     file.write(f"{product_code},{data[1]},{current_quantity}\n")
#                     print(f"Transaction completed. New quantity of {product_code}: {current_quantity}")
#                 else:
#                     file.write(line)

#         if not found:
#             print("Record not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     display()

#DEF DISPLAY
def display():
    try:
        with open('product.txt', 'r') as file:
            print("Product Code\tProduct Name\tProduct Quantity")
            for line in file:
                code, name, quantity = line.strip().split(',')
                print(f"{code}\t{name}\t{quantity}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        display()
        print("\n1. Add Product")
        print("2. Delete Product")
        print("3. Edit Product")
        print("4. Transact Product")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add()
        elif choice == '2':
            delete()
        # elif choice == '3':
        #     edit()
        # elif choice == '4':
        #     trans()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number from 1-6.")

if __name__ == "__main__":
    main()