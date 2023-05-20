#8 В парламентскую комиссию нужно выбрать К членов.
#Претендентов предоставили N партий. Вывести все возможные варианты комиссии
#(от каждой партии должно быть от 1 до 3 членов).

import itertools
K = int(input('Введите колличество членов коммисии ')) #Ввод данных
N = int(input('Введите колличество партий '))
if K < N:
    print("Ошибка ввода")
combinations = set(itertools.combinations_with_replacement(range(N + 1), K)) #Создаём все возможные комбинации
unique_combinations = set(map(tuple, map(sorted, combinations))) #Убираем повторения
for combination in unique_combinations:                    #Добавляем условие от 1 до 3 кандидатов из каждой партии
    if combination.count(0) <= 3 and combination.count(1) <= 3 and combination.count(2) <= 3:
        print(combination)
