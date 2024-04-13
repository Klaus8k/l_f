# a = input()
# b = input()
a = 'hellochild'
b = 'helto<left><bspace>l<delete>ochilds<bspace>'
# control = ['<delete>', '<bspace>', '<left>', '<right>',]
# test = 'lorem ipsum'

def delete_letter(a: str, pos: int):
    if len(a) == pos:
        return [a, pos]
    else:
        a = a[:pos+1] + a[pos+2:]
        return [a, pos]
    
def bspace_letter(a: str, pos: int):
    if pos == 0:
        return [a, pos]
    else:
        pos -= 1
        a = a[:pos] + a[pos+1:]
        return [a, pos]
    
def direction_l(a: str, pos: int):
    if pos == 0:
        return [a, pos]
    else:
        return[a, pos-1]

def direction_r(a: str, pos: int):
    if pos == len(a):
        return a, pos
    else:
        return [a, pos+1]
    



res = None
pos_res = pos = 0

for i in b:
    
    if i.isalpha():
        res += i
    
    elif a[pos:pos+2] == '<d':
        a = a[:pos] + a[pos+8:]
        return delete_letter(a, pos)
    
    elif a[pos:pos+2] == '<b':
        a = a[:pos] + a[pos+8:]
        return bspace_letter(a, pos)
    
    elif a[pos:pos+2] == '<l':
        a = a[:pos] + a[pos+6:]
        return direction_l(a, pos)
    elif a[pos:pos+2] == '<r':
        a = a[:pos] + a[pos+7:]
        return direction_r(a, pos)



