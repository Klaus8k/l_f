import sys


def main():
    # len_arr = int(input())
    # arr = [int(i) for i in input().split()]
    # ask = int(input())

    len_arr = 5
    arr = [-12, 3, 29, -4]
    ask = -2

    arr.sort()

    x = None
    y = None
    
    

    res = arr[0]
    mid = abs(ask)

    if ask > 0:
        for i in arr:
            if abs(ask-i) < mid:
                mid = abs(ask-i)
                res = i

    elif ask < 0:
        for i in arr:
        
            if abs(-i-ask) < mid:
                    mid = abs(-i-ask)
                    res = i


    print(res)


if __name__ == '__main__':
    main()
