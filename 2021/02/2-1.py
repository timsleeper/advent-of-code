def solve():
    with open("input.txt") as infile:
        data = [line.strip() for line in infile.readlines()]

    horizontal = 0
    vertical = 0
    for i in range(0, len(data)):
        if data[i].split()[0] == "forward":
            horizontal += int(data[i].split()[1])
        elif data[i].split()[0] == "up":
            vertical -= int(data[i].split()[1])
        elif data[i].split()[0] == "down":
            vertical += int(data[i].split()[1])

    print(horizontal * vertical)


if __name__ == "__main__":
    solve()
