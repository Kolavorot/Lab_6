#8 В парламентскую комиссию нужно выбрать К членов.
#Претендентов предоставили N партий. Вывести все возможные варианты комиссии
#(от каждой партии должно быть от 1 до 3 членов).

import itertools
K = int(input('Введите колличество членов коммисии '))
N = int(input('Введите колличество партий '))
combinations = set(itertools.combinations_with_replacement(range(N + 1), K))
unique_combinations = set(map(tuple, map(sorted, combinations)))
for combination in unique_combinations:
    if combination.count(0) <= 3 and combination.count(1) <= 3 and combination.count(2) <= 3:
        print(combination)
