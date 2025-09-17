# Python Mini Projects

This repository contains a collection of simple Python programs that demonstrate basic programming concepts like arithmetic operations, conditionals, loops, and user input. These projects are great for beginners to practice problem-solving with Python.

---

## 📌 Projects Included

### 1. Basic Arithmetic
```python
a = 5 + 3        # addition
b = 7 - 22       # subtraction
c = 567 * 66     # multiplication
d = 777 / 7      # division
e = 286 % 12     # remainder

print(a, b, c, d, e)
````

Performs basic math operations and prints the results.

---

### 2. Interactive Calculator

```python
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter Second number: "))
    operation = int(input("Choose operation (1:add 2:subtract 3:multiply 4:divide 5:remainder): "))

    if operation == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == 4:
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    elif operation == 5:
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("Invalid choice. Try again.")

    again = input("Continue? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
```

A looped calculator that supports multiple operations and handles invalid inputs.

---

### 3. Age Check (Voting Eligibility)

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You're allowed to vote.")
else:
    print("You are under age.")
```

Simple control flow example for checking voting eligibility.

---

### 4. Grading System

```python
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

    print(f"Your grade is: {grade}")

    again = input("Try another? (yes/no): ").lower()
    if again not in ["yes", "y"]:
        print("Goodbye!")
        break
```

Implements the **AAU grading system** and allows multiple attempts.

---

### 5. Leap Year Checker

```python
while True:
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

    again = input("Check again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
```

Checks if a given year is a leap year.

---

## 🚀 How to Run

1. Make sure Python is installed on your machine.
   You can check with:

   ```bash
   python --version
   ```
2. Clone this repository:

   ```bash
   git clone https://github.com/YourUsername/YourRepoName.git
   cd YourRepoName
   ```
3. Run any script:

   ```bash
   python filename.py
   ```

---

## 🎯 Skills Learned

* Using variables and operators
* Handling user input
* Applying conditional statements (`if`, `elif`, `else`)
* Looping with `while`
* Error handling (e.g., divide by zero)

---

## 📷 Example Output

```
Enter first number: 10
Enter Second number: 5
Choose operation: (1-5): 1
10.0 + 5.0 = 15.0
Continue? (yes/no): no
Goodbye!
```

---
