grades = {"John": 23.1, "Mike": 11.1, "Milka":99.1}

for grade in grades.keys():
    print(grade)

for grade in grades.values():
    print(grade)

for grade in grades.items():
    print(grade)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for num in phone_numbers.values():
    print(num.replace("+", "00"))