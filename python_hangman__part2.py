turn_counter = 0

def run_game:
    #get input
    #validates
 #loop
    turn = #turn generator
    #turn display(tur
    #print art
    #user input
    #check word
    #t
    #check for end/win




def turn_generator(correct_guesses, missed_guesses):

    turn_counter = correct_guesses + missed_guesses + 1
    return turn_counter

def turn_display(turn_counter):
    print("It is now turn " + str(turn_counter))
    print(art[len(missed_guesses)-1])
    print(

def check_word(user_input, secret_word, under_score):
    for i in range(0:len(secret_word)-1):
        if secret_word[i] == user_input:
            under_score[i] = user_input
            return under_score
        else:
            missed_guesses.append(user_input)
            return missed_guesses
