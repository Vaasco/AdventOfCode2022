#File path
fileName = 'D:\college\AOC 2022\Day6\input.txt'

#Reading from file
file = open(fileName,'r')
string = file.read()

agregate = set()

for i in range(14,len(string)):
    s = set(string[(i-14):i ])
    if(len(s) ==14):
        print(i)
        break