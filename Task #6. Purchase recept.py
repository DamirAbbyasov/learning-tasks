name = input()
price = int(input())
weight = int(input())
buyer_has = int(input())
cost = price * weight
change = buyer_has - cost
print(f"Чек\n{name} - {weight}кг - {price}руб/кг\nИтого: {cost}руб\nВнесено: {buyer_has}руб\nСдача: {change}руб")
