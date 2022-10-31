from pathlib import Path

#A
def shopping_list_to_dict(shopping_list_str):
    shopping_list_dict = {}
    shopping_list_split = shopping_list_str.split("\n")[:-1]
    for entry in shopping_list_split:
        shopping_list_dict[entry.split(" ")[1]] = int(entry.split(" ")[0])
    return (shopping_list_dict)

print("Tester shopping_list_to_dict... ", end="")
shopping_list_as_string = """\
2 brød
3 pizza
10 poteter
1 kaffe
1 ost
14 epler
"""
shopping_list_as_dict = shopping_list_to_dict(shopping_list_as_string)
assert({
    "brød": 2,
    "pizza": 3,
    "poteter": 10,
    "kaffe": 1,
    "ost": 1,
    "epler": 14,
} == shopping_list_as_dict)
print("OK")

#B
def shopping_list_file_to_dict(path):
    return shopping_list_to_dict(Path(path).read_text(encoding="utf-8"))

print("Tester shopping_list_file_to_dict... ", end="")
shopping_list_as_dict = shopping_list_file_to_dict("handleliste.txt")
assert({
    "brød": 2,
    "pizza": 3,
    "poteter": 10,
    "kaffe": 1,
    "ost": 1,
    "epler": 13,
} == shopping_list_as_dict)
print("OK")