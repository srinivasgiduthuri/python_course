# Accept numbers from user until zero is given and display numbers in the sorted order
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    numbers.append(number)
print(f"List contains {numbers}. Sorted order is {sorted(numbers)}")
# Accept 10 numbers from user and display all odd numbers first then all even numbers
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    if number % 2 == 0:
        numbers.insert(-1, number)
    else:
        numbers.insert(0, number)
print(f"List contains {numbers}")
# Understand the difference between the methods extend(...) and append(...)
list1 = [1,2,3]
list2 = [4,5]
list1.append(list2)
print(list1)
list1.extend(list2)
print(list1)
