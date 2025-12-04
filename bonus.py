import random
from utils import print_jolie
from utils import random_number
from utils import valid_choice

def bonus_armor(team):

    armor = random.randint(1, 4)
    
    print_jolie()
    print(f"Bonus de {armor} 🛡️ !")

    for i, champ in enumerate(team):
        print(f"{i+1}. {champ['name']} ({champ['def']}) 🛡️")

    idx = valid_choice(len(team))
    if idx is not None:
        team[idx]['def'] += armor
        print(f" {team[idx]['name']} gagne {armor} 🛡️ et possède :  {team[idx]['def']} 🛡️")
    else:
        print("Invalide.")

def bonus_hp(team):
    print_jolie()

    if random_number(10) % 2 == 1:
        hp = random.randint(10, 50)
        print(f"Bonus de {hp} HP pour toute l'équipe !")

        for champ in team:
            champ['hp'] += hp
            print(f" {champ['name']} gagne {hp} ❤️ et possède :  {champ['hp']} ❤️")

    if random_number(10) % 2 == 0: 
        hp = random.randint(5, 30)
        print(f"Bonus de {hp} HP !")
        
        for i, champ in enumerate(team):
            print(f"{i+1}. {champ['name']} ({champ['hp']}) ❤️")

        idx = valid_choice(len(team))
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

        # choix = input(" numéro : ")
        idx = valid_choice(len(team))
        if idx is not None:
            team[idx]['atk'] += 5
            print(f" {team[idx]['name']} gagne 5 ⚔️ et possède :  {team[idx]['atk']} ⚔️")
        else:
            print("Invalide.")

def bonus_crit(team):

    if random_number(10) != 7:
        return
    
    print_jolie()
    print("Bonus de 0.15 💥 !")

    for i, champ in enumerate(team):
        print(f"{i+1}. {champ['name']} ({champ['crit']}) 💥")

    #choix = input(" numéro : ")
    idx = valid_choice(len(team))
    if idx is not None:
        team[idx]['crit'] += 0.15
        print(f" {team[idx]['name']} gagne 0.15 💥 et possède :  {team[idx]['crit']} 💥")
    else:
        print("Invalide.")

def resurrect_from_dead(dead_list, team):
    if random_number(3) !=1 and random_number(10) != 2:
        return
    
    if not dead_list:
        return

    print_jolie()
    print("Choisissez un mort à ressusciter :")

    for i, champ in enumerate(dead_list):
        print(f"{i+1}. {champ.get('name','?')} 0 ❤️")
    
    idx = valid_choice(len(dead_list))
    if idx is not None:
        cible = dead_list.pop(idx)
        cible['hp'] = 50
        team.append(cible)
        print(f"{cible.get('name','?')} a été ressuscité avec 50 ❤️ !")
    else:
        print("Invalide.")