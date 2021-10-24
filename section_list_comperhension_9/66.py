temps = [22, -9999, 111, -9999, 332, 11]

new_temp = [temp / 2 for temp in temps if temp != -9999]

new_temp = [temp / 2 if temp != -9999 else 0 for temp in temps]

print(new_temp)


def only_num(thelist):
    return [item for item in thelist if type(item) == int]

only_num([22.1, 22, 11, 'fuck'])

def only_positive(numbers):
    return [num for num in numbers if num > 0]

only_positive([-1, 200, -22])