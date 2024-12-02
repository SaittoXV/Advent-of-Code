with open("Day 5\inputTest.txt") as file:
    inputFile = file.readlines()

seedRange = []
blockMap = []
seed = list(map(int, inputFile[0].split(":")[1].split()))

seedRange = [(seed[index], seed[index] + seed[index+1])
             for index in range(0, len(seed), 2)]

del inputFile[0]
blockMap = [list(map(int, item.strip().split()))
            for item in inputFile if ":" not in (item)]

for range in blockMap:
    new = []
    while len(seedRange) > 0:
        start, end = seedRange.pop()
        for destination, source, rangeItem in blockMap:
            overlapStart = max(start, source)
            overlapEnd = min(end, source + rangeItem)
            if overlapStart < overlapEnd:
                new.append((overlapStart - source + destination,
                            overlapEnd - source + destination))
                if overlapStart > start:
                    seedRange.append((start, overlapStart))
                if end > overlapEnd:
                    seedRange.append((overlapEnd, end))
                break
        else:
            new.append((start, end))
    seedRange = new

print(min(seedRange)[0])
