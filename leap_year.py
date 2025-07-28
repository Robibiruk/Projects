while True:
    year = int(input("Enter a year to check if it's a leap year or not: "))
    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    
       
    again = input("Wanna check again? (yes/no)").lower()
    if again == "yes":
       continue 
    else:
     print("Goodbye!")
     break
     