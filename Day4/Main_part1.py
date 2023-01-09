with open("D:\college\AOC 2022\Day4\input.txt") as fin:
    lines = fin.read().strip().split()

ans = 0
for line in lines:
    elves = line.split(",")
    ranges = [list(map(int,elf.split("-"))) for elf in elves]

    a,b = ranges[0]
    c,d = ranges[1]

    if a <= c and b >= d or a >= c and b <= d:
        ans += 1


print(ans)