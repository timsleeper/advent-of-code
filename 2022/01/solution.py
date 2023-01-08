
def solve():

    file = open('input', 'r')
    Lines = file.readlines()
    
    running_sum = 0
    max_val = 0

    for line in Lines:
        if line.strip() == "":
            if running_sum > max_val:
                max_val = running_sum
            running_sum = 0
        else:
            if line.strip():
                running_sum += int(line)
        
    print(max_val)

if __name__ == "__main__":
    solve()