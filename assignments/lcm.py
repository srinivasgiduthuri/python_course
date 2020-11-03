# Take two numbers and display LCM
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
max_num = num1 if num1 > num2 else num2
while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        print(f"LCM of {num1} and {num2} is {max_num}")
        break
    max_num += max_num
