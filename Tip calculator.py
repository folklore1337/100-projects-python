
number_of_people = int(input("Введите количество людей: "))
tips = float(input("Чаевые(в процентах(10,20,30)): "))
total_price = float(input("Общая цена: "))

t = total_price * (tips / 100)
i = t + total_price
r = i // number_of_people

print(r)