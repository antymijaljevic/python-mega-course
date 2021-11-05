# runtime errors

a = 1
b = "2"
c = 3

print(int(2.5)) # invalid syntex
print(a + float(b)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(c) # NameError: name 'c' is not defined
print(c/0) # ZeroDivisionError: division by zero