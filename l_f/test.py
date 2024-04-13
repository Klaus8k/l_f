nickname = input()
len_name = len(nickname) >= 8
num_name = [i.isdigit() for i in nickname]
alfa_name = [i.isalpha() for i in nickname]
lower_name = [i.islower() for i in nickname]
upper_name = [i.isupper() for i in nickname]


def check_rules(data: list):
    count = 0
    for i in data:
        if i == False:
            count += 1
    if len(data) == count:
        return False
    else:
        return True


rules_list = [[len_name,], num_name, alfa_name, lower_name, upper_name]
result = [check_rules(i) for i in rules_list]

print('YES' if all(result) else 'NO')
