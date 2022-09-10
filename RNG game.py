import random
number = random.randint(1,10)
player_name = input("Hello! What is your name?")
number_of_guesses = 0
print("Hello"+ player_name +", I am guessing a number between 1 and 10.")
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("This number is too small")
    elif guess > number:
        print("This number is too high")
    elif guess == number:
        print("Correct!!")
        break
if guess == number:
    print("You got the number, and you got it in "+ str(number_of_guesses)+ " tries!")
else:
    print("You did not get the number, the number is actually"+ str(number)+ ".")