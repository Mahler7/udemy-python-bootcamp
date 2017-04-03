my_dict = {'key1':'value', 'key2': 'value2'}
print(my_dict)
print(my_dict['key1'])
my_dict2 = {'k1':123, 'k2':3.4, 'k3':'string'}
print(my_dict2)
print(my_dict2['k3'])
print(my_dict2['k3'][::-1])
print(my_dict2['k1'] - 120)
my_dict2['k1'] = my_dict2['k1'] - 120
print(my_dict2)
d = {}
d['animal'] = 'dog'
d['answer'] = 42
print(d)
e = {'k1': {'nestkey': {'subnestkey': 'value'}}}
print(e)
print(e['k1']['nestkey']['subnestkey'])
f = {"k1": 1, "k2": 2, "k3":3}
print(f.keys())
print(f.values())