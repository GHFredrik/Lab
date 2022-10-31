def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for item in inventory:
        print (f"{inventory[item]} {item}")
        total += inventory[item]
    return total

def add_to_inventory(inventory, loot):
    for item in loot:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = add_to_inventory(inv, dragonLoot)
print(display_inventory(inv))