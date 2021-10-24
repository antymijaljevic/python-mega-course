# without list comperhension

temps = [22, 111, 332, 11]
new_temps = []

for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)



# with
new_co_list = [temp / 10 for temp in temps]

print(new_co_list)