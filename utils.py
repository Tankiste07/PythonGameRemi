import random

def print_jolie():
    print("\n" + "="*50)
    print("Bonus time !")
    print("="*50 + "\n")

def evenement_aleatoire(x):
    return random.randint(1, x)

def valider_choix(choix_str, max_index):

    try:
        choix = int(choix_str)
        if 1 <= choix <= max_index:
            return choix - 1
    except ValueError:
        pass
    return None