money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
money_for_month = salary + money_capital  # Деньги, которые мы имеем в нашем распоряжении
count = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_for_month > spend:
    money_for_month -= spend
    money_for_month += salary
    spend += spend * 0.05
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
