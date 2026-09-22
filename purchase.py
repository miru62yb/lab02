price=int(input('Введите цену одной тетради в рублях: '))
count=int(input('Введите количество тетрадей: '))
paid=int(input('Введите сумму, которую вы заплатили в рублях: '))
short_change = paid - price * count
sale = price * count
print(f'Сумма покупки: {sale} рублей')
print(f'Ваша сдача: {short_change} рублей')
