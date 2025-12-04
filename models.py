from db import LoL

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
    from db import LoL
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

    print("Votre équipe :")
    for c in team:
        print(f"{c['name']}  ⚔️ {c['atk']}  🛡️ {c['def']} ❤️ {c['hp']}  💥  {c['crit']}")
    return team
