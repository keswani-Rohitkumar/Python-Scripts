from collections import Counter, OrderedDict

word1 = "cabbba"
word2 = "abbccc"

#Incomlete need to change the logic

word1 = sorted(word1)
word2 = sorted(word2)

w1 = Counter(word1)
w2 = Counter(word2)

if w1 == w2 :
    print(True)
else:
    print(False)

# expected True