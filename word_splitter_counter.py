string1 = input("Enter a string of words: ")
print(string1)
string1 = string1.lower()

words = string1.split()
wordCount = list()

for j in range(0, len(words)):
    words[j] = ''.join([i for i in words[j] if i.isalpha()])
    if words[j] != '':
        wordCount.append(words[j])

if len(wordCount) == 1:
    print("There is " + str(len(wordCount)) + " word in your input string")
else:
    print("There are " + str(len(wordCount)) + " words in your input string")