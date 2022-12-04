with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

overlaps = 0
for line in lines:
    section1, section2 = line.split(",")
    start1, end1 = map(int, section1.split("-"))
    start2, end2 = map(int, section2.split("-"))

    if start1 <= start2 <= end1 or start2 <= start1 <= end2:
        overlaps += 1

print(overlaps)
