#Step 3

import random
word_list = ["aardv_ark", "babo_on", "came_l"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ["_"]*word_length
display_str = ""

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.



#Check guessed letter
won = False
while not won:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    display_str = display_str.join(display)
    print(display_str)
    if display_str == chosen_word:
        won = True
    else:
        display_str = ""
print("You're WON!")
