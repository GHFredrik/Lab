def people_with_age(path, age):
    file = open(path, "r", encoding="utf-8")
    file_listed = file.read().splitlines()
    file.close()
    people_with_age = set()
    for entry in file_listed:
        entry = entry.split(" ")
        if int(entry[1]) == age:
            people_with_age.add(entry[0])
    return people_with_age

print("Tester people_with_age... ", end="")
assert(people_with_age('namesages.txt', 18) == {'Odin', 'Trym'})
assert(people_with_age('namesages.txt', 19) == {'Brage', 'Embla', 'Idun',
                                                'Astrid', 'Gro'})
assert(people_with_age('namesages.txt', 20) == {'Alf', 'Frøya', 'Edda'})
assert(people_with_age('namesages.txt', 21) == {'Thor'})
assert(people_with_age('namesages.txt', 22) == {'Geir'})
assert(people_with_age('namesages.txt', 23) == set())
print("OK")