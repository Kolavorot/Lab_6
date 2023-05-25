# В парламентскую комиссию нужно выбрать К членов.
# Претендентов предоставили N партий.
# Вывести все возможные варианты комиссии
# (от каждой партии должно быть от 1 до 3 членов).

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


n = int(input("Введите количество партий "))
k = int(input("Введите колличество кандидатов "))
if n * 3 < k:
    print("Ошибка ввода")
    exit()
combinations = generatecombinations(n, k)
print("\nВсевозможные варианты комиссии: ")
for combination in combinations:
    print(combination)