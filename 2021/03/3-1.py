def solve():
    with open("input.txt") as infile:
        data = [line.strip() for line in infile.readlines()]

    n = []
    for i in range(12):
        n.append(0)

    for i in range(len(data)):
        for j in range(12):
            n[j] += int(data[i][j])

    for j in range(12):
        if n[j] > len(data) / 2:
            n[j] = 1
        else:
            n[j] = 0

    m = [1 if i == 0 else 0 for i in n]
    res = int("".join(str(x) for x in n), 2)
    res2 = int("".join(str(x) for x in m), 2)

    print(res * res2)


if __name__ == "__main__":
    solve()
