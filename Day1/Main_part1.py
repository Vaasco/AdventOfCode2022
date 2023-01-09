#File path
fileName = 'D:\college\AOC 2022\Day1\input.txt'

#Reading from file
file = open(fileName,'r')
read = file.readlines()

#Going through the array and adding up all the calories and when we find a '\n' character we see if the current sum is bigger than the best sum then we put current sum back on zero and start again until the end of the array.
newString = ''
bestSum = 0
currentSum = 0
for i in read:
    if i == '\n':
        currentSum = 0
    else:
       newString = i.replace('\n','')
       currentSum += int(newString)  
    if currentSum > bestSum:
        bestSum = currentSum

print(bestSum)