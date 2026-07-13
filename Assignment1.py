# Assignment Operators

a = 20

print("Assignment Operators")
print("---------------------")

a += 5
print("+= :", a)

a -= 3
print("-= :", a)

a *= 2
print("*= :", a)

a /= 4
print("/= :", a)

print()

# Membership Operators

fruits = ["Apple", "Mango", "Banana"]

print("Membership Operators")
print("---------------------")

print("Apple" in fruits)
print("Orange" in fruits)
print("Orange" not in fruits)

print()

# Identity Operators

x = [10, 20, 30]
y = x
z = [10, 20, 30]

print("Identity Operators")
print("---------------------")

print(x is y)
print(x is z)
print(x is not z)