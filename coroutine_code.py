import functools


def is_divider(number):
	print("Coroutine start!!!")
	while True:
		value = yield
		if number % value == 0:
			print(value)


corout = is_divider(95)

corout.send(None)
corout.send(10)
corout.send(11)
corout.send(1)
corout.send(5)
corout.close()


