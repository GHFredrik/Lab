import csv

def sum_of_column(path_in, col_num):
    sum = 0.0
    with open(path_in, "r", encoding="utf-8") as file_in:
        reader = list(csv.reader(file_in))
        for line in reader:
            if 0 <= col_num < len(line):
                data = line[col_num]
                if data.isdecimal():
                    sum += float(data)
    print (sum)
    return (sum)

print("Tester sum_first_col... ", end="")
assert(42.0 == sum_of_column("foo.csv", 0))
assert(95.0 == sum_of_column("foo.csv", 1))
assert(0.0 == sum_of_column("foo.csv", 2))
assert(76363.0 == sum_of_column("Statistikk_Tilsyn_ar.csv", 1))
assert(46007.0 == sum_of_column("Statistikk_Tilsyn_ar.csv", 2))
assert(5024518.0 == sum_of_column("airport-codes.csv", 3))
print("OK")