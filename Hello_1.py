import random

name = input("What is your name? ")

def random_greeting():
    hello = [
        f"Hello,{name}",
        f"gamarjoba, {name}",
        f"salami, {name}",
        f"hallo, {name}",

    ]

    greet =hello[random.randint(0, len(hello)-1)]


    print(greet)

random_greeting()

