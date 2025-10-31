import random

print("Welcome to number guessing game!")
print("The number is going to be between 0 and 100")

randomNum = random.randint(0,100)
guessCount = 0

def optimalCount(number):
    guessCount = 0
    guessedNumber1 = 50
    guessedNumber2 = 50
    guessedNumber3 = 50
    while True:
        guessCount +=1
        if guessedNumber1 == number:
            print("Great! You won.")
            break
        elif guessedNumber1 < number: #yukarı
            if guessedNumber1 < guessedNumber3:
                guessedNumber2 = guessedNumber1
                guessedNumber1 = int((guessedNumber3 + guessedNumber2)/2)
                
            elif guessedNumber1 < guessedNumber2:
                guessedNumber3 = guessedNumber1
                guessedNumber1 = int((guessedNumber2 + guessedNumber1)/2)
            else:
                guessedNumber1 = guessedNumber1/2 + 50
                
                
        else: #aşağı
            if guessedNumber1 > guessedNumber3:
                guessedNumber2 = guessedNumber1
                guessedNumber1 = int((guessedNumber3 + guessedNumber2)/2)
                
            elif guessedNumber1 > guessedNumber2:
                guessedNumber3 = guessedNumber1
                guessedNumber1 = int((guessedNumber + guessedNumber1)/2)
            else:
                guessedNumber1 = guessedNumber1/2 
                
    return guessCount


while True:
    print("Enter your guess: ")
    guessedNumber = int(input())
    guessCount += 1

    if not guessedNumber < 100 or not guessedNumber>=0:
        print("Please enter a number between 0 and 100!")
    elif guessedNumber == randomNum:
        print("Great! You won.")
        break
    elif guessedNumber > randomNum:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

print("Total attampts: ", guessCount)
print("The optimum attempts it would take: " + str(optimalCount(randomNum)))


