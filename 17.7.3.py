money = int(input("Введите значение"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for value in per_cent:
    deposit.append(int(per_cent[value] * money / 100))

print(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))

