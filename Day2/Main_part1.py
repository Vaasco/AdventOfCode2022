#Rock -> x -> 1
#Paper -> y -> 2
#Scissors -> z -> 3

#file path
fileName = 'D:\college\AOC 2022\Day2\input.txt'

#REading from file
file = open(fileName,'r')
read = file.readlines()

dictionary = {
    "A X":4,"A Y":8,"A Z":3,
    "B X":1,"B Y":5,"B Z":9,
    "C X":7,"C Y":2,"C Z":6,
}

sum = 0
for i in read:
    newString = i.replace("\n","")
    result = dictionary[newString]
    sum += result

print(sum)