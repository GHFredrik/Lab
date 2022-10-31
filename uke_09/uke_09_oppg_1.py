def will_work(city, salary):
    city_salary_dict = {
        "Bergen":400000,
        "Bodø":900000,
        "Verdensrommet":0
    }
    will_work = False
    if city in city_salary_dict:
        if city_salary_dict[city] <= salary:
            will_work = True
    else:
        if 600000 <= salary:
            will_work = True
    return will_work

print("Tester will_work...", end="")
assert(will_work('Bergen', 400_000))
assert(not will_work('Bergen', 399_999))
assert(not will_work('Kristiansand', 590_000))
assert(will_work('Bodø', 900_000))
assert(will_work('Tromsø', 600_000))
assert(not will_work('Bodø', 899_999))
assert(will_work('Verdensrommet', 10))
print("OK")
