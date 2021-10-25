with open("fruits.txt") as file: # close method will be applied automaticlly 
    content = file.read()

# print(file.read()) # as you see file is closed

print(content)