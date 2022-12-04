with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

unnecessary_elves = 0
for line in lines:
    section1, section2 = line.split(",")
    start1, end1 = map(int, section1.split("-"))
    start2, end2 = map(int, section2.split("-"))

    if end1 - start1 >= end2 - start2:
        if start2 >= start1 and end2 <= end1:
            unnecessary_elves += 1

    elif end2 - start2 > end1 - start1:
        if start1 >= start2 and end1 <= end2:
            unnecessary_elves += 1

print(unnecessary_elves)
