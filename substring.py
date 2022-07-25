
word = "TheWordInQuestion"
length = 1
largest = 1
for i in range(len(word)):
    hmap = {}
    hmap[i] = True
    for j in range(i + 1, len(word)):
        if word[j] in hmap:
            break
        hmap[word[j]] = True
        length = length + 1



