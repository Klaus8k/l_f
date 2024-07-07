import sys

"""https://coderun.yandex.ru/selections/quickstart/problems/largest-product-three-numbers/description?currentPage=1&pageSize=20
"""
def main():
    # len_arr = int(input())
    # arr = [int(i) for i in input().split()]

    # len_arr = 9
    arr = [-3, -5, -7, 0, -16]
    arr_abs = [abs(i) for i in arr]
    
    a = []
    for i in range(3):
        x = arr_abs.index(max(arr_abs))
        arr_abs[x] = None
        a.append(x)
        # arr_abs.pop(x)
        # arr_abs.pop(arr_abs.index(max(arr_abs)))
        print(a)

    print(arr[a[0]], arr[a[1]], arr[a[2]])
    
if __name__ == '__main__':
    main()
