import matplotlib.pyplot as plt

stats = {"år":[], "tilsyn":[], "reaksjon":[]}

with open("Statistikk_Tilsyn_ar.csv") as file:
    for line in file.read().splitlines()[1:]:
        data = line.split(",")
        stats["år"].append(int(data[0]))
        stats["tilsyn"].append(int(data[1]))
        stats["reaksjon"].append(int(data[2]))


plt.plot(stats["år"], stats["tilsyn"], label="antall tilsyn")
plt.plot(stats["år"], stats["reaksjon"], label="tilsyn med reaksjon")

plt.legend()

plt.savefig("uke_11_oppg_8.png")

plt.show() 

