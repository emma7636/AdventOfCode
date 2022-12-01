binaryArray = []
with open('2021/Day 3 - PowerDiagnostics/numberfile.txt', 'rb') as f:
    binaryArray = list(f)

intArray = []
for binary in binaryArray:
    intArray.append(int(binary))

numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def countbits(number, scale):
    number = number - number%1
    if (number%10 == 1):
        numbers[scale] += 1
    if (scale < len(numbers)):
        scale += 1
        countbits(number/10, scale)

for number in intArray:
    countbits(number, 0)

gammaRate = int('000000000000', 2)
epsilonRate = int('000000000000', 2)
pos = 0
for number in numbers:
    if (number >= 500):
        gammaRate = gammaRate | (int('1', 2) << pos)
    else:
        epsilonRate = epsilonRate | (int('1', 2) << pos)
    pos += 1

print(gammaRate * epsilonRate)