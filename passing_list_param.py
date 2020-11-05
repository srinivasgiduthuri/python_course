def prepend(lst, value):
    lst.insert(0, value)


def empty_using_clear(lst):
    print('In Before Empty Clear', id(lst))
    lst.clear()
    print('In After Empty Clear', id(lst))


def empty_using_assignment(lst):
    print('In Before Empty Assignment', id(lst))
    lst = [1]
    print('In After Empty Assignment', id(lst))
    print(lst)


nums = [1, 2, 3]
print('Before Prepend', id(nums))
prepend(nums, 10)
print('After Prepend', id(nums))
print(nums)
print('Before Empty Clear', id(nums))
empty_using_clear(nums)
print('After Empty Clear', id(nums))
print(nums)
print('Before Empty Assignment', id(nums))
empty_using_assignment(nums)
print('After Empty Assignment', id(nums))
print(nums)
