# ==========================
# Assignment 1: Employee Database
# ==========================

print("\nAssignment 1")

employee = {}

if employee:
    print("Employee data exists.")
else:
    print("Employee data does not exist.")

# ==========================
# Assignment 2: Traffic Signal
# ==========================

print("\nAssignment 2")

signal = input("Enter Signal Color: ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")

# ==========================
# Assignment 3: Calculator
# ==========================

print("\nAssignment 3")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter Choice: "))

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

match choice:
    case 1:
        print("Result =", num1 + num2)
    case 2:
        print("Result =", num1 - num2)
    case 3:
        print("Result =", num1 * num2)
    case 4:
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot Divide by Zero")
    case _:
        print("Invalid Choice")

# ==========================
# Assignment 4: ATM Menu
# ==========================

print("\nAssignment 4")

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")

choice = int(input("Enter Choice: "))

match choice:
    case 1:
        print("Deposit Selected")
    case 2:
        print("Withdraw Selected")
    case 3:
        print("Balance Enquiry Selected")
    case 4:
        print("Exit")
    case _:
        print("Invalid Choice")

# ==========================
# Assignment 5: Food Ordering
# ==========================

print("\nAssignment 5")

print("1. Pizza")
print("2. Burger")
print("3. Sandwich")
print("4. Pasta")

choice = int(input("Enter Choice: "))

match choice:
    case 1:
        print("Pizza Ordered")
    case 2:
        print("Burger Ordered")
    case 3:
        print("Sandwich Ordered")
    case 4:
        print("Pasta Ordered")
    case _:
        print("Invalid Choice")

# ==========================
# Assignment 6: Student Grade
# ==========================

print("\nAssignment 6")

grade = input("Enter Grade (A/B/C/D/F): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")

# ==========================
# Assignment 7: Banking Deposit
# ==========================

print("\nAssignment 7")

account = input("Account Active (True/False): ") == "True"
kyc = input("KYC Completed (True/False): ") == "True"
amount = float(input("Deposit Amount: "))

if not account:
    print("Deposit Rejected")
elif not kyc:
    print("Complete KYC")
elif amount <= 0:
    print("Invalid Deposit Amount")
elif amount > 200000:
    print("Manager Approval Required")
elif amount > 50000:
    print("PAN Verification Required")
else:
    print("Deposit Successful")

# ==========================
# Assignment 8: Smart Login
# ==========================

print("\nAssignment 8")

username = input("Username: ")
password = input("Password: ")
otp = input("OTP Verified (True/False): ") == "True"

if not username:
    print("Username Cannot Be Empty")
elif not password:
    print("Password Cannot Be Empty")
elif not otp:
    print("OTP Verification Failed")
else:
    print("Login Successful")

# ==========================
# Assignment 9: Certificate System
# ==========================

print("\nAssignment 9")

course = input("Course Completed (True/False): ") == "True"
project = input("Project Submitted (True/False): ") == "True"
exam = input("Exam Passed (True/False): ") == "True"

if course and project and exam:
    print("Certificate Issued")
else:
    print("Certificate Not Issued")

# ==========================
# Assignment 10: Airline Boarding
# ==========================

print("\nAssignment 10")

ticket = input("Ticket Confirmed (True/False): ") == "True"
passport = input("Passport Valid (True/False): ") == "True"
security = input("Security Check Completed (True/False): ") == "True"

if ticket and passport and security:
    print("Boarding Allowed")
else:
    print("Boarding Denied")

# ==========================
# Assignment 11: Mini Banking App
# ==========================

print("\nAssignment 11")

balance = 10000

print("1. Deposit")
print("2. Withdraw")
print("3. Balance Enquiry")
print("4. Exit")

choice = int(input("Enter Choice: "))

match choice:
    case 1:
        amount = float(input("Enter Deposit Amount: "))
        if amount > 0:
            balance += amount
            print("Deposit Successful")
            print("Balance =", balance)
        else:
            print("Invalid Deposit Amount")

    case 2:
        amount = float(input("Enter Withdraw Amount: "))
        if amount <= 0:
            print("Invalid Amount")
        elif amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            print("Withdrawal Successful")
            print("Balance =", balance)

    case 3:
        if balance:
            print("Current Balance =", balance)
        else:
            print("No Balance")

    case 4:
        print("Thank You")

    case _:
        print("Invalid Menu Choice")