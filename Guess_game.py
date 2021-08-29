import random

range_num = input("Type a Number: ")
if range_num.isdigit():
    range_num = int(range_num)

    if range_num <=0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,range_num)
gues=0

while True:
    gues +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it !")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")


print("You got it in",gues,"Guesses :)")
