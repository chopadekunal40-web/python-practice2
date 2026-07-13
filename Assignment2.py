# ==========================
# PRACTICE ASSIGNMENT
# if, if-else, if-elif-else, Nested if
# ==========================

# --------------------------
# IF STATEMENT
# --------------------------

# 1. Eligible to Vote
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to Vote")

# 2. Positive Number
num = int(input("Enter number: "))
if num > 0:
    print("Positive Number")

# 3. Marks above 90
marks = int(input("Enter marks: "))
if marks > 90:
    print("Excellent")

# 4. Product in Stock
stock = int(input("Enter stock quantity: "))
if stock > 0:
    print("Product Available")

# 5. Age >=18
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")

# 6. Temperature above 100
temp = float(input("Enter temperature: "))
if temp > 100:
    print("High Temperature")

# 7. Salary >50000
salary = int(input("Enter salary: "))
if salary > 50000:
    print("High Salary")


# --------------------------
# IF ELSE
# --------------------------

# 1. Positive or Negative
num = int(input("Enter number: "))
if num >= 0:
    print("Positive")
else:
    print("Negative")

# 2. Even or Odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Vote Eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# 4. Pass or Fail
marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# 5. Balance Check
balance = int(input("Enter balance: "))
amount = int(input("Enter payment amount: "))
if balance >= amount:
    print("Payment Successful")
else:
    print("Insufficient Balance")

# 6. Stock Check
stock = int(input("Enter stock: "))
if stock > 0:
    print("Available")
else:
    print("Out of Stock")

# 7. Fever Check
temp = float(input("Enter body temperature: "))
if temp > 99:
    print("Fever")
else:
    print("Normal")


# --------------------------
# IF ELIF ELSE
# --------------------------

# 1. Grade Calculator
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")

# 2. Age Classification
age = int(input("Enter age: "))
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")

# 3. Traffic Signal
signal = input("Enter signal (Red/Yellow/Green): ")
if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Wait")
elif signal == "Green":
    print("Go")
else:
    print("Invalid Signal")

# 4. Discount
amount = float(input("Enter purchase amount: "))
if amount >= 5000:
    print("30% Discount")
elif amount >= 3000:
    print("20% Discount")
elif amount >= 1000:
    print("10% Discount")
else:
    print("No Discount")

# 5. Temperature
temp = int(input("Enter temperature: "))
if temp < 15:
    print("Cold")
elif temp < 25:
    print("Warm")
elif temp < 35:
    print("Hot")
else:
    print("Very Hot")

# 6. Membership
points = int(input("Enter points: "))
if points >= 1000:
    print("Platinum")
elif points >= 700:
    print("Gold")
elif points >= 400:
    print("Silver")
else:
    print("Regular")

# 7. Menu
print("1. Hello")
print("2. Welcome")
print("3. Exit")
choice = int(input("Enter choice: "))
if choice == 1:
    print("Hello User")
elif choice == 2:
    print("Welcome User")
elif choice == 3:
    print("Good Bye")
else:
    print("Invalid Choice")


# --------------------------
# NESTED IF
# --------------------------

# 1. Exam Eligibility
attendance = int(input("Attendance (%): "))
if attendance >= 75:
    fees = input("Fees Paid (yes/no): ")
    if fees == "yes":
        print("Eligible for Exam")
    else:
        print("Pay Fees First")
else:
    print("Attendance Short")

# 2. Login System
username = input("Username: ")
if username == "admin":
    password = input("Password: ")
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

# 3. ATM
card = input("Insert Card (yes/no): ")
if card == "yes":
    pin = int(input("Enter PIN: "))
    if pin == 1234:
        print("Access Granted")
    else:
        print("Wrong PIN")
else:
    print("Insert Card")

# 4. College Admission
marks = int(input("Enter Marks: "))
if marks >= 60:
    docs = input("Documents Verified (yes/no): ")
    if docs == "yes":
        print("Admission Confirmed")
    else:
        print("Verify Documents")
else:
    print("Not Eligible")

# 5. Online Shopping
stock = input("Product Available (yes/no): ")
if stock == "yes":
    payment = input("Payment Done (yes/no): ")
    if payment == "yes":
        print("Order Confirmed")
    else:
        print("Payment Pending")
else:
    print("Out of Stock")

# 6. Hospital Appointment
registered = i  nput("Registered (yes/no): ")
if registered == "yes":
    doctor = input("Doctor Available (yes/no): ")
    if doctor == "yes":
        print("Appointment Confirmed")
    else:
        print("Doctor Not Available")
else:
    print("Please Register First")1