#A
def good_style(src):
    srcSplit = src.split("\n")
    for l in srcSplit:
        if (len(l) > 79):
            return False
    return True

# print("Tester good_style... ", end="")
# assert(good_style("""\
# def distance(x0, y0, x1, y1):
#     return ((x0 - x1)**2 + (y0 - y1)**2)**0.5
# """))
# assert(good_style((("x" * 79) + "\n") * 20))
# assert(not good_style((("x" * 79) + "\n") * 5 +
#                       (("x" * 80) + "\n")     +
#                       (("x" * 79) + "\n") * 5))
# print("OK")

#B
folder = ""

def good_style_from_file(fileSrc):
    src = open(folder + fileSrc, "r")
    for l in src:
        if (len(l) > 79):
            return False
    return True

# print("Tester good_style_from_file... ", end="")
# assert(good_style_from_file("test_file1.py"))
# assert(not good_style_from_file("test_file2.py"))
# assert(not good_style_from_file("test_file3.py"))
# assert(good_style_from_file("uke_04_oppg_4.py"))
# print("OK")