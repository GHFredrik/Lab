lines = []
lines.append(input("Første raden: "))
lines.append(input("Andre raden: "))
lines.append(input("Tredje raden: "))

frameWidth = 4 + max(len(lines[0]),len(lines[1]),len(lines[2]))

print("@" * frameWidth)
for i in range(3):
    print("@ " + " " * (frameWidth - 4 - len(lines[i])) + lines[i] + " @")
print("@" * frameWidth)