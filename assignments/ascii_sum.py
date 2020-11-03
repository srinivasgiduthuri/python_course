# Accept a string and display the sum of ascii codes
string = input("Enter a string: ")
ascii_sum = 0
for char in string:
    ascii_sum += ord(char)
print(f"ASCII sum for the string {string} is {ascii_sum}")
