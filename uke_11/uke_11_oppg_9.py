import matplotlib.pyplot as plt

stats = {"size":[], "code":[], "x-coords":[], "y-coords":[]}

with open("airport-codes.csv", "r", encoding="utf-8") as file:
    for line in file.read().splitlines()[1:]:
        data = line.replace(", ", ";").split(",")
        stats["size"].append(data[1])
        stats["code"].append(data[9])
        stats["x-coords"].append(float(data[11].strip(" ").split(";")[0].replace('"', "")))
        stats["y-coords"].append(float(data[11].strip(" ").split(";")[1].replace('"', "")))

for i in range(len(stats["size"])):
    if stats["size"][i] == "medium_airport":
        marker = ".c"
    elif stats["size"][i] == "large_airport":
        marker = "oc"
        plt.annotate(stats["code"][i], (stats["y-coords"][i], stats["x-coords"][i]))
    plt.plot(stats["y-coords"][i], stats["x-coords"][i], marker)


plt.savefig("uke_11_oppg_9.png")

plt.show() 

