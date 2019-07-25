import random

r = random.randint(1, 100)
while True:
	num = input('guess num: ')
	num = int(num)
	if num == r:
		print('good job!')
		break
	elif num > r:
		print('greater than ans')
	elif num < r:
		print('less than ans')
