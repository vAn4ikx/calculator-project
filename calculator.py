#Улучшенный калькулятор
def get_number(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Ошибка: введите число")
def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	if b!=0:
		return a/b
	else:
		return "Ошибка: деление на ноль"
def power(a,b):
	return a**b
def square_root(a):
	return a**0.5
#Основная программа
printf("Улучшенный калькулятор")
printf("Доступные операции:+,-,*,/,^,sqrt")
