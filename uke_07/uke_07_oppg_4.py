def find_words_in_character_grid(char_grid, words):
    found_words = []
    for i in range(len(char_grid)): #Loop through cols
        for j in range(len(char_grid[i])): #Loop through cells

            for k, word in enumerate(words): #Loop through words

                if word[0] == char_grid[i][j]: #Check if first char = char in wordsearch
                    hor_valid = True
                    for l in range(1, len(word)): #Horizontal search
                        if (j + l == len(char_grid[i])):
                            hor_valid = False
                            break
                        if word[l] != char_grid[i][j + l]:
                            hor_valid = False
                            break
                    if hor_valid:
                        found_words.append(word)
                    
                    vert_valid = True
                    for l in range(1, len(word)): #Vertical search
                        if (i + l == len(char_grid)):
                            vert_valid = False
                            break
                        if word[l] != char_grid[i + l][j]:
                            vert_valid = False
                            break
                    if vert_valid:
                        found_words.append(word)

    return (found_words)

print("Tester find_words_in_character_grid... ", end="")

glossary = ["dikt", "hus", "lese", "by", "elev",
            "smart", "helt", "mål", "yr", "lære"]
char_grid= [
        ['d','s','h','s','s','y'],
        ['l','æ','r','e','s','å'],
        ['k','a','l','a','m','e'],
        ['t','h','e','r','a','q'],
        ['e','t','s','t','r','z'],
        ['e','t','e','r','t','p'],
        ['e','m','å','l','v','w'],
    ]
found_words = find_words_in_character_grid(char_grid, glossary)
assert(sorted(['lese', 'smart', 'mål', 'lære']) == sorted(found_words))
print("OK")

