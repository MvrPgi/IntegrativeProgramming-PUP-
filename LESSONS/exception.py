## occures during the execution of a program that disrupts the normal flow of the program's instruction.
## the try block lets you test a block for errors
## except block lets you handle the error
## else block lets you execute code when there is no error
## finally block lets you execute the code regardless

#try:
  #print(x) # THIS IS AN ERROR
#except:
  #print("ERROR")



## TRY EXCEPT

#x ="Rachel"
#try:
  #print(x) # THIS IS AN ERROR
  #print(x+25)
#except NameError:
 # print("Variable Not Defined")
#except ValueError:
  #print("Invalid Input")
#except TypeError:
  #print("Something Went Wrong")


## TRY ELSE

#x ="Rachel"
#try:
  #print(x) # THIS IS AN ERROR
#except NameError:
 #print("Variable Not Defined")
#except ValueError:
  #print("Invalid Input")
#except TypeError:
  #print("Something Went Wrong")
#else:
  #print(x)

## FINALLY

#x ="Rachel"
#try:
  #print(x) # THIS IS AN ERROR
#except NameError:
 #print("Variable Not Defined")
#except ValueError:
  #print("Invalid Input")
#except TypeError:
  #print("Something Went Wrong")
#else:
  #print(x)
#finally:
  #print("END")

## LETS CODE #1
while True:
  try:
    divEnd = float(input("Dividend: "))
    div = float(input("Divisor: "))
    qou = divEnd/div
    print(qou)
    #ans = input("Y/N")
    #if ans.upper() != 'Y' and ans.upper() !='N':
      #break
  
   
  except ValueError:
    print("Value Error")
    
  except TypeError:
    print("Integers Only") 
  except ZeroDivisionError:
    print("None Zero Value")
  else:
    print("Okay Code")
  finally:
    print("End")
    




