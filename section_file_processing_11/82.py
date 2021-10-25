with open("fruits.txt", "x") as file: # will write to new file, if name already don't exist
    file.write()

with open("fruits.txt", "a+") as file: # 'a+' append and read
    file.write("\nnew fruit")
    file.seek(0) # return to beginning
    content = file.read()

print(content)


with open("bear1.txt", "r") as file:
    content = file.read()
    
with open("bear2.txt", "a") as second_file:
    second_file.write(content)

with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\n"+content)
    file.seek(0)
    file.write("\n"+content)
    file.seek(0)
    content = file.read()

print(content)

# or 

with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)
