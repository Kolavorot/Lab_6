# В парламентскую комиссию нужно выбрать К членов.
# Претендентов предоставили N партий.
# Вывести все возможные варианты комиссии
# (от каждой партии должно быть от 1 до 3 членов).

# Дополнительное условие: от 1 партии должно быть 3 человека

# Целевая функция: найти максимальный рейтинг комиссии

def generatecombinations(n, k):
    parties = [str(i) for i in range(1, n + 1)]
    combinations = []
    generate_combination_recursive(parties, k, [], combinations)
    return combinations

def generate_combination_recursive(parties, k, currentcombination, combinations):
    if len(currentcombination) == k:
        for party in parties:
            if party not in currentcombination:
                return
        combinations.append(''.join(currentcombination))
        return
    for digit in parties:
        if currentcombination.count(digit) < 3:
            currentcombination.append(digit)
            generate_combination_recursive(parties, k, currentcombination, combinations)
            currentcombination.pop()

def suma(combination):
    m = str(combination)
    s = 0
    for i in range(len(combination)):
        s += int(m[i])
    return s

n = int(input("Введите количество партий "))
k = int(input("Введите колличество кандидатов "))
if n * 3 < k or n < 5:
    print("Ошибка ввода")
    exit()
else:
    combinations = generatecombinations(n, k)
    print("\nВсевозможные варианты комиссии:")
    a = []
    b = []
    for combination in combinations:
        l = str(combination)
        if '1' in l:
            l = l.replace('1', '', 1)
            if '1' in l:
                l = l.replace('1', '', 1)
                if '1' in l:
                    a.append(combination)
                    b.append(suma(combination))
                    print("Комиссия ",combination, "Её рейтинг = ", suma(combination))
    max_value = max(b)
    max_index = b.index(max_value)
    print("\nКомиссия с максимальным рейтингом ", a[max_index])
    print("Рейнтиг этой комиссии =", b[max_index])



