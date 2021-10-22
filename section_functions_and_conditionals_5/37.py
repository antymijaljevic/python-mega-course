def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean


print(mean([1, 5, 3, 2]))

print(type(mean), type(sum))
# <class 'function'> <class 'builtin_function_or_method'>

def calculate_length(lst):
    return len(lst)

def square_area(num):
    return num ** 2
    
print(square_area(7))

def volume_converter(ounces):
    return ounces * 29.57353
    
volume_converter(5)

def sample(x, y):
    print(x, y)
    # return x, y # will return None if return isn't set

print(sample(2, 4))