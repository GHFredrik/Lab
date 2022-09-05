def dummy_chatbot():
    while True:
        print("Hi! Do you want to talk to me?")
        if input() == "no":
            print("All right, bye!")
            return
        else:
            print("That's cool!")

dummy_chatbot()
