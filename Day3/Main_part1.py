from string import ascii_letters

#file path
fileName = 'D:\college\AOC 2022\Day3\input.txt'

#Reading from file
with open(fileName) as file:
    rucksack = [i for i in file.read().strip().split("\n")]

#First split every rucksack into two compartments
sum = 0
enumerateObj = enumerate(ascii_letters)
print(enumerateObj)
for i in rucksack:
    midPoint = int(len(i)//2)
    firstCompartment = i[:midPoint]
    secondCompartment = i[midPoint:]

    for priority,char in enumerate(ascii_letters):
        if char in secondCompartment and char in firstCompartment:
            sum += priority + 1

print(sum)
