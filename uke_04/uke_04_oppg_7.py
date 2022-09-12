#A
def get_impact(line):
    lineSplit = line.split(";")
    return float(lineSplit[2])

# print("Tester get_impact... ", end="")
# assert(1.43 == get_impact("nc72666881;California;1.43;2016-07-27 00:19:43"))
# assert(4.9 == get_impact("us20006i0y;Burma;4.9;2016-07-27 00:20:28"))
# print("OK")

#B
def filter_earthquakes(src, threshhold):
    result = []
    srcSplit = src.split("\n")
    for line in srcSplit[1:-1]:
        if get_impact(line) > threshhold:
            result.append("".join(line) + "\n")
    return (srcSplit[0] + "\n" + "".join(result))

# print("Tester filter_earthquakes... ", end="")
# assert("""\
# id;location;impact;time
# nc72666881;California;1.43;2016-07-27 00:19:43
# us20006i0y;Burma;4.9;2016-07-27 00:20:28
# """ == filter_earthquakes("""\
# id;location;impact;time
# nc72666881;California;1.43;2016-07-27 00:19:43
# us20006i0y;Burma;4.9;2016-07-27 00:20:28
# nc72666891;California;0.06;2016-07-27 00:31:37
# """, 1.1))
# assert("""\
# id;location;impact;time
# us20006i0y;Burma;4.9;2016-07-27 00:20:28
# """ == filter_earthquakes("""\
# id;location;impact;time
# nc72666881;California;1.43;2016-07-27 00:19:43
# us20006i0y;Burma;4.9;2016-07-27 00:20:28
# nc72666891;California;0.06;2016-07-27 00:31:37
# """, 3.0))
# assert("""\
# id;location;impact;time
# """ == filter_earthquakes("""\
# id;location;impact;time
# nc72666881;California;1.43;2016-07-27 00:19:43
# us20006i0y;Burma;4.9;2016-07-27 00:20:28
# nc72666891;California;0.06;2016-07-27 00:31:37
# """, 5.0))
# print("OK")

#C
folder = ""

def filter_earthquakes_file(srcFile, targetFile, threshhold):
    result = []
    src = open(folder + srcFile, "r")
    target = open(folder + targetFile, "w")
    lines = src.readlines()
    for line in lines[1:-1]:
        if get_impact(line) > threshhold:
            result.append("".join(line))
    target.write(lines[0] + "".join(result))

filter_earthquakes_file("earthquakes_simple.csv", "earthquakes_above_7.csv", 7.0)