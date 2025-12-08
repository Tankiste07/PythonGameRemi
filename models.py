from db import LoL
from combat import attacker_to_defender
import random
from utils import valid_choice
import random


def print_champ(query):
    jeux = LoL.find(query)
    for jeu in jeux:
        i = jeu.get('i', '<unknown>')
        name = jeu.get('name', '<unknown>')
        atk = jeu.get('atk', 0)
        defense = jeu.get('def', 0)
        hp = jeu.get('hp', 0)
        crit = jeu.get('crit', 0)
        print(f"{i} : {name},  ⚔️ : {atk} , 🛡️ : {defense},  ❤️ : {hp},  💥 : {crit}")
    
def monstres():
    print_champ({"type": "monstre"})

def display_champions():
    print_champ({"type": "champion"})

def choose_team():

    print("Choisissez votre équipe de 3 champions!")
    display_champions()

    team = []
    while len(team) < 3:
        choix = input("Numéro du champion : ").strip()
        try:
            choix = int(choix)
        except:
            print("Entrez un entier.")
            continue

        champion = LoL.find_one({"i": choix, "type": "champion"})
        if not champion:
            print("Champion introuvable.")
            continue

        if any(champ['i'] == champion['i'] for champ in team):
            print("Déjà dans l’équipe.")
            continue

        team.append(champion)
        print(f"{champion['name']} ajouté !")
    print("-"*30)
    print("Votre équipe :")
    print("-"*30)
    for c in team:
        print(f"{c['name']}  ⚔️ {c['atk']}  🛡️ {c['def']} ❤️ {c['hp']}  💥  {c['crit']}")
    return team

def execute_turn_by_difficulty(game_difficulty, team, monster, counter_wave):

    difficulty = int(game_difficulty)
    
    if difficulty == 2:

        monster['atk'] += counter_wave + 1
        monster['def'] += counter_wave + 1
        monster['hp'] += counter_wave + 1

    elif difficulty == 1 or difficulty == 2:

        for champion in team:
            if champion['hp'] > 0 and monster['hp'] > 0:
                attacker_to_defender(champion, monster)
                if monster['hp'] > 0:
                    attacker_to_defender(monster, champion)   
    else:
        
        for champion in team:
            if champion['hp'] > 0 and monster['hp'] > 0:
                attacker_to_defender(champion, monster)
        if monster['hp'] > 0:
            alive = [c for c in team if c.get('hp', 0) > 0]
            if alive:
                cible = random.choice(alive)
                attacker_to_defender(monster, cible)
