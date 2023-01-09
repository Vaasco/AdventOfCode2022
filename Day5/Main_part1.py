import string

with open("D:\college\AOC 2022\Day5\input.txt",'r') as f:
    lines = f.read()


crateRaw, instructions = lines.rstrip().split("\n\n")

count = 0
spaceCount = 0

#Arranging the crates
obj = {}
for i in range(0,len(crateRaw)+1):
    if(crateRaw[i] == '\n'):
        count = 0
    if(crateRaw[i] in string.ascii_uppercase):
        count += 1
        if('l'+str(count) not in obj):
            obj['l'+str(count)] = []
            obj['l'+str(count)].append(crateRaw[i])
        else:
            obj['l'+str(count)].append(crateRaw[i])

print(obj)