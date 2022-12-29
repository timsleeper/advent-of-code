# Using Hashing

def findPair(arr, sum_val):

    s = set()

    arr_len = len(arr)
    for i in range(arr_len):
        tmp = sum_val-arr[i]
        if tmp in s:
            print("Pair: " + str(arr[i]) + " " + str(tmp))
            print("Mult: " + str(arr[i]*tmp))
        s.add(arr[i])


my_file = open("data.txt", "r")
content_list = my_file.readlines()
for i in range(len(content_list)):
    content_list[i] = int(content_list[i])

findPair(content_list, 2020)