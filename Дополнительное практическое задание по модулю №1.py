# Задание "Средний балл":
grades =([[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]])
print(grades)
grades =([sum([5, 3, 3, 5, 4])/len([5, 3, 3, 5, 4]), sum([2, 2, 2, 3])/len([2, 2, 2, 3]), sum([4, 5, 5, 2])/len([4, 5, 5, 2]),
          sum([4, 5, 5, 2])/len([4, 5, 5, 2]), sum([5, 5, 5, 4, 5])/len([5, 5, 5, 4, 5])])
students=sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
print(students)
journal={'Aaron':grades[0],'Bilbo':grades[1],'Johnny':grades[2] ,
          'Khendrik':grades[3],'Steve':grades[4]}
print(journal)

#grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#journal= {'Johnny': sum(grades[2])/len(grades[2]),'Bilbo':sum(grades[1])/len(grades[1]),
#         'Steve': sum(grades[4])/len(grades[4]), 'Khendrik':sum(grades[3])/len(grades[3]),
#         'Aaron':sum(grades[0])/len(grades[0])}
#print(journal)

#journal=dict(zip(students, grades))
#print(journal)
