with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# convert a -> 1, b -> 2, c -> 3, etc.
get_priority = lambda x: ord(x) - 96 if not x.isupper() else ord(x) - 38

sum_priorities = 0

# iterate on groups of 3
for idx in range(0, len(lines), 3):
    # get the 3 lines
    line1, line2, line3 = lines[idx:idx+3]
    priorities1 = set(map(get_priority, line1))
    priorities2 = set(map(get_priority, line2))
    priorities3 = set(map(get_priority, line3))

    # take intersection of priorities
    priorities = priorities1.intersection(priorities2).intersection(priorities3)
    assert len(priorities) == 1, "No unique priority found"
    priority = priorities.pop()
    sum_priorities += priority

print(sum_priorities)