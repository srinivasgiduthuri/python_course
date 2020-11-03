# Accept a string like 10,20,30,40... and print the sum of numbers
number_string = "10,20,30,40,50"
total = 0
for split_number in number_string.split(sep=","):
    total += int(split_number)
print(f"Total of {number_string} is {total}")

# Accept a string and print all the indices where the particular string present
string = "How do you do"
search_string = "do"
position = -1
while True:
    position = string.find(search_string, position + 1)
    if position == -1:
        break
    print(position)

# Accept a string and display how many times each digit is occurring
string_with_numbers = "Python 3.9 released on 12th Oct 2020"
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(f"Count of {number} - {string_with_numbers.count(str(number))}")

# Accept a string and display how many times each vowel is occurring
vowels = ["a", "e", "i", "o", "u"]
for vowel in vowels:
    print(f"Count of {vowel} - {string_with_numbers.count(vowel)}")
