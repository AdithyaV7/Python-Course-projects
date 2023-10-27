import random
from words import words
import string
from hangman_visual import lives_visual_dict

#Get valid word because words.py contain words with "-"
def get_valid_word(words):
    picked_word = random.choice(words) #pick a random word from words list

    while '-' in picked_word or ' ' in picked_word:
        picked_word = random.choice(words) # keep picking word until we get a word without "-" or spaces

    return picked_word.upper() # return the picked word

def hangman():
    word = get_valid_word(words)

    #Sets are similar to a list or tuple
    #Set does not allow duplicate elements

    word_letters = set(word) # get letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #Already guessed leters by user

    lives =7 #Tries in game

    #Get user inputs
    while len(word_letters) >0 and lives >0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #Show current word (ex: W_R_ = WORD)
        word_list =[letter if letter in used_letters else '_' for letter in word ]
        print(lives_visual_dict[lives])
        print("Current Word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters: #valid character that has not used yet add it to the used_letter set
            used_letters.add(user_letter)
            if user_letter in word_letters: # this ensure every right letter guess decrease letters from the word
                word_letters.remove(user_letter)
            else:
                lives =lives-1  #lives decreaases for each wrong guess
                print("Sorry, Wrong Guess")
        
        elif user_letter in used_letters:
            print("You already used that letter, Try Again! ")
        
        else: 
            print("Invalid Character !!!, Try Again")
    
    if lives ==0 :
        print(lives_visual_dict[lives]) # Hang man ascii art
        print("Sorry, You died Correct word is - ",word)
    else:
        print(lives_visual_dict[8])
        print("You Won, Correct word is - ", word)
    
hangman()




