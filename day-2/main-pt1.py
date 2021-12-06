dist = 0
depth = 0
aim = 0
with open("input.txt") as file:
    for line in file:
        cmd = line.strip()
        if cmd[0] == 'f':
            dist += int(cmd[-1])
        elif cmd[0] == 'd':
            depth += int(cmd[-1])
        elif cmd[0] == 'u':
            depth -= int(cmd[-1])

print(dist*depth)