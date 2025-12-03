from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client["game_database"]

LoL = db["game_LoL"]
score_board = db["score_board"]
