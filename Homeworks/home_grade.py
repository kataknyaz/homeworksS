students = ['Иван', 'Мария', 'Петр', 'Оля']
grades = [85, 92, 76, 89]


average_grades = sum(grades) / len(grades)
print(f'Cредний бал: {average_grades:.2f}')


for i in range(len(grades)):
    if grades[i] > average_grades:
        print(f'Студенты с оценками выше среднего: {students[i]} ')


for i in range(len(grades)):
    if grades[i] < average_grades:
        print(f'Студенты с оценками ниже среднего: {students[i]}')   


        
for i in range(len(grades)):
    if grades[i] == max(grades):  
        print(f'Студент с наивысшей оценкой: {students[i]} {max(grades)} ') 


for i in range(len(grades)):
    if grades[i] == min(grades):  
        print(f'Студент с наивысшей оценкой: {students[i]} {min(grades)} ')         




