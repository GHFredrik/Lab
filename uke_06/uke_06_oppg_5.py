import io

#A

def can_be_made_of_letters(word, letters):
    for char in word:
        if char not in letters:
            if "*" not in letters:
                return False
            else:
                letters = letters.replace("*", "", 1)
        else:
            letters = letters.replace(char, "", 1)
    return True

print("Tester can_be_made_of_letters... ", end="")
assert(can_be_made_of_letters("emoji", "abcdefghijklmno"))
assert(not can_be_made_of_letters("smilefjes", "abcdefghijklmnopqrs"))
assert(can_be_made_of_letters("smilefjes", "abcdeeefghijklmnopqrsss"))
assert(can_be_made_of_letters("lese", "esel"))

# Ekstra tester for mer avansert variant, med wildcard * i bokstavene
assert(can_be_made_of_letters("lese", "ese*"))
assert(not can_be_made_of_letters("lese", "esxz*"))
assert(can_be_made_of_letters("smilefjes", "s*i*e*j*s"))
assert(not can_be_made_of_letters("smilefjes", "s*i*e*j*z"))
print("OK")

#B

def possible_words(wordList, letters):
    possible_words = []
    for word in wordList:
        if can_be_made_of_letters(word, letters):
            possible_words.append(word)
    return possible_words

print("Tester possible_words... ", end="")
hundsk =["tur", "mat", "kos", "hent", "sitt", "dekk", "voff"]
kattsk =["kos", "mat", "pus", "mus", "purr", "mjau", "hiss"]

assert(['kos', 'sitt'] == possible_words(hundsk, "fikmopsttuv"))
assert(['kos', 'pus', 'mus'] == possible_words(kattsk, "fikmopsttuv"))

# Ekstra tester for mer avansert variant, med wildcard * i bokstavene
assert(['tur', 'mat', 'kos', 'sitt'] == possible_words(hundsk, "fikmopsttu*"))
assert(['kos', 'mat', 'pus', 'mus'] == possible_words(kattsk, "fikmopsttu*"))
print("OK")

#C

folder = ""

def possible_words_from_file(path, letters):
    wordList = []
    file = io.open(folder + path, mode = "r", encoding = "utf-8")
    for line in file:
        wordList.append(line.rstrip("\n"))
    return possible_words(wordList,letters)

print("Tester possible_words_from_file... ", end="")
assert(['du', 'dun', 'hu', 'hud', 'hun', 'hund', 'nu', 'uh']
        == possible_words_from_file("nsf2022.txt", "hund"))

# Ekstra test for varianten hvor det er wildcard i bokstavene
assert(['a', 'cd', 'cv', 'e', 'i', 'pc', 'wc', 'æ', 'å']
        == possible_words_from_file("nsf2022.txt", "c*"))
print("OK")
