# Print number of uppercase letters, lowercase letters and others
string = "Hello World! Hello Python!"
uppercase_count = 0
lowercase_count = 0
others_count = 0
for char in string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    else:
        others_count += 1
print(f"Uppercase Letters Count - {uppercase_count}")
print(f"Lowercase Letters Count - {lowercase_count}")
print(f"Other Letters Count - {others_count}")
