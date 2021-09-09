def tt(**kwargs):
    print(kwargs)
tt(key={'test': 1}, test={'tes': 2})
a = {}
b = {}

def dictf(**kwargs):
    my_dicts = []
    my_dicts.append(kwargs["key"])
    my_dicts.append(kwargs["key2"])
    return my_dicts

a = {'lexus':570, 'lexus':470}
b = {'white':3, 'black':4}
print(dictf(key=a, key2=b))