import time
import sys

starttime = time.time()

crabPositions = []
with open('2021/Day 7 - WALES/numberfile.txt', 'rt') as f:
    for position in f.readline().split(','):
        crabPositions.append(int(position))

leastFuel = sys.maxsize
for i in range(1967):
    fuelConsumption = 0
    for position in crabPositions:
        fuelConsumption += abs(position - i)
    
    #isLess = leastFuel > fuelConsumption
    #leastFuel = fuelConsumption * isLess + leastFuel * (not isLess) #branchless min calculation, not faster in this case
    leastFuel = min(fuelConsumption, leastFuel) #faster cause it runs in C

print(leastFuel)
print(time.time() - starttime)