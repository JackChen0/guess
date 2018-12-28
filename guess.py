import random
start = input('Set up the starting value: ')
end = input('Set up the end value: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
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

	