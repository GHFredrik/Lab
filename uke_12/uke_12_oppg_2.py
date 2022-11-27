def first_letter_last_word(path_in):
    letter_string = ""
    with open(path_in, "r", encoding="utf-8") as file_in:
        for line in file_in.read().splitlines():
            letter_string += line.split(" ")[-1][0]
    return letter_string

print("Tester first_letter_last_word... ", end="")
assert("vlf" == first_letter_last_word("askeladden.txt"))
# Forklaring:
# Siste ord i første linje er 'vanns.'   Første bokstav i dette ordet er 'v'
# Siste ord i andre linje er 'landet.'   Første bokstav i dette ordet er 'l'
# Siste ord i tredje linje er 'fleste.'  Første bokstav i dette ordet er 'f'
print("OK")
