from db import LoL
from models import choose_team
from combat import *
from bonus import bonus_is_comming, resurrect_from_dead
from score import record_and_display_scores
import random

counter_wave = 0
counter_tour = 0

if __name__ == "__main__":
    nom = input("Entrez votre nom d'invocateur: ")
    team = choose_team()
    dead_list = []
    game_diffcult = input("Voulez-vous jouer en mode difficile ? (y/n)")
    monster = LoL.aggregate([
        {"$match": {"type": "monstre"}},
        {"$sample": {"size": 1}}
    ]).next()

    while True:
        if monster['hp'] <= 0:
            counter_wave += 1

            print(f"Vague {counter_wave} terminée.")
            print("Temps pour un bonus avant la prochaine vague!")

            resurrect_from_dead(dead_list, team)
            bonus_is_comming(team)

            monster = LoL.aggregate([
                {"$match": {"type": "monstre"}},
                {"$sample": {"size": 1}}
            ]).next()
        if game_diffcult.lower() == 'y':
            monster['atk'] += counter_wave + 1
            monster['def'] += counter_wave + 1
            monster['hp'] += counter_wave + 1
            for champion in team:
                if champion['hp'] > 0 and monster['hp'] > 0:
                    attacker_to_defender(champion, monster)
                    if monster['hp'] > 0:
                        attacker_to_defender(monster, champion)
        else:
            for champion in team:
                if champion['hp'] > 0 and monster['hp'] > 0:
                    attacker_to_defender(champion, monster)

            # Le monstre attaque UN champion aléatoire encore en vie
            if monster['hp'] > 0:
                alive = [c for c in team if c.get('hp', 0) > 0]
                if alive:
                    cible = random.choice(alive)
                    attacker_to_defender(monster, cible)


        new_dead = [champ for champ in team if champ.get('hp', 0) <= 0]
        for d in new_dead:
            if d not in dead_list:
                dead_list.append(d)

        team = [champ for champ in team if champ.get('hp', 0) > 0]
        counter_tour += 1
        
        print("="*50)
        print(f"\n--- Fin du tour {counter_tour} ---")

        info_status(team, monster, dead_list,)
        
        if not team:
            print("Tous vos champions ont été vaincus!")
            print(f"Vous avez survécu {counter_wave} vagues.")
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
            record_and_display_scores(nom, counter_wave, counter_tour)
            break
