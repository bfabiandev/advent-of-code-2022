with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

opponent_lookup = {"A": "rock", "B": "paper", "C": "scissors"}
you_lookup = {"X": "rock", "Y": "paper", "Z": "scissors"}
score = {"rock": 1, "paper": 2, "scissors": 3}

sum_score = 0
for line in lines:
    opponent, you = line.split(" ")

    sum_score += score[you_lookup[you]]
    if (
        (opponent_lookup[opponent] == "rock" and you_lookup[you] == "paper")
        or (opponent_lookup[opponent] == "paper" and you_lookup[you] == "scissors")
        or (opponent_lookup[opponent] == "scissors" and you_lookup[you] == "rock")
    ):
        sum_score += 6
    elif opponent_lookup[opponent] == you_lookup[you]:
        sum_score += 3
    else:
        pass

print(sum_score)
