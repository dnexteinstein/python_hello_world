for i in range(200):
	if i % 3 == 0 and not i % 5 == 0:
		print('Fizz')

	elif i % 5 == 0 and not i % 3 == 0:
		print('Buzz')

	elif i % 3 == 0 and i % 5 == 0:
		print('FizzBuzz')