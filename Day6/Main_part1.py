#File path
fileName = 'D:\college\AOC 2022\Day6\input.txt'

#Reading from file
file = open(fileName,'r')
string = file.read()

agregate = set()

for i in range(4,len(string)):
    s = set(string[(i-4):i ])
    if(len(s) == 4):
        print(i)
        break