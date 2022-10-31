def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for item in inventory:
        print (f"{inventory[item]} {item}")
        total += inventory[item]
    return total

stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
print(display_inventory(stuff))