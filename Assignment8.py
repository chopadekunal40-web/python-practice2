# Count ()

fruits = ("apple", "banana", "apple", "orange", "")

print(fruits.count("apple"))

fruits = ("apple", "banana", "apple", "orange", "apple")

print(fruits.count("apple"))

numbers = ("1002", "1003","1002" )

print(numbers.count("1002"))

# index ()

fruits = ("apple", "banana", "apple", "orange")

print(fruits.index("banana"))

fruits = ("apple", "banana", "apple", "orange")

print(fruits.index("apple"))

fruits = ("apple", "banana", "apple", "orange")

print(fruits.index("orange"))

numbers = (10, 20, 30, 20, 40, 20)

# count() method
print("Count of 20:", numbers.count(20))

# index() method
print("Index of 30:", numbers.index(30))

numbers = (10, 20, 40, 40, 40, 20)

print("Count of 40:", numbers.count(40))


print("Index of 10:", numbers.index(10))



Employee Salary Report
employees = (
    ("Rahul", 50000),
    ("Amit", 65000),
    ("Sneha", 72000),
    ("Pooja", 58000)
)