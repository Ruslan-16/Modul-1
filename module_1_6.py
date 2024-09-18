#2
my_dict={'Ruslan': 1987, 'Regina': 1989, 'Danis': 2022, 'Niki': 2020}
print(my_dict)
print(my_dict.get('Ruslan'))
print(my_dict.get('Max'))
my_dict.update({'Regin':1979,
'Alex':1980})
print(my_dict)
a= my_dict.pop('Regin')
print(my_dict)
print(a)
#3
my_set={'rus','lan','rus','reg',1987,1989,1989}
print(my_set)
my_set.add(2022)
my_set.add('Niki')
print(my_set)
my_set.discard('lan')
print(my_set)
