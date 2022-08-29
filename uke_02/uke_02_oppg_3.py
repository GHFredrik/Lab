def human_to_dog_years(years):
    if years >= 2:
        return ((2*10.5) + ((years-2)*4))
    else:
        return (years*10.5)

print(human_to_dog_years(1.5))
print(human_to_dog_years(2))
print(human_to_dog_years(11))
