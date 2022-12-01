calorieArr = []
with open('2022/Day 1 - CalorieCounting/numberfile.txt', 'rt') as f:
    for line in f:
        line = line.split('\n')[0]
        calorieArr.append(line)

def sum(array):
    temp = 0
    for number in array:
        temp += int(number)
    return temp

tempArr = []
elfArr = []
for line in calorieArr:
    if line:
        tempArr.append(line)
    else:
        elfArr.append(sum(tempArr))
        tempArr.clear()

elfArr.sort(reverse=True)
print(elfArr[0] + elfArr[1] + elfArr[2])