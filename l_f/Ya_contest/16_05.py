a = 'once upon a time, in a land far far away lived a princess , whose beauty was yet unmatched'

# a = ' , , ,,, ,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex'


res_list = []
list_a = []


    
res_a = a

word = ''
for n, i in enumerate(res_a):
    if i.isalpha():
        word += i
    elif i == ' ' and res_a[n+1] == ',':
        word += ','
        list_a.append(word)
        word = ''
    elif i == ' ':
        list_a.append(word)
        word = ''
    elif i == ',':
        word += ','
        list_a.append(word)
        word = ''
        
list_a.append(word)

print(list_a)

l = max(list_a, key=lambda x: len(x))
len_l = len(l)*3

for num, i in enumerate(list_a):

    if i == ',':
        res_list[-1] = res_list[-1]+','
    else:
        res_list.append(i)

print(res_list)

res_res_list = []
res_str = ''

for i in res_list:
    if len(res_str+i+' ') < len_l:
        res_str += (i + ' ')
    elif len(res_str+i) == len_l:
        res_str += i
        res_res_list.append(res_str)
        res_str = ''
    else:
        res_res_list.append(res_str)
        res_str = i + ' '

res_res_list.append(res_str)
[print(i.rstrip()) for i in res_res_list]
