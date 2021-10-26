"""
    dir(str) # methods
    dir(__builtins__) # built in functions

    python written in C language
"""

import sys # to import module
sys.builtin_module_names # builtins -- for purposes of speed, they're written in C and are directly incorporated into the Python interpreter.

"""
    ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022',
    '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', 
    '_functools', '_heapq', '_imp', '_io', '_json', '_loca '_sha3', '_sha512', '_signal', '_sre', 
    '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', 
    '_weakref', '_winapi', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 
    'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 
    'parser', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')
"""

import time # 1
from time import sleep # or 2
from time import sleep as something # or 3

while True:
    with open("text.txt", "r") as file:
        content = file.read()
        print(content)
    something(5)