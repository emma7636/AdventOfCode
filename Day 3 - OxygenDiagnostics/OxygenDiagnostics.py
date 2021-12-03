binaryArray = []
with open('Day 3 - OxygenDiagnostics/numberfile.txt', 'rb') as f:
    binaryArray = list(f)

intArray = []
for binary in binaryArray:
    intArray.append(int(binary, 2))

def countBits(numbers, pos, mask) -> int:
    result = 0
    for number in numbers:
        if (((number & mask) >> pos) == 1):
            result += 1
    return result

def getNumbers(array, pos, mask, comparator) -> int:
    if (len(array) == 1):
        return array[0]
    
    match comparator:
        case 1:
            if (countBits(array, pos, mask) >= len(array)/2):
                comparative = 1
            else:
                comparative = 0
        case 0:
            if (countBits(array, pos, mask) < len(array)/2):
                comparative = 1
            else:
                comparative = 0
    
    tempArray = []
    for number in array:
        if (((number & mask) >> pos) == comparative):
            tempArray.append(number)
    if (pos > 0):
        mask = mask >> 1
        pos -= 1
        return getNumbers(tempArray, pos, mask, comparator)

pos = 11
mask = int('100000000000', 2)

print(getNumbers(intArray, pos, mask, 1) * getNumbers(intArray, pos, mask, 0))