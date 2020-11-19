# Take a file name from the user and display lines along with line numbers
#
# Marks as follows
# 75
# 80
# 76
# 90
# 85
# 70
# Display marks >= 50
from statistics import mean

with open("marks.txt", "rt") as marks_file:
    for line in marks_file:
        try:
            mark = int(line.strip())
            if mark >= 50:
                print(mark)
        except ValueError:
            print(f"Invalid value {line}")

# Display marks >= average
print("Display marks >= average")
marks = []
with open("marks.txt", "rt") as marks_file:
    for line in marks_file:
        try:
            mark = int(line.strip())
            marks.append(mark)
        except ValueError:
            print(f"Invalid value {line}")
average_marks = mean(marks)
print(f"Average marks - {average_marks}")
for mark in marks:
    if mark >= average_marks:
        print(mark)
# Read a file and remove all the blank lines
lines = []
with open("blank_lines.txt", "rt") as blank_lines:
    for line in blank_lines:
        if len(line.strip()) > 0:
            lines.append(line)
print(lines)
with open("non_blank_lines.txt", "wt") as non_blank_lines:
    for line in lines:
        non_blank_lines.write(line)
# mobiles.txt
# -,-,-,-,-,-,-
# Display mobile numbers in the sorted order
mobiles = set()
try:
    with open("mobiles.txt", "rt") as lines:
        for line in lines:
            parts = line.strip().split(",")
            for mobile in parts:
                if len(mobile) == 10 and mobile.isdigit():
                    mobiles.add(mobile)
    for mobile in sorted(mobiles):
        print(mobile)
except Exception as ex:
    print(ex)
