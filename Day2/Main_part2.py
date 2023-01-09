#X = lose
#Y = draw
#Z = win

#Rock -> x -> 1
#Paper -> y -> 2
#Scissors -> z -> 3

#file path
fileName = 'D:\college\AOC 2022\Day2\input.txt'

#Reading from file
file = open(fileName,'r')
read = file.readlines()

dictionary = {
    "A X":3,"A Y":4,"A Z":8,
    "B X":1,"B Y":5,"B Z":9,
    "C X":2,"C Y":6,"C Z":7,
}

sum = 0
for i in read:
    newString = i.replace("\n","")
    result = dictionary[newString]
    sum += result

print(sum)