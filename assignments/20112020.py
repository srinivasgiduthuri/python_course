# Remove all extra white spaces in a document
import re

try:
    lines_with_no_white_spaces = []
    with open("file_with_extra_white_spaces.txt", "rt") as lines_with_white_spaces_file:
        for line in lines_with_white_spaces_file:
            if len(line.strip()) > 0:
                replace_line = re.sub(r"\s+", " ", line.strip())
                lines_with_no_white_spaces.append(replace_line)
    with open("file_with_no_extra_white_spaces.txt", "wt") as lines_with_no_white_spaces_file:
        for line in lines_with_no_white_spaces:
            lines_with_no_white_spaces_file.write(line + "\n")
except Exception as ex:
    print(ex)
# Read contacts with different delimiters and order
try:
    contacts = []
    with open("contacts.txt", "rt") as contacts_file:
        for line in contacts_file:
            if len(line.strip()) > 0:
                name_match = re.search(r"[a-zA-z]+", line.strip())
                number_match = re.search(r"[0-9]{10}", line.strip())
                if name_match is not None and number_match is not None:
                    print(name_match.group(0) + "\t" + number_match.group(0))
except Exception as ex:
    print(ex)
# Read mobiles with different delimiters
try:
    contacts = set()
    with open("mobiles2.txt", "rt") as mobiles_file:
        for line in mobiles_file:
            if len(line.strip()) > 0:
                number_match = re.findall(r"\d{10}", line.strip())
                for number in number_match:
                    contacts.add(number)
    for number in contacts:
        print(number)
except Exception as ex:
    print(ex)
