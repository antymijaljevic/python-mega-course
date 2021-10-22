def mean(value):
    if type(value) == dict: # dict without ''
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

students_grades = {'Marry': 22.1, 'Ante': 11.1, 'Mike':22.56, 'Lovre':32.1}
monday_temps = [22.1, 23.1, 22.9]
print(mean(students_grades))
print(mean(monday_temps))

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")



if x == 1 or y==2:
    print("Yes")
else:
    print("No")


x = 22
y = 22.1

isinstance(x, int) # True
isinstance(y, int) # False



x = -10
if x * 2 > x:
    print("Greater")
else:
    print("Less or Equal")


def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))


if isinstance(x, int) or isinstance(x, float) or x=='1':
    print("Valid type!")
else:
    print("Not valid!")


def some_func(some_string):
    if len(some_string) < 8:
        return False
    else:
        return True
        
some_func('mylongpass')


def warm_cold(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"

warm_cold(11)

