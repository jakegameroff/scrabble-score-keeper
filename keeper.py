import json

with open("scores.json", "r") as f:
    data = json.load(f)

players = data
order = ("Player 1", "Player 2", "Player 3")

while True:
    for p in order:
        pts = int(input(f"{p} scores: "))
        word = input(f"{p}'s word: ")

        players[p][0] += pts
        players[p][1].append(word)
        
        with open("scores.json", "w") as f:
            json.dump(players, f, indent=4)