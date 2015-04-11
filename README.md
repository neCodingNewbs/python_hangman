# python_hangman
 	
OVERVIEW	
"Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters or numbers. The word to guess is represented by a row of dashes, giving the number of letters, numbers and category. If the guessing player suggests a letter or number which occurs in the word, the other player writes it in all its correct positions. If the suggested letter or number does not occur in the word, the other player draws one element of a hanged man stick figure as a tally mark. 

The game is over when:
- An example game in progress; the answer is Wikipedia.
- The guessing player completes the word, or guesses the whole word correctly

The other player completes the diagram:
This diagram is, in fact, designed to look like a hanging man. Although debates have arisen about the questionable taste of this picture,[1] it is still in use today. A common alternative for teachers is to draw an apple tree with ten apples, erasing or crossing out the apples as the guesses are used up.

The exact nature of the diagram differs; some players draw the gallows before play and draw parts of the man's body (traditionally the head, then the torso, then the arms and legs one by one). Some players begin with no diagram at all, and drawing the individual elements of the gallows as part of the game, effectively giving the guessing players more chances. The amount of detail on the man can also vary, affecting the number of chances. Some players include a face on the head, either all at once or one feature at a time.

Some modifications to game play to increase difficulty level are sometimes implemented, such as limiting guesses on high-frequency consonants and vowels. Another alternative is to give the definition of the word. This can be used to facilitate the learning of a foreign language."
	
ASSUMPTIONS	
- The user will have a web browser with access to the internet
- There will be only 2 users competing against each other and both will be human
- Both users have a "grip" of the english language
- We will use english words, letters and whole words only
- There are 9 parts to the hangman and therefore only 9 mistakes could be made the 10th would be dead
- Both Players will use the same computer for their turns
	
TURNS	
- Player 1 enters of a word onto the keyboard, the program then hides the word and replaces it with placeholders
- Player 2 tries to guess the word by entering a letters onto the keyboard
-	If the suggested letter occurs in the word, it will be placed in the correct position within the placeholders.
-	If the letter does not occur in the word, the computer draws one element of the hanged stick man as a tally mark.
-	If the word is guessed within the max. number of wrong turns, Player 2 wins. If the hanged man diagram is completed, Player 1 wins.
	
REQUIREMENTS	
- An interface to enter a word. Validate that its one word, no spaces or numbers and submit the word. 
-	Assign an ID to each letter.
-	Represent each letter with a placeholder ( _ ) before its revealed.
-	Ask Player 2 to guess a letter. --> Reveal it in the word if guessed correctly. If not, add mark to tally and draw the sequential element of the hangman stick figure.
	A list will be kept of all the letters guessed by Player 2
-	Low priority: A graphical representation of the diagram -- based on tally.

WIREFRAMES	
- http://en.wikipedia.org/wiki/Hangman_%28game%29
	
FUNCTIONS	
- Input and store (as lowercase) secret word
-	Validate word
-	Print current state: Starts with blanks as many as there are letters
-	Empty list of guesses with a missed list extension
-	Input method
-	Missed turns tally function
-	Turn variable method
-	Art printing variable method
-	Matching function --> If match, reveal argument --> If not, add to missed list and add +1 to hangman/printing variable
	
VARIABLES	
- secret_word (string)
- turn_counter (integer)
- MAX_TURNS (constant, integer)
- guesses
- missed_guesses (list) --> as integer for hangman drawing
- correct_guesses (list)
- pictures (list, of strings)
