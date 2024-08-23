# import re

# with open("Day 5\inputTest.txt") as file:
#     inputFile = file.readlines()

# seedRange = []
# blockMap = []
# seed = list(map(int, inputFile[0].split(":")[1].split()))

# seedRange = [(seed[index], seed[index] + seed[index+1])
#              for index in range(0, len(seed), 2)]

# del inputFile[0]
# blockMap = [list(map(int, item.strip().split()))
#             for item in inputFile if ":" not in (item) and item != "\n"]


# new = []
# while len(seedRange) > 0:
#     start, end = seedRange.pop()
#     for destination, source, rangeItem in blockMap:
#         overlapStart = max(start, source)
#         overlapEnd = min(end, source + rangeItem)
#         if overlapStart < overlapEnd:
#             new.append((overlapStart - source + destination,
#                         overlapEnd - source + destination))
#             if overlapStart > start:
#                 seedRange.append((start, overlapStart))
#             if end > overlapEnd:
#                 seedRange.append((overlapEnd, end))
#             break
#         else:
#             new.append((start, end))
# seedRange = new

# print(min(seedRange)[0])

inputs, *blocks = open("Day 5\input.txt").read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))
    seeds = new

print(min(seeds)[0])
