while True:
    #input files
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter Second number: "))
    operation = int(input("Choose operation: 1. addition 2. subtraction 3. multiplication 4. division 5. Remainder: "))
    opp1 = num1 + num2
    opp2 = num1 - num2
    opp3 = num1 * num2


    #if and else
    if operation == 1:
        print(f"{num1} + {num2} = {opp1}")
    elif operation == 2:
        print(f"{num1} - {num2} = {opp2}")
    elif operation == 3:
        print(f"{num1} * {num2} = {opp3}")
    elif operation == 4:
        if num2 == 0:
            print("Invalid")
        else:
            quotient = num1 / num2
            remainder = num1  % num2
            print(f"{num1} / {num2} = {quotient} R{remainder}")
    elif operation == 5:
        if num2 == 0:
            print("Invalid")
        else:
            remainder2 = num1 % num2
            print(f"{num1} % {num2} = {remainder2}")
    else:
        print("Invalid option, Plese choose from 1 to 5")
        continue
    again = input("Continue: (yes/no)").lower()
    if again != "yes":
        print("goodbye")
        break

