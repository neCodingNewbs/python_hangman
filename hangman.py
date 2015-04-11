import re

secret_word = ""
turn_counter = 0
MAX_TURNS = 10
guesses = []
missed_guesses = []
correct_guesses = []
pictures = []

def getSecretWord():

    global secret_word
    
    found_match = 'false'

    while found_match == 'false':
    
        word = input("Please enter the secret word: ")

        match = re.match('[a-zA-Z_]+', word)

        if match:
            secret_word = word
            print ("Thank you, please pass to the next player")
            return;
        else:        
            print("The word wasn't valid")
     
    return;

def currentstate():

    for x in secret_word:
        print ("_",end=" ")

    return;

getSecretWord()

currentstate()
    
        
