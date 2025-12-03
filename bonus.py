import random
from utils import print_jolie
from utils import evenement_aleatoire
from utils import valider_choix

def bonus_armor(team):
    print_jolie()
    armor = random.randint(1, 4)
    print(f"Bonus de {armor} 🛡️ !")

    for i, champ in enumerate(team):
        print(f"{i+1}. {champ['name']} ({champ['def']}) 🛡️")

    choix = input(" numéro : ")
    idx = valider_choix(choix, len(team))
    if idx is not None:
        team[idx]['def'] += armor
        print(f" {team[idx]['name']} gagne {armor} 🛡️ et possède :  {team[idx]['def']} 🛡️")
    else:
        print("Invalide.")

def bonus_hp(team):
    print_jolie()
    alea = evenement_aleatoire(10)

    #si alea est egal a 2 toute l'équipe est soignée
    if alea % 2 == 1:

        print(f"Bonus de {hp} HP pour toute l'équipe !")

        hp = random.randint(10, 50)
        for champ in team:
            champ['hp'] += hp
            print(f" {champ['name']} gagne {hp} ❤️ et possède :  {champ['hp']} ❤️")

    if alea % 2 == 0: 

        print(f"Bonus de {hp} HP !")
        
        hp = random.randint(5, 30)
        for i, champ in enumerate(team):
            print(f"{i+1}. {champ['name']} ({champ['hp']}) ❤️")

        choix = input(" numéro : ")
        idx = valider_choix(choix, len(team))
        if idx is not None:
            team[idx]['hp'] += hp
            print(f" {team[idx]['name']} gagne {hp} ❤️ et possède :  {team[idx]['hp']} ❤️")
        else:
            print("Invalide.")

def bonus_ad(team):

    if random.randint(1,10) % 2 == 0:

        print_jolie()
        print("Bonus de 5 ⚔️ !")

        for i, champ in enumerate(team):
            print(f"{i+1}. {champ['name']} ({champ['atk']}) ⚔️")

        choix = input(" numéro : ")
        idx = valider_choix(choix, len(team))
        if idx is not None:
            team[idx]['atk'] += 5
            print(f" {team[idx]['name']} gagne 5 ⚔️ et possède :  {team[idx]['atk']} ⚔️")
        else:
            print("Invalide.")

def bonus_crit(team):


    if evenement_aleatoire(10) == 7:
        print_jolie()
        print("Bonus de 0.15 💥 !")

        for i, champ in enumerate(team):
            print(f"{i+1}. {champ['name']} ({champ['crit']}) 💥")

        choix = input(" numéro : ")
        idx = valider_choix(choix, len(team))
        if idx is not None:
            team[idx]['crit'] += 0.15
            print(f" {team[idx]['name']} gagne 0.15 💥 et possède :  {team[idx]['crit']} 💥")
        else:
            print("Invalide.")

def resurrect_from_dead(dead_list, team):
    if not dead_list:
        return

    print_jolie()
    print("Choisissez un mort à ressusciter :")

    for i, champ in enumerate(dead_list):
        print(f"{i+1}. {champ.get('name','?')} 0 ❤️")
    
    choix = input(" numéro : ")
    idx = valider_choix(choix, len(dead_list))
    if idx is not None:
        cible = dead_list.pop(idx)
        cible['hp'] = 50
        team.append(cible)
        print(f"{cible.get('name','?')} a été ressuscité avec 50 ❤️ !")
    else:
        print("Invalide.")