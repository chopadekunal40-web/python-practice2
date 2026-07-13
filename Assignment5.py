# ==========================================
# Section A – Basic String Operations
# ==========================================

full_name = "Rahul Sharma"

# 1. Print full name
print("1.", full_name)

# 2. Length
print("2. Length:", len(full_name))

# 3. First and last character
print("3. First:", full_name[0], "Last:", full_name[-1])

# 4. Third character
print("4. Third character:", full_name[2])

# 5. Last three characters
print("5. Last three characters:", full_name[-3:])

# 6. Reverse using slicing
print("6. Reverse:", full_name[::-1])

# 7. Every second character
print("7. Every second character:", full_name[::2])

# 8. Reverse using negative indexing
print("8. Reverse:", full_name[::-1])

# ==========================================
# Section B – Indexing & Slicing
# ==========================================

# 9. First name
first_name = full_name.split()[0]
print("9. First name:", first_name)

# 10. Last name
last_name = full_name.split()[-1]
print("10. Last name:", last_name)

# 11. First five characters
print("11.", full_name[:5])

# 12. Except first and last
print("12.", full_name[1:-1])

# 13. Reverse each word
text = "Python Programming"
words = text.split()
reversed_words = [word[::-1] for word in words]
print("13.", " ".join(reversed_words))

# ==========================================
# Section C – Traversing Strings
# ==========================================

sample = "Python"

# 14. Using for loop
print("14.")
for ch in sample:
    print(ch)

# 15. Using while loop
print("15.")
i = 0
while i < len(sample):
    print(sample[i])
    i += 1

# 16. Count vowels
string = "Python Programming"
vowels = "aeiouAEIOU"
vowel_count = 0

for ch in string:
    if ch in vowels:
        vowel_count += 1

print("16. Vowels:", vowel_count)

# 17. Count consonants
consonant_count = 0

for ch in string:
    if ch.isalpha() and ch not in vowels:
        consonant_count += 1

print("17. Consonants:", consonant_count)

# 18. Character with index
print("18.")
for index, ch in enumerate(sample):
    print(index, ":", ch)

# ==========================================
# Section D – Searching Methods
# ==========================================

text = "Java and Python are amazing"

# 19. First occurrence of 'a'
print("19.", text.find("a"))

# 20. Last occurrence of 'a'
print("20.", text.rfind("a"))

# 21. Count spaces
print("21.", text.count(" "))

# 22. Starts with Python
sentence = "Python is easy"
print("22.", sentence.startswith("Python"))

# 23. Ends with .pdf
filename = "report.pdf"
print("23.", filename.endswith(".pdf"))

# 24. Index of Python
print("24.", sentence.find("Python"))

# ==========================================
# Section E – Case Conversion
# ==========================================

sentence = "python programming is fun"

print("25.", sentence.upper())
print("26.", sentence.lower())
print("27.", sentence.title())
print("28.", sentence.capitalize())
print("29.", sentence.swapcase())

# ==========================================
# Section F – Whitespace Handling
# ==========================================

text = "   Hello Python   "

print("30.", text.lstrip())
print("31.", text.rstrip())
print("32.", text.strip())

print("33. Original Length:", len(text))
print("    Cleaned Length:", len(text.strip()))

# ==========================================
# Section G – Split, Join & Replace
# ==========================================

languages = "Python,Java,C++,Go"

# 34.
lang_list = languages.split(",")
print("34.", lang_list)

# 35.
print("35.", " | ".join(lang_list))

# 36.
print("36.", languages.replace("Java", "Rust"))

# 37.
text = "Python Python Python"
print("37.", text.replace("Python", "Java", 1))

# ==========================================
# Section H – Validation Methods
# ==========================================

inputs = [
    "Python",
    "12345",
    "Python123",
    " ",
    "HELLO",
    "hello",
    "Future Bright",
    "student_name"
]

for s in inputs:
    print("\nString:", repr(s))
    print("38. isalpha():", s.isalpha())
    print("39. isdigit():", s.isdigit())
    print("40. isalnum():", s.isalnum())
    print("41. islower():", s.islower())
    print("42. isupper():", s.isupper())
    print("43. isspace():", s.isspace())
    print("44. istitle():", s.istitle())
    print("45. isidentifier():", s.isidentifier())
    print("46. isascii():", s.isascii())

# ==========================================
# Section I – String Formatting
# ==========================================

name = "Rahul Sharma"
age = 20
course = "BCA"
city = "Pune"

# 47. Concatenation
print("\n47.")
print("Name: " + name + ", Age: " + str(age) + ", Course: " + course + ", City: " + city)

# 48. % Formatting
print("\n48.")
print("Name: %s, Age: %d, Course: %s, City: %s" % (name, age, course, city))

# 49. format()
print("\n49.")
print("Name: {}, Age: {}, Course: {}, City: {}".format(name, age, course, city))

# 50. f-Strings
print("\n50.")
print(f"Name: {name}, Age: {age}, Course: {course}, City: {city}")

# 51. Sum inside f-string
a = 15
b = 25
print("\n51.")
print(f"Sum of {a} and {b} = {a+b}")

# 52. Shopping bill
item = "Notebook"
qty = 3
price = 80
total = qty * price

print("\n52. Shopping Bill")
print(f"Item     : {item}")
print(f"Quantity : {qty}")
print(f"Price    : ₹{price}")
print(f"Total    : ₹{total}")

# ==========================================
# Section J – Comparison & Membership
# ==========================================

# 53.
print("\n53.", "Apple" < "Banana")

# 54.
print("54.", "Python" == "python")

# 55.
print("55.", "Bright" in "FutureBright IT Solutions")

# 56.
print("56.", "Java" not in "Python Programming")

# 57.
email = "student@gmail.com"
print("57.", "@" in email)

# 58.
filename = "Assignment5.py"
print("58.", filename.endswith(".txt"))
