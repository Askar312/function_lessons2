dic = {'lexus': 'toyota', 789: 'white'}

def take_tuples(dic):

    keys = set(dic.keys())

    values = set(dic.values())

    return keys, values

print(take_tuples(dic))