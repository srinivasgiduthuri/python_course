# Sort different types of elements in a list - investigate
# Accept numbers from user until zero is given and display all unique numbers in sorted order
numbers = set()
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    numbers.add(number)
print(f"Set contains {numbers}. Sorted order is {sorted(numbers)}")
# Accept a string and display how many times each character is occurring
user_input = input("Enter a string: ")
distinct_letters = set(user_input)
for char in distinct_letters:
    print(f"{char} appears {user_input.count(char)} times")
# Accept names from user until END is given and display all the unique characters in each name
while True:
    name = input("Enter a name: ")
    if name.__eq__('END'):
        break
    print(f"Unique characters in the {name} are {set(name)}")
# Accept names from user until END is given and display all the unique characters in all names
names = []
unique_letters = set()
while True:
    name = input("Enter a name: ")
    if name.__eq__('END'):
        break
    names.append(name)
    [unique_letters.add(char) for char in name]
print(f"Unique characters in the {names} are {unique_letters}")
