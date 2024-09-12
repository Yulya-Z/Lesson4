# Работа со словарями:
my_dict={'Kosty': 2005, 'Rostik' :2014, 'Gena': 1990}
print('Dict:',my_dict)
print('Existing value:',my_dict['Kosty'])
print('Not existing value:',my_dict.get('1900'))
print('Deleted value:',my_dict.get('1900',2014))
my_dict.update({'Olya':1985,
                'Masha':2000})
my_dict.pop('Gena')
print('Modified dictionary:',my_dict)
# Работа с множествами:
my_set_={1,2,3,4,5,False, 'name'}
print('Set:', my_set_)
a=33,58
my_set_.add(a)
my_set_.discard(1)
print('Modified set:', my_set_)




