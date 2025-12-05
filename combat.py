import math
import random
import time

def crit_attack(attacker):
    base_crit = attacker.get('crit', 0)
    crit_chance = min(base_crit * 10, 100)
    roll = random.randint(1, 100)
    if roll <= crit_chance:
        print(f"Coup critique de {attacker['name']}! 💥")
        return 2
    return 1

def compute_damage(atk,defense):
    return math.floor(max(0, atk * 100 / (100 + defense) ))

def compute_hp(hp, max_hp):
    return min(max(0, hp), max_hp)

def info_status(team, monster, dead_list=None):

    if dead_list is None:
        dead_list = []

    print("="*50)
    print("--- Statut de l'équipe ---")

    for champ in team:
        print(f"{champ['name']}: {max(0, champ.get('hp', 0))} ❤️")

    if dead_list:

        print("--- Champions morts ---")
        for champ in dead_list:
            print(f"{champ.get('name','?')}: 0 ❤️ ")

    print("--- Statut du monstre ---")
    print(f"{monster['name']}: {max(0, monster.get('hp', 0))} ❤️")
    print("="*50)
    time.sleep(1)

def attacker_to_defender(attacker, defender):

    crit = crit_attack(attacker)
    dmg = compute_damage(attacker['atk']*crit, defender['def'])
    max_hp = defender.get('max_hp', defender.get('hp', 100))
    defender['hp'] = compute_hp( defender['hp'] - dmg, max_hp)
    
    print("-"*15)

    if attacker.get('type') == 'monstre':
        print(f"{attacker['name']} 🔄⚔️  {defender['name']} {defender['hp']}❤️ !")
    else:
        print(f"{attacker['name']} ⚔️  {defender['name']}  {defender['hp']}❤️ !")
    print(f"dmg infligé: {dmg}")
    time.sleep(1)