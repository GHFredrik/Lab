lines = []
lines.append(input("Første rad: "))
lines.append(input("Andre rad: "))
lines.append(input("Tredje rad: "))

frameWidth = 4 + max(len(lines[0]),len(lines[1]),len(lines[2]))

print("@" * frameWidth)
for i in range(3):
    print("@ " + " " * (frameWidth - 4 - len(lines[i])) + lines[i] + " @")
print("@" * frameWidth)