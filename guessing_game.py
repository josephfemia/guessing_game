import random

answer1 = random.randint(1,15)
answer2 = random.randint(1,15)
points = 10

while points > 0:
    user = int(input("Guess a number between 1 and 15.\n"))
    if(user == answer1 or user ==answer2):
        print('You Win!')
        break
    else:
        points -= 1
        print('You have lost 1 point. You have {} points left.'.format(points))

if points == 0:
    print('You lost.')
    print("The two possible answers were {} and {}.".format(answer1, answer2))
