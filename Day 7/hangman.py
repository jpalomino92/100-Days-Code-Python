import random
from hangman_words import word_list
from hangman_art import logo, stages


print(logo)
chosen_word = random.choice(word_list)
display = []
lives = 6
end_game = False



for i in range(len(chosen_word)):
    display.append("_")


while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already choose the letter {guess}. Please choose another one. ")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        print(f" You guessed {guess}, that's not in the word. You lose a life. ")

        lives -= 1
        if lives == 0:
            end_game = True
            print(f" You lose! The word was: {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You Win!")

    print(stages[lives])
