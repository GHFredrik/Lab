def find_longest_words(w1, w2, w3):
    words = [w1, w2, w3]
    maxLength = max(len(w1), len(w2), len(w3))
    for word in words:
        if len(word) == maxLength:
            print (word)

find_longest_words("Game", "Action", "Champion")
find_longest_words("apple", "carrot", "ananas")
find_longest_words("Four", "Five", "Nine")