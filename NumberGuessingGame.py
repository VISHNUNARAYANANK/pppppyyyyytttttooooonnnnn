#importing necessary lib
import random

#create a random number

rand_num = random.randrange(1,10)

#get input from user

guess = int(input("enter your guess"))

#get input from user until it matches with the random number

while (guess  != rand_num):

    if guess < rand_num:

        print("too low")
        guess = int(input("enter your guess again"))

    elif guess > rand_num:

        print("too high")
        guess = int(input("enter your guess again"))

    else:

        break

print("you have guessed it right!!")