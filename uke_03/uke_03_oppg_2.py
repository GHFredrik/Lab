def multiplication_table(n):
    for i in range(1, n+1):
        result = str(i) + ": "
        for j in range(1, n+1):
            result += str(i * j) + " "
        print(result)