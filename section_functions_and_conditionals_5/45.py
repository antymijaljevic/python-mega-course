# one way

def some_func(temp):
    if temp > 25:
        return 'Hot'
    elif temp >= 15 and temp <= 25:
        return 'Warm'
    else:
        return 'Cold'

# another way

def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"

# last test