from string import ascii_letters

#file path
fileName = 'D:\college\AOC 2022\Day3\input.txt'

#Reading from file
with open(fileName) as file:
    rucksack = [i for i in file.read().strip().split("\n")]

#First split every rucksack into two compartments
sum = 0
#enumerateObj = enumerate(ascii_letters)
#print(enumerateObj)
for i in range(0,len(rucksack),3):
        first = set(rucksack[i])
        second = set(rucksack[i+1])
        third = set(rucksack[i+2])
        result = first.intersection(second).intersection(third).pop()
        for priority , char in enumerate(ascii_letters):
           if(result == char):
                sum += priority+1
                break

            
print(sum)
