from db import score_board

def enregistrer_et_afficher_scores(nom, vagues):
    score_board.insert_one({
        "nom_invocateur": nom,
        "vagues_survecues": vagues
    })

    print("Top 3 :")
    top = score_board.find().sort("vagues_survecues", -1).limit(3)
    for s in top:
        print(f"{s['nom_invocateur']} : {s['vagues_survecues']} vagues")
