from bisect import bisect_left
import string

# first_dict = {'First':None}
# second_dict = {'Second':None}

first = []
second = []

with open('input.txt', 'r', encoding='utf-8') as f:
    steps = []
    counter = 1
    for i in f.readlines():
        i = i.strip()
        if len(i) == 1:
            hodov = i
        else:
            if counter % 2 == 0:
                first.append([int(x) for x in i.split()])
            else:
                second.append([int(x) for x in i.split()])
        counter += 1


def get_win(arr: list):
    x = [i[0] for i in arr]
    y = [i[1] for i in arr]
    # go to x
    for i in arr:
        if x.count(i[0]) == 5: #got to all dotes where x.count == 5
            repeat_dots = [item[1] for item in arr if item[0] == i[0]]
            return max_long_sort(repeat_dots)
        elif y.count(i[1]) == 5: #got to all dotes where x.count == 5
            repeat_dots = [item[0] for item in arr if item[1] == i[1]]
            print(repeat_dots)
            return max_long_sort(repeat_dots)
        elif 


def max_long_sort(arr: list):
    print(arr)
    arr.sort()
    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == 1:
            cnt += 1
            if cnt == 4:
                return True
        else: cnt = 0
    return False

    

    #    [4, 1], [2, 1], [3, 1], [1, 1], [5, 1]
    #    [[4, 1], [2, 1], [3, 1], [1, 1], [5, 1]]


print(get_win([[4, 1], [2, 1], [3, 1], [1, 1], [5, 1]]))

print(get_win([[4, 1], [2, 1], [3, 1], [1, 1], [5, 1]]))
