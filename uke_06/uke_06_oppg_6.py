def compress(raw_binary):
    compressed = []
    oneOcc = 0
    nullOcc = 0
    if raw_binary[0] == "1":
        compressed.append("0")
    for i, bit in enumerate(raw_binary):
        if bit == "0":
            nullOcc += 1
            if raw_binary[i-1] == "1" and oneOcc != 0:
                compressed.append(str(oneOcc))
                oneOcc = 0
        if bit == "1":
            oneOcc += 1
            if raw_binary[i-1] == "0" and nullOcc != 0:
                compressed.append(str(nullOcc))
                nullOcc = 0
    if oneOcc != 0:
        compressed.append(str(oneOcc))
    if nullOcc != 0:
        compressed.append(str(nullOcc))
    return " ".join(compressed)

print("Tester compress... ", end="")
assert("2 3 4 4" == compress("0011100001111"))
assert("0 2 1 8 1" == compress("110111111110"))
assert("4" == compress("0000"))
print("OK")

def decompress(compBin):
    compBinList = compBin.split(" ")
    decomp = ""
    for i, entry in enumerate(compBinList):
        if i % 2 == 0:
            decomp += int(entry) * "0"
        else:
            decomp += int(entry) * "1"
    return decomp

print("Tester decompress... ", end="")
assert("0011100001111" == decompress("2 3 4 4"))
assert("110111111110" == decompress("0 2 1 8 1"))
assert("0000" == decompress("4"))
print("OK")

