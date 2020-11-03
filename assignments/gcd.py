# Take two numbers and display GCD
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
counter = 1
gcd = 0
while counter <= num1 and counter <= num2:
    if num1 % counter == 0 and num2 % counter == 0:
        gcd = counter
    counter += 1
print(f"GCD of {num1} and {num2} is {gcd}")
