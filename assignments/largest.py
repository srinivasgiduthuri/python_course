# Numbers until zero is given and display the largest
largest = 0
while True:
    num = int(input("Enter a number"))
    if num == 0:
        break
    if num > largest:
        largest = num
print(f"{largest} is largest number")
