#A
def at_least_two(word, char):
    if list(word).count(char) >= 2:
        return True
    else:
        return False

print("Tester at_least_two... ", end="")
assert(at_least_two('assessment', 's'))
assert(at_least_two('eksamen', 'e'))
assert(not at_least_two('gradering', 'd'))
assert(at_least_two('grunnleggende', 'e'))
assert(not at_least_two('midterm', 'x'))
print("OK")

#B
def at_least_two_in_list(word_list, char):
    count = 0
    for word in word_list:
        if at_least_two(word, char):
            count += 1
    return count

print("Tester at_least_two_in_list... ", end="")
words = ['exam', 'christmas', 'assessment', 'test', 'paper', 'class']
assert(3 == at_least_two_in_list(words, 's'))
assert(1 == at_least_two_in_list(words, 'e'))
assert(0 == at_least_two_in_list(words, 'a'))
print("OK")

#C
def at_least_two_in_file(path, char):
    file = open(path, "r")
    word_list = file.read().splitlines()
    file.close()
    return at_least_two_in_list(word_list, char)

print("Tester at_least_two_in_file... ", end="")
assert(4==at_least_two_in_file('wordlist.txt', 's'))
assert(1==at_least_two_in_file('wordlist.txt', 'e'))
assert(0==at_least_two_in_file('wordlist.txt', 'a'))
print("OK")
