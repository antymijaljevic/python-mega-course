
import datetime

while True:
    user_input = input("Name? ")
    if user_input == 'Ante':
        break
    else:
        continue


while True:
    name = input("Name? ")
    surname = input("Surname? ")

    if name == "" or surname == "":
        print("Full name missing ...")
        continue

    if name == 'Ante' and surname == "Mijaljevic":
        break



while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")