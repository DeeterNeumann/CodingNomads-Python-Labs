# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "


sentence = word[1:3] + word[8:] + word[-2:-7:-2] + word[8:] + word[0] + word[6] + word[2:4] + word[7]
print(sentence)