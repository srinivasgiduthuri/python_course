# Accept marks from user and display grade
# >80 - A
# >70 - B
# >60 - C
# <=60 - D

marks = int(input("Enter the marks: "))
if marks > 80:
    print("A")
elif marks > 70:
    print("B")
elif marks > 60:
    print("C")
else:
    print("D")

# Accept month number(1-12) from user and display the number of days

# Take year from the user and check whether it is a leap year or not

# Print squares of numbers 10 to 20
for number in range(10, 21, 1):
    print(f"Square of {number}: {number * number}")

# Accept 10 numbers and display sum of +ve numbers and -ve numbers and stop the loop when user enters zero
# 4x4 matrix
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
