print("STUDENT GRADE CALCULATOR")

tamil = int(input("Enter Tamil mark: "))
english = int(input("Enter English mark: "))
maths = int(input("Enter Maths mark: "))
science = int(input("Enter Science mark: "))
computer = int(input("Enter Computer mark: "))

total = tamil + english + maths + science + computer
average = total / 5

print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")

if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")
