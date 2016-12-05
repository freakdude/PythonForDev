import random

while True:
    i=0
    question = raw_input('Would you like to play the guessing game? Y or N: ')
    if question == 'y' or question == 'Y':
        print 'Let\'s play the guessing game....\n',
    else:
        break
    randomnumber = random.randint(1,100)
    print randomnumber,'\n'
    while True:
        i += 1
        while True:
            try:
                guess = int(raw_input('Please enter your guess between 1 - 100: '))
                break
            except (ValueError,NameError):
                print 'That was not a valid number. Please try again...'
        if guess == randomnumber:
            if i < 5:
                print 'Good job you guessed correctly in', i,'tries\n'
                break
            else:
                print 'You guessed it right in', i, 'tries but you could do better dumbass!\n'
                break
        elif guess < randomnumber and guess > 0:
            print 'Your guess is low. You have tried', i, 'times!\n'
        elif guess > randomnumber and guess <= 100:
            print 'Your guess is high. You have tried', i, 'times!\n'
        else:
            print'You entered a number that was not between 1 - 100....That counted as a try so you have tried', i, 'times!\n '
    print
print