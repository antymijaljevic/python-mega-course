name = input("What is your name? ")
surname = input("What is your surname? ")
when = 'today'

message = "Hello %s %s" % (name, surname)

message = f"Hey, Hello {name} {surname}, What's up {when}."

print(message)

def greeting(name):
    return "Hi %s" % name

def greet(name):
    return "Hi %s" % name.title()