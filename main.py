import random
random.randint(1,100)
print("Welcome to guess the number game")

print("Level 0")
n = random.randint(1,100)
i = 10
while i > 0:
    print("No. of chances left",i)
    guess = int(input("Guess the no. between 1 and 100: "))

    if guess>n:
        print("your guess is too high")

    elif guess<n:
        print("your guess is too low")

    elif guess==n:
        print("your guess is correct",'\nIn no.of chances you guess',i)
        break
    i-=1
    if i == 0:
        print("you lose")
        break
   


print("Level 1")

n = random.randint(1,200)
i = 10
while i > 0:
    print("No. of chances left",i)
    guess = int(input("Guess the no. between 1 and 200: "))

    if guess>n:
        print("your guess is too high")

    elif guess<n:
        print("your guess is too low")

    elif guess==n:
        print("your guess is correct",'\nIn no.of chances you guess',i)
        break
    i-=1
    if i == 0:
        print("you lose")
        break

print("Level 2")
n = random.randint(1,300)
i = 10
while i > 0:
    print("No. of chances left",i)
    guess = int(input("Guess the no. between 1 and 300: "))

    if guess>n:
        print("your guess is too high")

    elif guess<n:
        print("your guess is too low")

    elif guess==n:
        print("your guess is correct",'\nIn no.of chances you guess',i)
        break
    i-=1
    if i == 0:
        print("you lose")
        break
print("Level 3")
n = random.randint(1,400)
i = 10
while i > 0:
    print("No. of chances left",i)
    guess = int(input("Guess the no. between 1 and 400: "))

    if guess>n:
        print("your guess is too high")

    elif guess<n:
        print("your guess is too low")

    elif guess==n:
        print("your guess is correct",'\nIn no.of chances you guess',i)
        break
    i-=1
    if i == 0:
        print("you lose")
        break
print("Level 4")
n = random.randint(1,500)
i = 10
while i > 0:
    print("No. of chances left",i)
    guess = int(input("Guess the no. between 1 and 500: "))

    if guess>n:
        print("your guess is too high")

    elif guess<n:
        print("your guess is too low")

    elif guess==n:
        print("your guess is correct",'\nIn no.of chances you guess',i)
        break
    i-=1
    if i == 0:
        print("you lose")
        break
print(" Last Level")
n = random.randint(1,10000)
i = 10
while i > 0:
    print("No. of chances left",i)
    guess = int(input("Guess the no. between 1 and ?: "))

    if guess>n:
        print("your guess is too high")

    elif guess<n:
        print("your guess is too low")

    elif guess==n:
        print("your guess is correct",'\nIn no.of chances you guess',i)
        break
    i-=1
    if i == 0:
        print("you lose")
        break
