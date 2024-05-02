import random
import hangman_art
import hangman_words

word = random.choice(hangman_words.word_list)
word_length = len(word)
blank_word = []
lives = 6

print(hangman_art.logo)
for i in range(word_length):
    blank_word.append('_')
print(blank_word)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in blank_word:
        print(f"You have already guessed {guess}")
    for position in range(word_length):
        if word[position] == guess:
            blank_word[position] = guess

    if guess not in word:
        print(f"That letter is not in the word: {guess}. You ;ose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost!")
            print("The word was", word)

    print(blank_word)
    if "_" not in blank_word:
        end_of_game = True
        print("You guessed the word!")

    print(hangman_art.stages[lives])