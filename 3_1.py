with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# convert a -> 1, b -> 2, c -> 3, etc.
get_priority = lambda x: ord(x) - 96 if not x.isupper() else ord(x) - 38

sum_priorities = 0
for line in lines:
    compartment1, compartment2 = line[:len(line)//2], line[len(line)//2:]
    priorities1 = set(map(get_priority, compartment1))
    priorities2 = set(map(get_priority, compartment2))

    # take intersection of priorities
    priorities = priorities1.intersection(priorities2)
    assert len(priorities) == 1, "No unique priority found"
    priority = priorities.pop()
    sum_priorities += priority

print(sum_priorities)