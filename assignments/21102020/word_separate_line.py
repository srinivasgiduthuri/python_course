# Print each word on a separate line
string = "Hello World! Hello Python!"
split_string = string.split(sep=" ")
for split_part in split_string:
    print(split_part)
for char in string:
    if char == ' ':
        print()
    else:
        print(char, end="")
