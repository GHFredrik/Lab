from datetime import *

def first_friday_13th_after(date):
    next_friday_13th = None
    y = date.year
    m = date.month
    d = 13
    if date.day >= 13: #If 13th or more, check from next month
        m += 1
    while not next_friday_13th:
        if datetime(y, m, d).weekday() == 4:
            next_friday_13th = datetime(y, m, d)
        else:
            if m == 12: #if at twelth month, increment year and reset month
                y += 1
                m = 1
            else: #Increment month
                m += 1
    return next_friday_13th

print("Tester first_friday_13th_after... ", end="")
# Test 1
result = first_friday_13th_after(datetime(2022, 10, 24))
assert((2023, 1, 13) == (result.year, result.month, result.day))
# Test 2
result = first_friday_13th_after(datetime(2023, 1, 13))
assert((2023, 10, 13) == (result.year, result.month, result.day))
# Test 3
result = first_friday_13th_after(datetime(1950, 1, 1))
assert((1950, 1, 13) == (result.year, result.month, result.day))
print("OK")
