srange() Function
# Q1
for i in range(1,21): print(i)

# Q2
for i in range(20,0,-1): print(i)

# Q3
for i in range(2,51,2): print(i)

# Q4
for i in range(1,51,2): print(i)

# Q5
for i in range(1,11): print(f"7 x {i} = {7*i}")

# Q6
for i in range(100,9,-10): print(i)

# Q7
for i in range(5,101,5): print(i)
for Loop
# Q1
for i in range(10): print("Your Name")

# Q2
for i in range(1,101): print(i)

# Q3
for i in range(1,11): print(i*i)

# Q4
for i in range(1,11): print(i**3)

# Q5
print(sum(range(1,101)))

# Q6
print(sum(1 for i in range(1,51) if i%3==0))

# Q7
for i in range(10,0,-1): print(i)

# Q8
text="FutureBright"; [print(i) for i in text if i.lower() in "aeiou"]

# Q9
numbers=[25,67,12,98,45]; print(max(numbers))

# Q10
marks=[45,78,90,34,88,51]; print(sum(1 for i in marks if i>50))
while Loop
# Q1
i=1; while i<=20: print(i); i+=1

# Q2
i=20; while i>=1: print(i); i-=1

# Q3
i=2; while i<=50: print(i); i+=2

# Q4
i=1; while i<=10: print(f"9 x {i} = {9*i}"); i+=1

# Q5
i=10; while i<=100: print(i); i+=10

# Q6
i=10; while i>=1: print(i); i-=1; print("Happy New Year!")

# Q7
b=5000; while b>0: print(b); b-=500

# Q8
p=""; while p!="python123": p=input("Password: ")
Lists
# Q1
marks=[78,56,89,91,45,62,98]; [print(i) for i in marks]

# Q2
print(sum(marks))

# Q3
print(sum(marks)/len(marks))

# Q4
print(sum(1 for i in marks if i>75))

# Q5
[print(i) for i in marks if i%2==0]

# Q6
[print(i) for i in marks if i%2!=0]

# Q7
print(max(marks))

# Q8
print(min(marks))

# Q9
print(sum(1 for i in marks if i<50))

# Q10
for i in marks: print("A" if i>=90 else "B" if i>=75 else "C" if i>=50 else "Fail
Nested Loops
# Q1
for i in range(4): print("* "*4)

# Q2
for i in range(1,5): print("* "*i)

# Q3
for i in range(4,0,-1): print("* "*i)

# Q4
for i in range(1,5): print(*range(1,i+1))

# Q5
for i in range(1,6): print(*[i*j for j in range(1,6)])

# Q6
shirts=["Red","Blue","Black"]; pants=["Jeans","Formal"]; [print(s,"-",p) for s in shirts for p in pants]

# Q7
for r in range(1,4): [print(f"Row {r} Seat {c}") for c in range(1,6)]
 Mixed Practice
# Q1
numbers=[12,-5,18,-20,34,-7,0]; print(sum(1 for i in numbers if i>0),sum(1 for i in numbers if i<0))

# Q2
for i in range(1,101):
    if i%3==0 and i%5==0: print(i)

# Q3
n=5; f=1; [exec("f*=i") for i in range(1,n+1)]; print(f)

# Q4
text="Python"; print(text[::-1])

# Q5
numbers=[12,17,24,31,40,55]; print(sum(i for i in numbers if i%2==0))

# Q6
for i in range(1,6): print((str(i)+" ")*i)

# Q7
for i in range(65,70): print(" ".join(chr(j) for j in range(65,i+1)))

# Q8
numbers=[2,5,7,2,9,5,10]; [print(numbers[i]) for i in range(len(numbers)) for j in range(i+1,len(numbers)) if numbers[i]==numbers[j]]

# Q9
prices=[120,450,99,250,180]; print(sum(prices))

# Q10
attendance=["Present","Absent","Present","Present","Absent"]; print("Present:",attendance.count("Present"),"Absent:",attendance.count("Absent"))