with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

calories = []
current_calories = 0
for line in lines:
    if len(line) == 0:
        calories.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(line)

calories.append(current_calories)

print(sum(sorted(calories)[-3:]))
