    # 'r'       open for reading (default)
    # 'w'       open for writing, truncating the file first
    # 'x'       create a new file and open it for writing
    # 'a'       open for writing, appending to the end of the file if it exists
    # 'b'       binary mode
    # 't'       text mode (default)

with open("fruits.txt") as file: # default is read
    content = file.read()

print(content)

with open("fruits.txt", "r") as file: # better for readability 
    content = file.read()

print(content)


with open("new_file.txt", "w") as file: # create a new file and write
    file.write("Hello World\nI am here")
    file.write("Something new") # can apply more write methods

with open('new_file.txt') as file:
    content = file.read()
    
task = ''
for ch in range(0,90):
    task += content[ch]

print(task)

# or

file = open("new_file.txt")
content = file.read()
file.close()
print(content[:90])


def get(string, path):
    
    with open(path) as file:
        content = file.read()
    
    counter = 0
    for ch in content:
        if ch == string:
            counter += 1
        
    return counter


print(get('I', 'new_file.txt'))


# or simple

def foo(character, filepath="new_file.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

print(foo('beast'))

"Hi there".count('e')

with open('file.txt', 'w') as file:
    file.write('snail')


with open("bear.txt") as file:
    content = file.read()
    content = content[:90]
    
with open("first.txt", "w") as new_file:
    new_file.write(content)