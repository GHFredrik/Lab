folder = ""

def students_who_passed(path):
    file = open(folder + path, "r")
    passedList = []
    fileSplit = []
    for line in file:
        fileSplit.append(line.rstrip("\n").split(";"))
    for i in range(1, len(fileSplit)):
        passed = True
        if fileSplit[i][13:].count("B") < 4: #Quizzer
            passed = False

        if fileSplit[i][2:13].count("B") < 6: #6 av 11 labber
            if fileSplit[i][1] != "B": #Kartlegging
                passed = False
        
        if fileSplit[i][8:13].count("B") < 3: #3 av 5 siste labber
            passed = False

        if passed:
            passedList.append(fileSplit[i][0])
    return(passedList)

print("Tester students_who_passed... ", end="")
assert(['abc101', 'abc103', 'abc105', 'abc109', 'abc111', 'abc113'] 
        == students_who_passed("course_data.csv"))
print("OK")
