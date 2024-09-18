#2
tuple_immutable_var= 1, 2, 'rus', 'lan'
print(tuple_immutable_var)
#3
#tuple_immutable_var= 1, 2, 'rus', 'lan'
#tuple_immutable_var['rus']=['kruz']
#кортеж относится к неизменным типом данных.
#4
tuple_mutable_list= ([1987],'Ruslan')
print(tuple_mutable_list)
tuple_mutable_list[0][0]=1999
print(tuple_mutable_list)
tuple_mutable_list= (['Ruslan'],1987)
tuple_mutable_list[0][0]='Galimov'
print(tuple_mutable_list)
