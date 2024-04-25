from bisect import bisect_left
import string


first = []
second = []

with open('input.txt', 'r', encoding='utf-8') as f:
    steps = []
    counter = 1
    reads = f.readlines()
    hodov = reads[0]
    for i in reads[1:]:
        i = i.strip()
        if counter % 2 == 0:
            second.append([int(x) for x in i.split()])
        else:
            first.append([int(x) for x in i.split()])
        counter += 1


def write_to_f(data: str):
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(data)


def get_win(arr: list):
    x = [i[0] for i in arr]
    y = [i[1] for i in arr]

    for i in arr:
        if x.count(i[0]) == 5:
            repeat_dots = [item[1] for item in arr if item[0] == i[0]]
            return max_long_sort(repeat_dots)
        elif y.count(i[1]) == 5:
            repeat_dots = [item[0] for item in arr if item[1] == i[1]]
            return max_long_sort(repeat_dots)
        elif max_long_sort(x) == max_long_sort([-i for i in y]):
            return True
        elif max_long_sort(y) == max_long_sort([-i for i in x]):
            return True
    return False


def max_long_sort(arr: list):
    print(arr)
    arr.sort()
    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == 1:
            cnt += 1
            if cnt == 4:
                return True
        else:
            cnt = 0
    return False


hodov = len(first) + len(second)



if get_win(first) and hodov > len(first) // 2:
    write_to_f('First')
elif get_win(second) and hodov > len(second) // 2:
    write_to_f('Second')
else:
    write_to_f('Draw')


# if result_f > 4 or result_s > 4:
#     write_to_f('Inattention')
# elif result_f == 4:
#     write_to_f('First')
# elif result_s == 4:
#     write_to_f('Second')
# else:
#     write_to_f('Draw')
    