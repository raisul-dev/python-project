# we use while loop because we will not run it many type.
while True:
    #it's select what operation we needs
    operation = int (input(
    """
    Which operation do you went ?
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit
    Enter Operation No:
    """
    ))
    if operation == 5 :
           break
    # we collect tow num from user 
    num1 = float (input("Enter First Number:"))
    num2 = float (input("Enter Secound Number:"))
    #it run when user select any operation 
    if operation == 1 :
        print(f'Result :{num1} + {num2} = {num1+num2}')

    elif operation == 2:
         print(f'Result :{num1} - {num2} = {num1-num2}')

    elif operation == 3:
             print(f'Result :{num1} * {num2} = {num1*num2}')

    elif operation == 4:
                 print(f'Result :{num1} / {num2} = {num1/num2}')

    # user can't select any operation then run  else option
    else:
        print("Enter Valid Operation Number")