from db import score_board

def record_and_display_scores(name, waves, tours=None):
    score_board.insert_one({
        "nom_invocateur": name,
        "vagues_survecues": waves,
        "tours": tours
    })

    print("\nClassement des meilleurs scores :")
    print("Top 3 :")

    top_scores = score_board.find().sort(
        [("vagues_survecues", -1), ("tours", 1)]
    ).limit(3)
    for idx, score in enumerate(top_scores, start=1):
        name = score.get("nom_invocateur", "<inconnu>")
        waves = score.get("vagues_survecues", 0)
        tours = score.get("tours", 0)
        print(f"{idx}. {name} - Vagues survécues : {waves}, Tours : {tours}")
