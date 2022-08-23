name = input("Hva er ditt navn? ")
adress = input("Hva er din adresse? ")
post = input("Hva er ditt postnummer og poststed? ")

print(max(len(name), len(adress), len(post)))