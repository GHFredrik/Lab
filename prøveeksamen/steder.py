#A

def gen_adm_dict(path_in):
    adm_dict = {}
    with open(path_in, "r", encoding="utf-8") as file_in:
        for line in file_in.read().splitlines():
            data = line.split(";")
            adm_dict[data[1]] = {
                "latitude": data[3],
                "longitude": data[4],
                "feature code": data[5],
                "admin1 code":data[7],
                "population":data[9]
                }
    return adm_dict

def get_adm_code(place):
    adm_dict = gen_adm_dict("NO_ADM12.csv")
    return adm_dict[place]["admin1 code"]

def get_county_from_adm_code(adm_code):
    adm_dict = gen_adm_dict("NO_ADM12.csv")
    for key in adm_dict:
        if adm_dict[key]["admin1 code"] == adm_code and adm_dict[key]["feature code"] == "ADM1":
            return key

def get_places_from_adm_code(adm_code):
    adm_dict = gen_adm_dict("NO_ADM12.csv")
    within_county = []
    for key in adm_dict:
        if adm_dict[key]["admin1 code"] == adm_code and adm_dict[key]["feature code"] == "ADM2":
            within_county.append(key)
    return within_county

#B

def print_county(county):
    adm_dict = gen_adm_dict("NO_ADM12.csv")
    if county in adm_dict:
        places = get_places_from_adm_code(adm_dict[county]["admin1 code"])
        largest = places[0]
        smallest = places[0]
        northmost = places[0]
        southmost = places[0]
        for key in places:
            place = adm_dict[key]
            if int(place["population"]) > int(adm_dict[largest]["population"]):
                largest = key
            elif int(place["population"]) < int(adm_dict[smallest]["population"]):
                smallest = key

            if float(place["latitude"]) > float(adm_dict[northmost]["latitude"]):
                northmost = key
            elif float(place["latitude"]) < float(adm_dict[southmost]["latitude"]):
                southmost = key

        #Formatting
        largest_num = adm_dict[largest]['population']
        smallest_num = adm_dict[smallest]['population']
        northmost_num = adm_dict[northmost]['latitude']
        southmost_num = adm_dict[southmost]['latitude']
        spacing = 2 * max(
            len(county),
            len(largest),
            len(smallest),
            len(northmost),
            len(southmost),
            len(largest_num),
            len(smallest_num),
            len(northmost_num),
            len(southmost_num)
            )
        print(f"{spacing*'='}\n{county}\n{spacing*'='}")
        print(f"{largest}{(spacing - len(largest) - len(largest_num))*' '}{largest_num}")
        print(f"{smallest}{(spacing - len(smallest) - len(smallest_num))*' '}{smallest_num}")
        print(f"{northmost}{(spacing - len(northmost) - len(northmost_num))*' '}{northmost_num}")
        print(f"{southmost}{(spacing - len(southmost) - len(southmost_num))*' '}{southmost_num}")
        print(spacing*'=')
        return True
    else:
        return False

# print(get_adm_code("Oppegård"))
# print(get_county_from_adm_code("01"))
# print(get_places_from_adm_code("01"))
# print(print_county("Akershus fylke"))

#C

def main():
    while True:
        user_input = input("Which county (q to quit)? ")
        if user_input == "q":
            print ("Bye!")
            return
        if not (print_county(user_input)):
            print("No matching county found. Try Again.")
        
main()