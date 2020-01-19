"""name=input("Please enter your name:")
myvar="qa"
age =int(input("How old are you, {0}".format(name)))
print(age)

if age>=18:
    print("you are old enough to vote")
    print("Please put X in the box")
else:
    print("Please come back in {0} years".format(18-age))
"""

print("please Guess a number between 1 and 10: ")
guess=int(input())
if guess !=5:
    if guess<5:
        print("please guess higher")
    else:
        print("Please guess Lower")
    guess=int(input())
    if guess ==5:
        print("well done, you guessed it ")
    else:
        print("sorry, you have not guess correctly")
else:
    print("you got it first time")

