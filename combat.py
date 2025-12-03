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

def attaquer_champions_to_monstre(champion, monstre):
    print("\n" + "-"*50)
    print(f"{champion['name']} ⚔️  {monstre['name']}  {monstre['hp']}❤️! ")

    crit = crit_attack(champion)
    dmg = math.floor(max(0, champion['atk'] * crit * 100 / (100 + monstre['def'])))

    # Appliquer les dégâts et empêcher les HP négatifs
    monstre['hp'] = max(0, monstre.get('hp', 0) - dmg)
    print(f"dmg infligé: {dmg}")
    time.sleep(1)

def attaquer_monstre_to_champions(monstre, champion):
    print(f"{monstre['name']} 🔄⚔️  {champion['name']} {champion['hp']}❤️!")
    dmg = math.floor(max(0, monstre['atk'] * 100 / (100 + champion['def'])))
    print(f"dmg infligé: {dmg}")

    # Appliquer les dégâts et empêcher les HP négatifs
    champion['hp'] = max(0, champion.get('hp', 0) - dmg)
    time.sleep(1)

def info_status(team, monstre):
    print("\n" + "="*50)
    print("--- Statut de l'équipe ---")
    for champ in team:
        print(f"{champ['name']}: {max(0, champ.get('hp', 0))} ❤️")

    print("--- Statut du monstre ---")
    print(f"{monstre['name']}: {max(0, monstre.get('hp', 0))} ❤️")
    print("="*50)
    time.sleep(1)
