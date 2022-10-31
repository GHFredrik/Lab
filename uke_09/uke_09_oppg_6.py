#A
def key_value_getter(d):
    #Print keys
    print("Dictionary keys:")
    for key in d.keys():
        print (key)

    #Print values
    print("\nDictionary values:")
    for key in d.keys():
        print (d[key])

    #Print keys/values
    print("\nDictionary keys/value:")
    for key in d.keys():
        print (f"{key} {d[key]}")

key_value_getter({
  "monday": 0,
  "tuesday": 0.7,
  "wednesday": 0,
  "thursday": 4.7,
  "friday": 10
})

#B
def index_value_getter(a):
    #Print indices
    print("\nList indices:")
    for i in range(len(a)):
        print (i)

    #Print values
    print("\nList values:")
    for entry in a:
        print (entry)

    #Print indices/values
    print("\nList indices/value:")
    for i, entry in enumerate(a):
        print (f"{i} {entry}")

index_value_getter([7.0, 8.0, 10.0, 9.0, 10.0])
