per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("введите сумму"))
bank1 = int((money / 100) * (per_cent['ТКБ']))
bank2 = int((money / 100) * (per_cent['СКБ']))
bank3 = int((money / 100) * (per_cent['ВТБ']))
bank4 = int((money / 100) * (per_cent['СБЕР']))
deposit = [bank1, bank2, bank3, bank4]
print(deposit)
max_number = max(deposit)
print("Наибольшая доходность по вкладу:", max_number)
