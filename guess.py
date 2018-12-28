import random
r = random.randint(1,100)
count = 0
while True:
	g = input('Enter your number: ')
	count = count + 1
	print('This is your',count,'time')
	g = int(g)
	if g == r:
		print('You are right !!!')
		break
	elif g > r:
		print('Your number is bigger than mine.')
	else:
		print('Your number is smaller than mine.')

	