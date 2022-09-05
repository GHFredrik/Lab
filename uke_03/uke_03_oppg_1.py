def multiples_of_seven_up_to(n):
    for i in range(1, n):
        if i % 7 == 0:
            print(str(i))