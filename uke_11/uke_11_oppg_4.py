#A
def simplified_pig_latin(word):
    word_lower = word.lower()
    if word_lower[0] in ["a", "e", "i", "o", "u"]: #If first is vowel
        return (word_lower + "hay")
    else:
        return (word_lower[1:] + word_lower[0] + "ay")

print("Tester simplified_pig_latin... ", end="")
assert("ellohay" == simplified_pig_latin("Hello"))
assert("imagehay" == simplified_pig_latin("Image"))
print("OK")

#B
def sentence_to_simplified_pig_latin(string):
    result = []
    for word in string.split(" "):
        result.append(simplified_pig_latin(word))
    return " ".join(result)

sentence = "My name is Sylvia Lavrans"
expected_value ="ymay amenay ishay ylviasay avranslay"
print("Tester sentence_to_simplified_pig_latin... ", end="")
assert(expected_value == sentence_to_simplified_pig_latin(sentence))
print("OK")