def mean(**kwargs): # keyword agruments
    return kwargs

print(mean(a=1, b=2, c=3)) # you get dictionary


def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=3, b=3, c=3))

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 15, Kae = 34))


def report(*args):
    print("REPORT: "+args[0]+" coins\n"+args[1]+" Token")


report("1000", "ADA")