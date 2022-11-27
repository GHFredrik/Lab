#A
def sub_course_positions(path):
    pos = {"forward":0, "depth":0}
    with open(path, "r", encoding="utf-8") as file:
        for line in file.read().splitlines():
            instruction = line.split(" ")
            if instruction[0] == "forward":
                pos["forward"] += int(instruction[1])
            elif instruction[0] == "down":
                pos["depth"] += int(instruction[1])
            elif instruction[0] == "up":
                pos["depth"] -= int(instruction[1])
    return pos

print("Tester sub_course_positions... ", end="")
result = sub_course_positions("sub-path-sample.txt")
assert({'forward': 15, 'depth': 10} == result)
print("OK")

#B
def sub_course(path):
    pos = sub_course_positions(path)
    return (pos["forward"] * pos["depth"])

print("Tester sub_course... ", end="")
assert(150 == sub_course("sub-path-sample.txt"))
print("OK")
