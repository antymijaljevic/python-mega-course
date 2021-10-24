def mean(*args): #non-keyword agruments, comes as tuple
    print(args)

mean(1,3,4)


def mean(*mul): # can be any name
    print(sum(mul))

mean(1,3,4)


def get_average(*args):
    return sum(args) / len(args)

def sorted_words(*args):
    upper = [item.upper() for item in args]
    upper.sort()
    return upper


# or

def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args) # sorted will always return list type

