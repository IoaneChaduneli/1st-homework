import random

name = input("What is your name? ")

def random_greeting():
    greeting = [
        f"Hello,{name}",
        f"gamarjoba, {name}",
        f"salami, {name}",
        f"hallo, {name}",

    ]

    greet = greeting[random.randint(0, len(greeting)-1)]


    print(greet)

random_greeting()

