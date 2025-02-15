# 1 задание
# students = [
#     {'name': 'Максимилиан', 'average_grade': 534},
#     {'name': 'Александр', 'average_grade': 235},
#     {'name': 'Роман', 'average_grade': 828},
#     {'name': 'Алексей', 'average_grade': 812},
#     {'name': 'Семен', 'average_grade': 800},
#     {'name': 'Екатерина', 'average_grade': 823},
#     {'name': 'Данил', 'average_grade': 592},
#     {'name': 'Арсений', 'average_grade': 383},
#     {'name': 'Герман', 'average_grade': 745}
# ]

# def bubble_sort(students):
#     n = len(students)
#     for i in range(n-1):
#         for j in range(n-1):
#             if students[j]['average_grade'] > students[j+1]['average_grade']:
#                 students[j], students[j+1] = students[j+1], students[j]

# bubble_sort(students)

# for student in students:
#     print(f"{student['name']}: {student['average_grade']}")






# 2 задание    
# temperatures = [15, 13, 20, 14, 17, 22, 13, 7, 13.5, 10, 5, 15, 16, 21, 22, 20, 11, 6, 1, 4, 9, 12, 16, 25, 26, 23, 21, 23, 18, 13]

# def bubble_sort(temperatures):
#     n = len(temperatures)
#     for run in range(n-1):
#         for i in range(n-1):
#             if temperatures[i] > temperatures[i+1]:
#                 temperatures[i], temperatures[i+1] = temperatures[i+1], temperatures[i]

# bubble_sort(temperatures)

# print(f'Отсортированный список температур: {temperatures}')  





# 3 задание
# sentence = 'слова в предложении по алфавиту'
# words = sentence.split()

# def bubble_sort(words):
#     n = len(words)
#     for run in range(n-1):
#         for i in range(n-1):
#             if words[i] > words[i+1]:
#                 words[i], words[i+1] = words[i+1], words[i]

# bubble_sort(words)

# print(f'слова в предложении по алфавиту: {words}')  





# 4 задание
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i 
    return -1    


numbers = [ 3, 5, 2, 8, 1, 22, 40, 50]
target = 17
result = linear_search(numbers,target)


if result != -1:
    print(f'Элемент {target} найден на позиции {result}')
else:   
    print(f'Элемент {target} не был найден')