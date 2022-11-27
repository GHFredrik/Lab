import matplotlib.pyplot as plt
from math import sin

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

print (ys_1)
print (ys_2)

plt.minorticks_on()

plt.plot(xs, ys_1, "-.r")
plt.plot(xs, ys_2, "--b")

plt.arrow(5,2,-1.9,-1.9)
plt.text(3.5,2.1,"Første interseksjonen")

# savefig lagrer filene
plt.savefig("uke_11_oppg_7c.png")

# interaktivt vindu
plt.show() 

# Hva skjer om vi ikke har med den raden: plt.show()?
# Du får ikke opp grafikken