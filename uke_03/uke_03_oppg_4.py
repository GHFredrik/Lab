#A
def cross_sum(n):
    sum = 0
    numList = list(str(n))
    for num in numList:
        sum += int(num)
    return sum

#B
def nth_number_with_cross_sum_x(n, x):
    correctTry = 0
    i = 0
    correctList = []
    while correctTry <= n:
        i += 1
        if cross_sum(i) == x:
            correctTry += 1
            correctList.append(i)
    return correctList[n-1]