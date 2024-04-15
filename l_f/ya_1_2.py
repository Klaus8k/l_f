a = 'hellochild'
b = 'helto<left><bspace>l<delete>ochilds<bspace>'
b = 'ooo<left><left>l<left><bspace>l'
b = '<left><left><left><bspace>ooo<bspace>aaaaaa<left><left><left>o<right>е<delete><delete><delete><delete><right><right><right><delete>'

res = []
pos = pos_res = 0

while True:
    
    if pos > len(b)-1:
        break
    
    if b[pos].isalpha():
        res.insert(pos_res, b[pos])
        pos += 1
        pos_res += 1
  
    if b[pos:pos+2] == '<b':
        if pos_res != 0:
            pos += 8
            pos_res -= 1
            del res[pos_res]
        else:
            pos += 8
            continue

    elif b[pos:pos+2] == '<d':
        print(pos_res, res)
        if pos_res <= len(res)-1:
            pos += 8
            del res[pos_res]
        else:
            pos += 8
            continue
        
    elif b[pos:pos+2] == '<l':
        if pos_res != 0:
            pos_res -= 1
            pos += 6
        else:
            pos += 6
            continue
        
    elif b[pos:pos+2] == '<r':
        if pos_res <= len(res)-2:
            pos_res += 1
            pos += 7
        else:
            pos += 7
            continue
        

print(res)