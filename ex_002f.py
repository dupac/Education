'''
# Чек

Сдачу посчитать, конечно, все могут, но красивый чек напечатать — не так просто.

## Формат ввода

- название товара;
- цена товара;
- вес товара;
- количество денег у пользователя.

## Формат вывода

Чек  
<название товара> - <вес>кг - <цена>руб/кг  
Итого: <итоговая стоимость>руб  
Внесено: <количество денег от пользователя>руб  
Сдача: <сдача>руб

### Пример 1


Ввод

черешня
2
3
10
 
Вывод

Чек
черешня - 3кг - 2руб/кг
Итого: 6руб
Внесено: 10руб
Сдача: 4руб


### Пример 2


Ввод

манго
187
43
8041

Вывод

Чек
манго - 43кг - 187руб/кг
Итого: 8041руб
Внесено: 8041руб
Сдача: 0руб
'''
#---
'''
name = input("Название товара: ")
price = int(input("Цена товара: "))
quntity = int(input("Вес товара: "))
cash = int(input("Наличные: "))
sum = price * quntity
change = cash - sum
print("Чек","\n",name, "-", quntity, "кг -" , price, "руб/кг\n","Итого:",sum,"руб\n","Внесено:",cash,"руб\n","Сдача:",change,"руб\n")
'''
#---

'''
name = input("Название товара: ")
price = int(input("Цена товара: "))
quantity = int(input("Вес товара: "))
cash = int(input("Наличные: "))
total = price * quantity
change = cash - total
print("Чек")
print(name, "-", quantity, "кг -", price, "руб/кг")
print("Итого:", total, "руб")
print("Внесено:", cash, "руб")
print("Сдача:", change, "руб")
'''

'''
tovar = input()
price = int(input())
ves = int(input())
summ = int(input())
kgves = price * ves
sdacha = summ - kgves

print("Чек")
print(str(tovar + " - " + ves + "кг" + " - " + price + "руб/кг"))
print("Итого: " + str(kgves) + "руб")
print("Внесено: " + str(summ) + "руб")
print("Сдача: " + str(sdacha) + "руб")

'''

name = input()
price = int(input())
quantity = int(input())
cash = int(input())
total = price * quantity
change = cash - total
print("Чек")
print(str(name) + " - " + str(quantity) + "кг" + " - " + str(price) + "руб/кг")
print("Итого: " + str(total) + "руб")
print("Внесено: " + str(cash) + "руб")
print("Сдача: " + str(change) + "руб")

