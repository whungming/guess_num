import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('guess num: ')
	num = int(num)
	if num == r:
		print('good job!')
		print('you have try', count, 'times')
		break
	elif num > r:
		print('greater than ans')
	elif num < r:
		print('less than ans')
	print('you have try', count, 'times')
