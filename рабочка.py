# int() числа
#float() дробные числа
#str() строки
#[]
#[::]
# //-целая часть от деления
# %-остаток от деления
# **-
# input() взаимодействоать с пользователем
# print(f'меня зовут{name},мне {age})
# .add- добавить
# set- множество
# dict- словарь
# True-1
# fols-0
#
#
#
#
#
#
#
#
#
#
#
#
#
# Задание "Средний балл":
grades =([[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]])
print(grades)
#Чтобы найти среднее число "sum/len"
grades =([sum([5, 3, 3, 5, 4])/len([5, 3, 3, 5, 4]), sum([2, 2, 2, 3])/len([2, 2, 2, 3]), sum([4, 5, 5, 2])/len([4, 5, 5, 2]),
          sum([4, 4, 3])/len([4, 4, 3]), sum([5, 5, 5, 4, 5])/len([5, 5, 5, 4, 5])])

# Чтобы отсортировать "sorted"
students=sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
print(students)

# Чтобы создать словарь из grades и students, необходимо использовать функцию, students_and_grades = "dict(zip(students, grades))"
#dict это словарь - мы объявляем формат переменной (как с int и str),zip - фуункция которая собирает объединяет списки в один
journal=dict(zip(students, grades))

#Лучше так!
journal={students[0]:grades[0],students[1]:grades[1],students[2]:grades[2] ,
         students[3]:grades[3],students[4]:grades[4]}
print(journal)


