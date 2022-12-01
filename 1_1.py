with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

max_calories = 0
current_calories = 0
for line in lines:
    if len(line) == 0:
        if current_calories > max_calories:
            max_calories = current_calories
        current_calories = 0
    else:
        current_calories += int(line)

if current_calories > max_calories:
    max_calories = current_calories

print(max_calories)
