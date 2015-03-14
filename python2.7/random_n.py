import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = input("New number: ")
    if guess > 0:
        if guess > to_be_guessed:
            print "Number too large"
        else:
            print "Number too small"
    else:
        print "Sorry, that you're giving up!"
        break
else:
    print "Congratulation. You made it!"
