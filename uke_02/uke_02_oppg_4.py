def find_first_longest_word(w1, w2, w3):
    words = [w1, w2, w3]
    maxLength = max(len(w1), len(w2), len(w3))
    for word in words:
        if len(word) == maxLength:
            print (word)
            break

find_first_longest_word("Game", "Action", "Champion")
find_first_longest_word("apple", "carrot", "ananas")
find_first_longest_word("Four", "Five", "Nine")