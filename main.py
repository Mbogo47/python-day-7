import random
from hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6

display = []

word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter:").lower()
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word. You lose a life.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    

    if not guess == letter:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f'Your word was {chosen_word}')


    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
