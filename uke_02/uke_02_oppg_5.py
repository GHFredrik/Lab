def wavelength_to_color(waveLength):
    dict = [
    {"color": "Violet", "min":380, "max":450},
    {"color": "Blue", "min":450, "max":485},
    {"color": "Cyan", "min":485, "max":500},
    {"color": "Green", "min":500, "max":565},
    {"color": "Yellow", "min":565, "max":590},
    {"color": "Orange", "min":590, "max":625},
    {"color": "Red", "min":625, "max":750},
    ]

    for entry in dict:
        if entry["min"] < waveLength <= entry["max"]:
            return entry["color"]

def frequency_to_color(frequency):
    waveLength = (3e8 / (frequency*10**12)) * 1e9
    return(wavelength_to_color(waveLength))

def frequency_or_wavelength_to_color():
    unit = input("Enter a unit (nm or THz):")
    if unit == "nm":
        value = int(input("Enter a value in nm:"))
        result = wavelength_to_color(value)
        if result:
            print("\n" + result)
        else:
            print("\nThere is no color with wavelength " + str(value) + " nm")
        return
    if unit == "THz":
        value = int(input("Enter a value in THz:"))
        result = frequency_to_color(value)
        if result:
            print("\n" + result)
        else:
            print("\nThere is no color with frequency " + str(value) + " THz")
        return
    else:
        print("The unit must be either nm or THz, it can not be " + unit)
        return

frequency_or_wavelength_to_color()