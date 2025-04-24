import random

stages = ['''  
     --------
     |   |
     |   
     |      
     |
     |
     -------
''',
'''
     -------
     |      |
     |      o
     |
     |
     |
     -------
     ''',
     '''
     -------
     |     |
     |     o
     |     |
     |
     | 
     -------            
     ''',
     '''
     -------
     |      |
     |      0
     |      /|
     | 
     | 
     -------
     ''',
     ''' 
     -------
     |      |
     |      o
     |      /|\\
     |
     |   
     ---------
     ''',
     '''
     ---------
     |       |
     |       o
     |      /|\\
     |
     |
     ---------
     ''',
     '''
     ---------
     |        |
     |        o
     |       /|\\
     |
     |
     ----------
     ''',
     '''''']

words = ['apple','mango','banana','orange','grapes','kiwi','pear','plum','berry']

chosen_word = random.choice(words)
word_display = ['_'for _ in chosen_word]
guess_letters = []
lives = len(stages)-1

print("Welcome to Hangman!")
print("Guess tha fruits word")

while True:
    print(" ".join(word_display))
    guess = input("Guess a letters:").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("please enter a valid letter.\n")
        continue
    if guess in guess_letters:
        print("you already guessed that letter.Try again.\n")
        continue
    guess_letters.append(guess)

    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in tha word.")
        for index, letter in enumerate(chosen_word):
          if letter == guess:
                word_display[index] = guess
          else:
               print(f"sorry, '{guess}' is not in tha word.")
               print(stages[len(stages) - lives -1])
               print(f"you have {lives} lives left.")
        lives -=1

        if lives == 0:
            print(stages[lives])
            print(f"you lose! The word was '{chosen_word}'.")
            break
     

