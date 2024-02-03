distance_dict = {
    # 'distance': 130,
    'speed': 100,
    'time': 1.3,
}


# A function is created to which the dictionary is passed
# If dict has 'distance' and its value is an integer, print the string...
# Else if dict has 'speed' and 'time' as value, print the string...
# Else print the string...
def route_info(**kwargs):  # A function that gets a different set of arguments.
    if kwargs.get('distance'):  # The presence of the Distance key in the dictionary is checked.
        return f"Distance to your destination is {kwargs.get('distance')} km."

    # The presence of the "speed" and "time" key in the dictionary is checked.
    if type(kwargs.get('speed')) and type(kwargs.get('time')):
        speed = kwargs.get('speed')
        time = kwargs.get('time')
        return f"Distance to your destination is {round(speed * time)} km."

    return f"No distance info is avalible."


print(route_info(**distance_dict))

# ===================================================================================

my_num = 25
if my_num >= 0:
    print('is positive number')

info_person = {
    'age': 29,
    'Name': 'Bazhen'
}

if not info_person.get('Name'):
    print('Name is missing.')
else:
    print(f"Person {info_person['Name']} is {info_person['age']} years old")
# =================================================================================

my_number = 25

if type(my_number) is int:
    print(f'{my_number} is Integer.')
else:
    print(f"{my_number} is not an Integer.")

# ==================================================================================

my_phone = {
    'price': 200,
}

if my_phone.get('brand'):
    print(f"Phone's brand is {my_phone['brand']}")
else:
    print(f"There is no phone Brand.")

# ===================================================================================

another_num = -10

if another_num > 0:
    print(f"{another_num} is posotive.")
elif another_num < 0:
    print(f"{another_num} is negative.")
else:
    print(f"{another_num} is zero")

# ===================================================================================