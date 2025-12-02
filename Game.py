from pymongo import MongoClient
import random

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choisir la base de données
db = client["game_database"]

# Choisir la collection
LoL = db["game_LoL"]

# collection score board
score_board = db["score_board"]

def print_champ(query):
    jeux = LoL.find(query)
    for jeu in jeux:
        i = jeu.get('i', '<unknown>')
        name = jeu.get('name', '<unknown>')
        atk = jeu.get('atk', 0)
        defense = jeu.get('def', 0)
        hp = jeu.get('hp', 0)
        print(f"{i} : {name}, attaque : {atk}, defense : {defense}, hp : {hp}")

# afficher les documents de la collection
def afficher_monstres():
    query = {"type": "monstre"}
    print_champ(query)

# afficher les champions du jeu
def afficher_champions():
    query = {"type": "champion"}
    print_champ(query)

# attaquer les monstres avec les champions
def attaquer_champions_to_monstre(champion, monstre):
    print(f"{champion['name']} ⚔️  {monstre['name']}! ")
    dmg = champion['atk'] > monstre['def']  if champion['atk'] - monstre['def'] else 0
    monstre['hp'] -= dmg
    if monstre['hp'] <= 0:
        print(f"{monstre['name']} a été vaincu! 💀 ")
    else:
        print(f"{monstre['name']} a {monstre['hp']} HP restants.")

# attaquer les champions avec les monstres
def attaquer_monstre_to_champions(monstre, champion):
    print(f"{monstre['name']} 🔄⚔️  {champion['name']} !")
    dmg = monstre['atk'] > champion['def']  if monstre['atk'] - champion['def'] else 0
    champion['hp'] -= dmg
    if champion['hp'] <= 0:
        print(f"{champion['name']} a été vaincu! 💀 ")
    else:
        print(f"{champion['name']} a {champion['hp']} HP restants.")

def choisir_team():
    print("Choisissez votre équipe de 3 champions!")
    afficher_champions()
    team = []
    while len(team) < 3:
        choix_raw = input("Entrez le n° du champion à ajouter à votre équipe: ")
        choix_raw = choix_raw.strip()
        # On exige un entier : l'utilisateur choisit le n° 'i' tel qu'il est dans la BDD
        try:
            choix_int = int(choix_raw)
        except ValueError:
            print("Veuillez entrer un numéro entier (le n° 'i' affiché).")
            continue

        # Recherche stricte par entier
        champion = LoL.find_one({"i": choix_int, "type": "champion"})
        if champion:
            # Vérifier si déjà sélectionné (par _id si présent, sinon par 'i')
            champ_id = champion.get('_id')
            already = False
            for m in team:
                if champ_id is not None and m.get('_id') == champ_id:
                    already = True
                    break
                if champ_id is None and m.get('i') == champion.get('i'):
                    already = True
                    break

            if already:
                # Afficher le nom du champion en cas de doublon
                print(f"{champion.get('name', str(choix_int))} est déjà dans votre équipe. Choisissez un autre champion.")
            else:
                team.append(champion)
                # Afficher le nom du champion ajouté (pas l'i)
                print(f"{champion.get('name', str(choix_int))} ajouté à votre équipe.")
        else:
            print("Champion non trouvé (vérifiez le n° 'i' affiché), veuillez réessayer.")
    print("Votre équipe est prête!")
    #print les noms des champions choisis avec attaque, defense et hp
    print("Votre équipe:")
    for membre in team:
        print(f"{membre['name']} - Attaque: {membre['atk']}, Défense: {membre['def']}, HP: {membre['hp']}")
    return team


def enregistrer_et_afficher_scores(nom_invocateur, vagues_survecues):
    """
    Enregistre le score d'un invocateur et affiche le top 3 des meilleurs scores.
    
    Args:
        nom_invocateur (str): Le nom de l'invocateur
        vagues_survecues (int): Le nombre de vagues survivies
    """
    # Insérer le score dans la collection
    document = {
        "nom_invocateur": nom_invocateur,
        "vagues_survecues": vagues_survecues
    }
    score_board.insert_one(document)
    
    # Récupérer et afficher les 3 meilleurs scores
    top_scores = score_board.find().sort("vagues_survecues", -1).limit(3)
    print("Top 3 des meilleurs scores:")
    for score in top_scores:
        print(f"{score['nom_invocateur']} : {score['vagues_survecues']} vagues")

def bonus_hp(team):
    #choisir un champion encore en vie et lui attribuer un bonus de 10 hp
    #valeur aléatoire entre 5 et 30
    hp_win = random.randint(5, 30)
    print(f"Un champion reçoit un bonus de {hp_win} HP!")
    print("Choisissez un champion pour recevoir le bonus:")
    for idx, champ in enumerate(team):
        print(f"{idx + 1}. {champ['name']} (HP actuel: {champ['hp']})")
    input_choice = input(f"Entrez le numéro du champion qui recevra {hp_win} hp : ")
        #vérifier que l'entrée est un entier valide
    try:
        choice_int = int(input_choice)
        if 1 <= choice_int <= len(team):
            team[choice_int - 1]['hp'] += 10
            print(f"{team[choice_int - 1]['name']} a maintenant {team[choice_int - 1]['hp']} HP.")
        else:
            print("Numéro invalide. Aucun bonus attribué.")
    except ValueError:
        print("Entrée invalide. Aucun bonus attribué.")
    pass

def bonus_ad(team):
    #choisir un champion encore en vie et lui attribuer un bonus de 5 ad
    print("Un champion reçoit un bonus de 5 AD!")
    print("Choisissez un champion pour recevoir le bonus:")
    for idx, champ in enumerate(team):
        print(f"{idx + 1}. {champ['name']} (AD actuel: {champ['atk']})")
    input_choice = input("Entrez le numéro du champion qui recevra 5 ad : ")
        #vérifier que l'entrée est un entier valide
    try:
        choice_int = int(input_choice)
        if 1 <= choice_int <= len(team):
            team[choice_int - 1]['atk'] += 5
            print(f"{team[choice_int - 1]['name']} a maintenant {team[choice_int - 1]['atk']} AD.")
        else:
            print("Numéro invalide. Aucun bonus attribué.")
    except ValueError:
        print("Entrée invalide. Aucun bonus attribué.")
    pass

counter_vague = 0

if __name__ == "__main__":
    nom = input("Entrez votre nom d'invocateur: ")
    team = choisir_team()
    monstre = LoL.aggregate([{"$match": {"type": "monstre"}}, {"$sample": {"size": 1}}]).next()

    while True:
        if monstre['hp'] <= 0:
            counter_vague += 1
            print(f"Vague {counter_vague} terminée.")
            bonus_hp(team)
            bonus_ad(team)

            # nouveau monstre
            monstre = LoL.aggregate([
                {"$match": {"type": "monstre"}},
                {"$sample": {"size": 1}}
            ]).next()

            print(f"Un monstre sauvage apparaît: {monstre['name']} (Attaque: {monstre['atk']}, Défense: {monstre['def']}, HP: {monstre['hp']})")

        for champion in team:
            if champion['hp'] > 0 and monstre['hp'] > 0:
                attaquer_champions_to_monstre(champion, monstre)

                if monstre['hp'] > 0:  # le monstre est encore en vie → il contre-attaque
                    attaquer_monstre_to_champions(monstre, champion)

        team = [champ for champ in team if champ['hp'] > 0]

        if not team:
            print("Tous vos champions ont été vaincus! Game Over.")
            print(f"Il s'est passé {counter_vague} vagues.")
            print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

            enregistrer_et_afficher_scores(nom, counter_vague)
            break
