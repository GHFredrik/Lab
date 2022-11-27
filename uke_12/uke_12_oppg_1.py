def filter_high_temperatures(path_in, path_out, threshold):
    with open(path_in, "r", encoding="utf-8") as file_in:
        with open(path_out, "w", encoding="utf-8") as file_out:
            for line in file_in.read().splitlines():
                if float(line.split(" ")[1]) >= threshold:
                    file_out.write(f"{line}\n")
            
# print("Tester filter_high_temperatures... ", end="")
# filter_high_temperatures("temperatures.txt", "high_temps.txt", 23.5)
# expected_result = """\
# Monday 23.5
# Wednesday 24.0
# Thursday 23.9
# Sunday 23.9
# """
# with open("high_temps.txt", "rt", encoding='utf-8') as f: 
#     actual_result = f.read()
# assert(expected_result == actual_result)
# print("OK")

filter_high_temperatures("temperatures.txt", "high_temps.txt", 23.5)
