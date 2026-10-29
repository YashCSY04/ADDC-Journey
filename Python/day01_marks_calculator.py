print("STUDENT MARKS CALCULATOR")


m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))

total = m1 + m2 + m3

average = total / 3

print("Total marks:", total)
print("Average marks:", round(average, 2))
