# Take a string and display how many times each alphabet is occurring
string = "how do you do"
alpha_map = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0,
             "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
for char in string.upper():
    if char in alpha_map:
        alpha_map[char] += 1
print(alpha_map)

# Take a string and display how many times each word is occurring
word_map = {}
for word in string.upper().split():
    if word in word_map:
        word_map[word] += 1
    else:
        word_map[word] = 1
print(word_map)


# Create a function that takes a number and display the factors of the number
def factors(num):
    for i in range(1, num // 2):
        if num % i == 0:
            print(i)


factors(15)


# Create a function that takes a string and print alphanumeric characters only
def print_alphanumeric_only(val=""):
    for char in val:
        if char.isalnum():
            print(char, end="")


string = "Python 3.9"
print_alphanumeric_only(string)
