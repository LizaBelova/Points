x1 = float(input("Точка начала отрезка: " ))
x2 = float(input("Точка конца отрезка: " ))
step = float(input("Шаг: " ))
 
if x1 > x2:
	x1, x2 = x2, x1
 
print("Функция: y = -3x**2 - 4x + 20")
print("   x        y")
while x1 <= x2:
	y = -3*x1**2 - 4*x1 + 20
	print('%5.2f | %7.2f' % (x1, y))
	x1 += step
input('enter')