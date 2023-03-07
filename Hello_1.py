import random

name = input("What is your name? ")

def random_greeting ():
    greeting = [
        f"Hello,{name}",
        f"gamarjoba, {name}",
        f"salami, {name}",
        f"hallo", {name}

    ]

    print(greeting[
        random.randint(0, len(greeting)-1)
    ])

random_greeting()

