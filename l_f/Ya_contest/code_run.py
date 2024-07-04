import sys


def main1():
    len_arr = int(input())
    arr = [int(i) for i in input().split()]
    ask = int(input())
    
    arr.sort()
    res = {}
    
    counter = 0
    while counter < len_arr:
        
        
        
    

def main():
    a = set(input().split())
    res = set(list(input()))
    print(len(res) - len(set.intersection(a, res)))


text = ['She sells sea shells on the sea shore;\n',
        "The shells that she sells are sea shells I'm sure.\n",
        'So if she sells sea shells on the sea shore,\n',
        "I'm sure that the shells are sea shore shells.\n", '\n']


def main():
    # text_list = sys.stdin.readlines()
    text_list = [i.split() for i in text]
    res = []
    for i in text_list:
        res += i
    print(len(set(res)))



if __name__ == '__main__':
    main1()
