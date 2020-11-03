# Accept a string and display only uppercase letters of the string
string = input("Enter a string: ")
for char in string:
    if 65 <= ord(char) <= 90:
        print(char, end="")

for char in string:
    if char.isupper():
        print(char, end="")
