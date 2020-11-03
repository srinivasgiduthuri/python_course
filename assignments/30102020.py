# Create a function that takes multiple names and prints only first four letters of each name
def first_four_letters(*names):
    for name in names:
        print(str(name)[:4])


first_four_letters("Steve", "Larry", "James")


# Create a function that takes a list and returns how many positive numbers and negative numbers
def count_positive_negative(numbers: list):
    neg_count = 0
    pos_count = 0
    for number in numbers:
        if number >= 0:
            pos_count += 1
        else:
            neg_count += 1
    return pos_count, neg_count


counts = count_positive_negative([10, -4, -6, 40, 50])
print(counts)


# Create a function that takes multiple numbers and returns a string with all unique digits
# Input - 150,240,125,336 -> Output - 1502436
def unique_digits(*numbers):
    unique = []
    for number in numbers:
        for char in str(number):
            if not unique.__contains__(char):
                unique.append(char)
    return "".join(unique)


print(unique_digits(150, 240, 125, 336))


# Create a function that takes a number and returns highest factor other than itself

def highest_factor(number):
    factor = 1
    for i in range(2, number // 2):
        if number % i == 0 and i > factor:
            factor = i
    return factor


print(highest_factor(30))


def highest_factor_v2(number):
    for i in range(number // 2, 1, -1):
        if number % i == 0:
            return i
    else:
        return number


print(highest_factor_v2(29))
print(highest_factor_v2(1))
