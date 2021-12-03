binaryArray = []
with open('Day 3 - OxygenDiagnostics/numberfile.txt', 'rb') as f:
    binaryArray = list(f)

intArray = []
for binary in binaryArray:
    intArray.append(int(binary, 2))

def getNumbers(array, pos, mask, comparator) -> int:
    if (len(array) == 1):
        return array[0]
    
    array0 = []
    array1 = []
    for number in array:
        if (((number & mask) >> pos) == 0):
            array0.append(number)
        else:
            array1.append(number)
    
    mask = mask >> 1
    pos -= 1
    match comparator:
        case 1:
            if (len(array1) >= len(array0)):
                return getNumbers(array1, pos, mask, comparator)
            else:
                return getNumbers(array0, pos, mask, comparator)
        case 0:
            if (len(array1) < len(array0)):
                return getNumbers(array1, pos, mask, comparator)
            else:
                return getNumbers(array0, pos, mask, comparator)

pos = 11
mask = int('100000000000', 2)

print(getNumbers(intArray, pos, mask, 1) * getNumbers(intArray, pos, mask, 0))