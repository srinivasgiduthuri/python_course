# Create a program 'table.py' accepting two numbers
# python table.py 15 20
# python table.py 15 [10]
# Default length of the table is 10


import sys

number = 0
length = 10
if len(sys.argv) == 3:
    number = int(sys.argv[1])
    length = int(sys.argv[2])
elif len(sys.argv) == 2:
    number = int(sys.argv[1])
else:
    print("Missing parameter! Requires at least one parameter")

for i in range(1, length + 1):
    print(f"{number:3} X {i:3} = {number * i:5}")
