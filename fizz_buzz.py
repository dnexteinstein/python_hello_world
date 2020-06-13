print('Print Fizz, Buzz or FizzBuzz when value is divisible by 3, 5 and (3 & 5) respectively')
for i in range(151):
	if i % 3 == 0 and not i % 5 == 0:
		print('Fizz')

	elif i % 5 == 0 and not i % 3 == 0:
		print('Buzz')

	elif i % 3 == 0 and i % 5 == 0:
		print('FizzBuzz')