# Use filter to select strings that contain one or more uppercase letters

names = ["John", "peter", "parKer"]


def contains_uppercase(val):
    for char in str(val):
        if char.isupper():
            return True
        else:
            continue
    else:
        return False


print(list(filter(contains_uppercase, names)))

# Ignore the invalid entry

st = "90,70,abc"


def convert_to_int(num):
    if str(num).isnumeric():
        return int(num)
    else:
        return 0


print(sum(map(convert_to_int, st.split(","))))
# Display sum of digits for each number in a list using map function
numbers = [2916, 1832, 1769, 4051, 2104, 2453, 4542, 1214, 4225, 2574]


def sum_digits(val):
    return sum(map(int, str(val)))


print(list(map(sum_digits, numbers)))
# Display strings that have length more than 5 using filter function

print(list(filter(lambda val: len(str(val)) >= 5, names)))
