positionArray = []
with open('Day 5 - HydrothermalVents/numberfile.txt', 'rt') as f:
    for position in f:
        positionArray.append(position)

for positionCollection in positionArray:
    print(positionCollection)

print(positionArray)