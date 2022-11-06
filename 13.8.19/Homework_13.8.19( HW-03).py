price_for_all = 0
while True:
    try:
        ticket_number = input('Введите количество билетов')
        ticket_number = int(ticket_number)
        if type(ticket_number) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age_for_ticket = input('Для какого возраста билет № {i}?')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('Билет бесплатный')
            elif 25 > age_for_ticket >= 18:
                price_for_all += 990
                print('Стоимость билета: 990 руб')
            else:
                price_for_all += 1390
                print('Стоимость билета: 1390 руб')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_number > 3:
    discount_price = price_for_all - ((price_for_all / 100) * 10)
    print(f'Сумма к оплате {discount_price} руб (С учетом 10%-ой скидки на полную стоимость заказа'
          f' за покупку более трех билетов).')
else:
    print(f'Сумма к оплате {price_for_all} руб.')