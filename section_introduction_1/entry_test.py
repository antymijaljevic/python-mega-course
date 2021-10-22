#What's the output of the code below?

mylist = [['abc'], ['def', 'ghi']]
mylist[-1][-1][-1]

#'i'


# What does the code below output?

def eur_to_usd(euros, rate=0.8):
    return euros * rate
print(eur_to_usd(10))

#8.0 mixed with float

# What would be the output of the following code if the user entered 10 as input?

weight = input("How many kg?")
price = weight * 2.5
print(price)

# must be float to return 25, so error


# What would be the value of y given the following code?

y = [i * 2 if i > 0 else 0 for i in [1, -2, 10]]

# [2, 0, 20] same as:

y = []

for i in [1, -2, 10]:
    if i > 0:
        y.append(i * 2)
    else:
        y.append(0)



# What would the output of the following code be?

def foo(*args):
    return len(args) # sees tuple as len(0)
print(foo(1, 2, 4))

"""
 3, because

*args is a special parameter. It means the function can practically take an infinite number of arguments. 
The arguments will be added to the args tuple. The above function returns the length of that tuple. 
The length is three since three arguments were passed in the function call.
"""

