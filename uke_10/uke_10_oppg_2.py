def num_pairwise_diff_gt10(num_list):
    count = 0
    for i in range(len(num_list) - 1):
        if abs(num_list[i] - num_list[i+1]) > 10:
            count += 1
    return count

print("Tester num_pairwise_diff_gt10... ", end="")
a =[9, 3, 12, 0,- 3, 2, -9]  # Forskjellen er større: 12 -> 0 og 2 -> -9
assert(2 == num_pairwise_diff_gt10(a))
a =[10, 2, 12, 0, 1, 2, 11]
assert(1 == num_pairwise_diff_gt10(a))
a= [1, 14, 0, 12, 1, 20, 8]
assert(6 == num_pairwise_diff_gt10(a))
print("OK")
