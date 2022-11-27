def filter_words(word_list, include, exclude):
    filtered_word_list = []
    for word in word_list:
        valid = True
        for char in include:
            if char not in word:
                valid = False
        for char in exclude:
            if char in word:
                valid = False
        if valid:
            filtered_word_list.append(word)
    return filtered_word_list

print("Tester filter_words... ", end="")
word_list = ["kattepus", "hundevofs", "kosebamse", "kanintuss", "slangesvin"]
must_include = {"a", "s"}
must_exclude = {"m", "v"}
expected_value = ["kattepus", "kanintuss"]
assert(expected_value == filter_words(word_list, must_include, must_exclude))

word_list = ["abc", "abd", "adc", "dbc", "abcx", "abyc", "azbc", "dcba"]
must_include = {"a", "b", "c"}
must_exclude = {"x", "y", "z"}
expected_value = ["abc", "dcba"]
assert(expected_value == filter_words(word_list, must_include, must_exclude))
print("OK")
