temps = [22, -9999, 111, -9999, 332, 11]

new_temp = [temp / 2 if temp != -9999 else 0 for temp in temps]

print(new_temp)

def zeros(thelist):
    return [item if item != 'no data' else 0 for item in thelist]


# one way
def convert(thelist):
    result = 0
    for num in [float(item) for item in thelist]:
        result += num
    return result

print(convert(['22.1','18.3','55.8']))

# better way
def foo(lst):
    return sum([float(i) for i in lst])

foo(['22.1','18.3','55.8'])



