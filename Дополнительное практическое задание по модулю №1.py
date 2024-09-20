# Задание "Средний балл":
grades =([[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]])
print(grades)
grades =([sum([5, 3, 3, 5, 4])/len([5, 3, 3, 5, 4]), sum([2, 2, 2, 3])/len([2, 2, 2, 3]), sum([4, 5, 5, 2])/len([4, 5, 5, 2]),
          sum([4, 5, 5, 2])/len([4, 5, 5, 2]), sum([5, 5, 5, 4, 5])/len([5, 5, 5, 4, 5])])
students=sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
print(students)
journal=dict(zip(students, grades))
print(journal)
#journal={students[0]:grades[0],students[1]:grades[1],students[2]:grades[2] ,
          students[3]:grades[3],students[4]:grades[4]}
#print(journal)




#grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#journal= {'Johnny': sum(grades[2])/len(grades[2]),'Bilbo':sum(grades[1])/len(grades[1]),
#         'Steve': sum(grades[4])/len(grades[4]), 'Khendrik':sum(grades[3])/len(grades[3]),
#         'Aaron':sum(grades[0])/len(grades[0])}
#print(journal)


#print(journal)
