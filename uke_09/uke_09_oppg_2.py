def mase_for_is():
    user_input = ""
    print("Kan jeg få en is?")
    while user_input != "ja":
        user_input = input()
        if user_input != "ja":
            print("Vær så snill, si ja!")
    print("Tusen takk!")

mase_for_is()