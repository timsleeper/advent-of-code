def solve():
    with open("input.txt") as infile:
        data = [int(line.strip()) for line in infile.readlines()]

    count = 0
    for i in range(0, len(data) - 1):
        if data[i + 1] > data[i]:
            count += 1

    print(count)


if __name__ == "__main__":
    solve()
