# Create a function that takes a number and returns smallest factor other than itself
def lowest_factor_v2(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return i
    else:
        return number


print(lowest_factor_v2(29))
print(lowest_factor_v2(1))
print(lowest_factor_v2(9))
print(lowest_factor_v2(30))
