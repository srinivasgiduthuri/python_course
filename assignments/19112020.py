# Accept two files from user and display common lines between files
try:
    with open("names_1.txt", "rt") as names1_lines, open("names_2.txt", "rt") as names2_lines:
        names1 = set()
        names2 = set()
        for name in names1_lines:
            names1.add(name.strip())
        for name in names2_lines:
            names2.add(name.strip())
        print(names1.intersection(names2))
except Exception as ex:
    print(ex)
# Accept a file and display the word frequency of the file
try:
    with open("words.txt", "rt") as words_lines:
        word_map = {}
        for line in words_lines:
            for word in line.upper().split():
                if word in word_map:
                    word_map[word] += 1
                else:
                    word_map[word] = 1
        print(word_map)
except Exception as ex:
    print(ex)
