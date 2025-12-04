import random

def print_jolie():
    print("\n" + "="*50)
    print("Bonus time !")
    print("="*50 + "\n")

def random_number(x):
    return random.randint(1, x)

def valid_choice(max_index):
    while True:
        choix = input(" numéro : ")
        try:
            choix = int(choix)
            if 1 <= choix <= max_index:
                return choix - 1
        except ValueError:
            print("Choix invalide")