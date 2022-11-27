def spise_sammen():
    menu = ["Stekt uer med blomkålpuré", "Piggvarfilet med ertepuré", "Boknatorsk med kremstuede", "Steinbit, sjøkreps og snøkrabbe", "Norske oster med marmelade"]
    print(f"Meny\n\n1. {menu[0]}.\n2. {menu[1]}.\n3. {menu[2]}.\n4. {menu[3]}.\n5. {menu[4]}.\n")
    order = input("Hvilket nummer vil du bestille? ")
    if order.isdigit() and 0 <= int(order)-1 <= len(menu):
        print(f"{menu[int(order)-1]} kommer straks!")
    else:
        print("Beklager, det er ikke et gyldig valg!")

spise_sammen()