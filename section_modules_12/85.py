from time import sleep
import os # written in Python not part of sys.builtin_module_names (C)


while True:
    if os.path.exists("text.txt"):
        with open("text.txt", "r") as file:
            content = file.read()
            print(content)
    else:
        print("File doesn't exist")

    sleep(5)


"""
    import sys
    sys.prefix # to see path of libraries
    'C:\\Users\\antym\\AppData\\Local\\Programs\\Python\\Python39 # windows

"""