import random

print("\n-------- Welcome to Hangman Game ---------\n")

def getName():
    global name
    name = input("Please enter your user name: ")
    
def sayWelcome(name):
    return print("Welcome {}".format(name))

getName()
sayWelcome(name)

words = ["global","artificial","intelligence","python","reinforcement"]
word = random.choice(words)

numberOfPrediction = 5

letters = []

x = len(word)

z = list('_'*x)

print(' '.join(z), end="\n")

while numberOfPrediction > 0:
    y = input("\nPlease guess a letter: ")
    if y in letters:
        print("Please do not guess the letters you guessed earlier.")
        continue

    elif len(y) > 1:
        print("Please just enter one letter.")
        continue
    
    elif y not in word:
        numberOfPrediction -= 1
        print("wrong guess!. You have {} guesses left".format(numberOfPrediction))
        
    else:
        for i in range(len(word)):
            if y == word[i]:
                print("Right guess")
                z[i] = y
                letters.append(y)
                                  
                
       
        print(' '.join(z), end='\n')


    result = input("Do you want to guess the whole word? ['y' or 'n']: ")

    if result == "y":
        prediction = input("You can guess the whole word: ")
        if prediction == word:
            print("Congratulations")
            break
        else:
            numberOfPrediction -=1
            print("wrong guess!. You have {} guesses left".format(numberOfPrediction))
            
    if numberOfPrediction == 0:
        print("You are out of guesswork")
        break


        

