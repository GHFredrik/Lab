def add_numbers():
    total = 0
    while True:
        user_input = input("Give me an integer (q to quit):")
        if user_input.lstrip("+-").isdigit():
            total += int(user_input)
        elif user_input == "q":
            print (f"The sum is {total}.")
            break
        else:
            print("That was not an integer. Please try again.")

add_numbers()