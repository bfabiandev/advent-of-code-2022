with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

opponent_lookup = {"A": "rock", "B": "paper", "C": "scissors"}
you_lookup = {"X": "must lose", "Y": "must draw", "Z": "must win"}
score = {"rock": 1, "paper": 2, "scissors": 3}

sum_score = 0
for line in lines:
    opponent, you = line.split(" ")

    if you_lookup[you] == "must lose":
        if opponent_lookup[opponent] == "rock":
            choice = "scissors"
        elif opponent_lookup[opponent] == "paper":
            choice = "rock"
        elif opponent_lookup[opponent] == "scissors":
            choice = "paper"
    elif you_lookup[you] == "must draw":
        sum_score += 3
        choice = opponent_lookup[opponent]
    elif you_lookup[you] == "must win":
        sum_score += 6
        if opponent_lookup[opponent] == "rock":
            choice = "paper"
        elif opponent_lookup[opponent] == "paper":
            choice = "scissors"
        elif opponent_lookup[opponent] == "scissors":
            choice = "rock"

    sum_score += score[choice]

print(sum_score)
