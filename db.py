from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client["game_database"]

LoL = db["game_LoL"]
score_board = db["score_board"]


"""from pymongo import MongoClient

def seed_database():
    client = MongoClient("mongodb://localhost:27017/")

    # NOM DE TA BASE DE DONNÉES
    db = client["game_database"]

    # NOM DE TA COLLECTION PRINCIPALE
    col = db["game_LoL"]

    # Vérifier si la BDD contient déjà des données
    if col.count_documents({}) > 0:
        print("📌 Base déjà initialisée, aucun ajout nécessaire.")
        return

    print("📦 Base vide → initialisation des données...")


    { i: 0, type: "champion", name: "Garen", atk: 15, def: 10, hp: 100, crit : 0.2 },
    { i: 1, type: "champion", name: "Ryze", atk: 20, def: 5, hp: 80, crit : 0.1},
    { i: 2, type: "champion", name: "Ashe", atk: 18, def: 7, hp: 90, crit : 0.4},
    { i: 3, type: "champion", name: "Zed", atk: 22, def: 8, hp: 85, crit : 0.5},
    { i: 4, type: "champion", name: "Akshan", atk: 14, def: 12, hp: 110, crit : 0.45 },
    { i: 5, type: "champion", name: "Aurelion Sol", atk: 25, def: 3, hp: 70, crit : 0.1 },
    { i: 6, type: "champion", name: "Jarvan IV", atk: 17, def: 15, hp: 120, crit : 0.15 },
    { i: 7, type: "champion", name: "Lee Sin", atk: 19, def: 9, hp: 95, crit : 0.2},
    { i: 8, type: "champion", name: "Warwick", atk: 23, def: 6, hp: 105, crit  : 0.15},
    { i: 9, type: "champion", name: "Graves", atk: 16, def: 11, hp: 100, crit : 0.35 },

    { i: 10, type: "monstre", name: "Krugs", atk: 10, def: 5, hp: 50 },
    { i: 11, type: "monstre", name: "Rift Herald", atk: 20, def: 8, hp: 120 },
    { i: 12, type: "monstre", name: "Elder Drake", atk: 35, def: 20, hp: 300 },
    { i: 13, type: "monstre", name: "Raptors", atk: 12, def: 6, hp: 70 },
    { i: 14, type: "monstre", name: "Wolfs", atk: 25, def: 15, hp: 200 },
    { i: 15, type: "monstre", name: "Gromp", atk: 18, def: 10, hp: 100 },
    { i: 16, type: "monstre", name: "Blue Buff", atk: 30, def: 25, hp: 250 },
    { i: 17, type: "monstre", name: "Red Buff", atk: 22, def: 12, hp: 150 },
    { i: 18, type: "monstre", name: "Drake Infernale", atk: 28, def: 18, hp: 180 },
    { i: 19, type: "monstre", name: "Scuttle", atk: 15, def: 7, hp: 90 }

    # Insertion de tous les personnages
    col.insert_many(champions + monstres)

    print("✅ Base de données initialisée avec champions + monstres !")
"""