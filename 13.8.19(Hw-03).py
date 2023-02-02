N = int(input("количество билетов "))
cost = 0 
Num = 0
while Num<N:
 Age = int(input("Введите возраст посетителя: "))
 if 0 < Age < 18:
        cost += 0
 elif 18 <= Age <= 25:
        cost += 990
 elif Age > 25:
        cost += 1390
 else:
     cost += 0
 if Num >= 2:
     cost = round(cost*0.9,2)
 Num = Num + 1
                # if Num >3:       # cost = cost*0.9#
print("общая стоимость",cost, "руб")
  #  print("Общая стоимость: руб", cost)
