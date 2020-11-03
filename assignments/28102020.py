# Count the characters in the sentence using dictionary data structure
sentence = "How do you do"
char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] = char_freq[char] + 1
    else:
        char_freq[char] = 1
print(char_freq)
# Check whether the list can be modifiable inside a tuple
list_tuple = (1, [10, 20])
number, number_list = list_tuple
number_list.append(30)
print(list_tuple)
# Convert a dictionary into a list of tuples
char_freq_tuples_list = []
for char, freq in char_freq.items():
    char_freq_tuples_list.append((char, freq))
print(char_freq_tuples_list)
