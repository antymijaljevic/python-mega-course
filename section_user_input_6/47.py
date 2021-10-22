def weather_condition(temp):
    if temp > 7:
        return 'Warm'
    else:
        return 'Cold'


user_input = float(input("Enter temperature: "))
# print(user_input.upper())
# type(user_input)

print(weather_condition(user_input))