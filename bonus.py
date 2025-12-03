import random
from utils import print_jolie

def bonus_armor(team):
    print_jolie()
    armor = random.randint(1, 4)
    print(f"Bonus de {armor} ARMOR !")

    for i, champ in enumerate(team):
        print(f"{i+1}. {champ['name']} (ARMOR {champ['def']})")

    choix = input(" numéro : ")
    try:
        choix = int(choix)
        team[choix-1]['def'] += armor
        print(f" {team[choix-1]['name']} gagne {armor} 🛡️ et possède :  {team[choix-1]['def']} 🛡️")
    except:
        print("Invalide.")

def bonus_hp(team):
    print_jolie()
    hp = random.randint(5, 30)
    print(f"Bonus de {hp} HP !")

    for i, champ in enumerate(team):
        print(f"{i+1}. {champ['name']} (❤️ {champ['hp']})")

    choix = input(" numéro : ")
    try:
        choix = int(choix)
        team[choix-1]['hp'] += hp
        print(f" {team[choix-1]['name']} gagne {hp} ❤️ et possède :  {team[choix-1]['hp']} ❤️")
    except:
        print("Invalide.")

def bonus_ad(team):
    print_jolie()
    print("Bonus de 5 ⚔️ !")

    for i, champ in enumerate(team):
        print(f"{i+1}. {champ['name']} (⚔️ {champ['atk']})")

    choix = input(" numéro : ")
    try:
        choix = int(choix)
        team[choix-1]['atk'] += 5
        print(f" {team[choix-1]['name']} gagne 5 ⚔️ et possède :  {team[choix-1]['atk']} ⚔️")
    except:
        print("Invalide.")
