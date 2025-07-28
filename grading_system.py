    #AAU grading system

while True: 

    score = float(input("Enter your mark: "))
    if score >= 90:
        grade = 'A+'
    elif score >= 85:
        grade = 'A'
    elif score >= 80:
        grade = 'A-'
    elif score >= 75:
        grade = 'B+'
    elif score >= 68:
        grade = 'B'
    elif score >= 65:
        grade = 'B-'
    elif score >= 60:
        grade = 'C+'
    elif score >= 50:
        grade = 'C'
    elif score >= 45:
        grade = 'C-'
    elif score >= 40:
        grade = 'D'
    else:
        grade = 'F'

    #print the results

    print(f"Your grade is: {grade}")
    again = input("Try another? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break