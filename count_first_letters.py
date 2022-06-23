
word_file_path = "DATA/words.txt"

letter_counts = {}
target = 's'
count = 0
with open(word_file_path) as words_in:
    for word in words_in:
        letter = word[0]  # first letter in word
        if letter == target:
            count += 1
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

print("letter_counts: {}".format(letter_counts))
print(f"{count} words start with {target}")
