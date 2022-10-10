def find_most_likely_answer():
    question = input()
    input_len = int(input()[0])
    answer_options_list = []
    for i in range(input_len):
        answer_options_list.append((input().split(", ")))

    most_common = [] #Get most common
    for i in range(len(answer_options_list[0])):
        test = []
        for j in range(input_len):
            test.append(answer_options_list[j][i])
        most_common.append(max(set(test), key = test.count))
    print (most_common)

    diff_list = [] #Find diff from most common
    for i in range(input_len):
        diff = 0
        for j in range(len(answer_options_list[0])):
            if answer_options_list[i][j] != most_common[j]:
                diff += 1
        diff_list.append(diff)
    print (diff_list)

    for i in range(input_len):
        if diff_list[i] == min(diff_list):
            print(", ".join(answer_options_list[i]))

find_most_likely_answer()