def divide(a, b):
    try:
        return a / b
    except:
        return "Zero division is meaningless"

print(divide(1, 0))
print("End of the program")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return e

print(divide(1, 0))
print("End of the program")