def read_and_sort():
    inputList = []
    while True:
        userInput = int(input())
        if userInput == 0:
            for num in sorted(inputList):
                print(str(num))
            return
        inputList.append(userInput)

read_and_sort()