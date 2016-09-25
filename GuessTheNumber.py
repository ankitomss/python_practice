import random

guesses_made=0

name=raw_input('Hello! waht is your name?\n')
number=random.randint(1,20)
print 'well , {0}, I am thinking of a number between 1 and 20.'.format(name)

while guesses_made < 6:

	guess = int(raw_input('take a guess: '))

	guesses_made = guesses_made+1;

	if guess < number:
		print 'your guess is too low'

	if guess > number:
		print 'Your guess is too high'

	if guess == number:
		print 'Weldone you have done it'
		break

if guess == number:
	print 'I am leaving now'
else: 
	print 'you could not guess what I was thinking :P'

