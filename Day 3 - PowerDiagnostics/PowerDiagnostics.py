binaryArray = []
with open('Day 3 - Diagnostics/numberfile.txt', 'rb') as f:
    binaryArray = list(f)

intArray = []
for binary in binaryArray:
    intArray.append(int(binary))

numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def doStuff(number, scale):
    
    number = number - number%1
    if (number%10 == 1):
        numbers[scale] += 1
    if (scale < len(numbers)):
        scale += 1
        doStuff(number/10, scale)

for number in intArray:
    doStuff(number, 0)

print(int(str(intArray[0]), 2))

gammaRate = int('000000000000', 2)
epsilonRate = int('000000000000', 2)
pos = 0
for number in numbers:
    if (number >= 500):
        gammaRate = gammaRate | (int('1', 2) << pos)
    else:
        epsilonRate = epsilonRate | (int('1', 2) << pos)
    pos += 1

print(gammaRate)
print(epsilonRate)

print(gammaRate * epsilonRate)