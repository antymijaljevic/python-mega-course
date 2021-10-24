def area(a, b):
    return a * b


print(area(a=5, b=4)) # keyword agruments


def area(a, b):
    return a * b


print(area(5, 6)) # positional agruments


def area(a, b=7): # default parameters
    return a * b
  
print(area(6))

def area(a=7, b): # non-default argument follows default argument Error
    return a * b
  
print(area(5))