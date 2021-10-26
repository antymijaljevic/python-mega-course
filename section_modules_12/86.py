from time import sleep
from os import path
import pandas


while True:
    if path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File doesn't exist")

    sleep(5)


"""
    Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

    Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

    Packages are a collection of .py modules.

    Third-party libraries are packages or modules written by third-party persons (not the Python core development team).
"""