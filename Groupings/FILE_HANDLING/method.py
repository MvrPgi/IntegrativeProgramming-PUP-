#=========================================================================================================ADD=========================================================================================================
#=========================================================================================================ADD=========================================================================================================
#=========================================================================================================ADD=========================================================================================================
def add():
    try: 
        with open('product.txt', 'a') as file:   # Open the file in append mode
            while True:
                try:
                    productCode = int(input("Enter Product Code: ")) # Get the product code from the user
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    continue
                productName = input("Enter Product Name: ")
                
                try:
                    productQuantity = int(input("Enter Product Quantity: "))
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    continue
                file.write(f"{productCode},{productName},{productQuantity}\n") # Write the product details to the file
                choice = input("Do you want to add more products? (y/n): ")
                if choice.lower() != 'y':  # If the user does not want to add more products, break out of the loop
                    break
    finally:
        file.close()
        print("Data Successfuly Added.")
#=========================================================================================================DELETE=========================================================================================================
#=========================================================================================================DELETE=========================================================================================================
#=========================================================================================================DELETE=========================================================================================================

def delete():
    try:
    
        with open('product.txt', 'r') as file:     # Read all lines from the file
            lines = file.readlines()

     
        try:
            productCode = int(input("Enter Product Code to delete: "))  # Get the product code from the user
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return

    
        choice = input("Do you want to delete this product? (y/n): ") # Ask the user if they want to delete the product
        if choice.lower() != 'y':
            print("Deletion cancelled.")
            return

        # Rewrite the file excluding the product with the specified code
        with open('product.txt', 'w') as file:
            product_found = False
            for line in lines:
                code, name, quantity = line.strip().split(',')
                if int(code) != productCode:
                    file.write(f"{code},{name},{quantity}\n")
                else:
                    product_found = True

            if product_found:
                print(f"Product with code {productCode} deleted.") # Print a message if the product was found and deleted
            else:
                print(f"No product found with code {productCode}.") # Print a message if the product was not found
    finally:
        file.close() # Close the file
       
#=========================================================================================================EDIT=========================================================================================================
#=========================================================================================================EDIT=========================================================================================================
#=========================================================================================================EDIT=========================================================================================================

def edit():
    try:
        while True:
        
            with open('product.txt', 'r') as file:
                lines = file.readlines()

           
            try:
                productCode = int(input("Enter Product Code to edit: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

           
            with open('product.txt', 'w') as file:  # Rewrite the file with the new product details
                product_found = False
                for line in lines:
                    code, name, quantity = line.strip().split(',')
                    if int(code) == productCode:
                        newName = input("Enter new Product Name: ")
                        try:
                            newQuantity = int(input("Enter new Product Quantity: "))
                        except ValueError:
                            print("Invalid input. Please enter an integer.")
                            break

                        file.write(f"{code},{newName},{newQuantity}\n")
                        product_found = True
                    else:
                        file.write(f"{code},{name},{quantity}\n")

                if product_found:
                    print(f"Product with code {productCode} edited.") # Print a message if the product was found and edited
                else:
                    print(f"No product found with code {productCode}.") # Print a message if the product was not found

         
            choice = input("Do you want to edit more products? (y/n): ").strip().lower()
            if choice != 'y':  # If the user does not want to edit more products, break out of the loop
                break
    finally:
        print("Editing completed.")
        file.close()
#================================================================================================TRANS========================================================================================================= #================================================================================================TRANS========================================================================================================= #================================================================================================TRANS=========================================================================================================

def trans():
    try:
        while True:
       
            with open('product.txt', 'r') as file:
                lines = file.readlines()
            try:
                productCode = int(input("Enter Product Code: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

           
            product_found = False
            for line in lines:
                code, name, quantity = line.strip().split(',')
                if int(code) == productCode:
                    product_found = True
                    break

            if product_found:
                print(f"Product found: {code}, {name}, {quantity}")
                break
            else:
                print("Record not found. Please try again.")

        # Get transaction code
        transactionCode = input("Enter Transaction Code (P for Purchase, S for Sold): ").upper()
        if transactionCode not in ['P', 'S']:
            print("Invalid transaction code.")
            return

       
        try:
            quantity = int(input("Enter Quantity: ")) # Get the quantity from the user
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return

        with open('product.txt', 'w') as file: 
            for line in lines:
                code, name, prev_quantity = line.strip().split(',') 
                if int(code) == productCode: # Check if the product code matches the code entered by the user
                    if transactionCode == 'P':
                        new_quantity = int(prev_quantity) + quantity # Add the quantity to the previous quantity
                    else:
                        new_quantity = int(prev_quantity) - quantity # Subtract the quantity from the previous quantity
                    file.write(f"{code},{name},{new_quantity}\n")
                else:
                    file.write(line)

        print("Transaction completed.")
    finally:
        file.close()

#=========================================================================================================EXIT========================================================================================================= #=========================================================================================================EXIT========================================================================================================= #=========================================================================================================EXIT=========================================================================================================       
def exit():
    print("END OF PROGRAM.")
