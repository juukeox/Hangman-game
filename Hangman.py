import random
import time
import nltk

nltk.download('words')
from nltk.corpus import words


class Hangman:
  def __init__(self, word):
    self.word = word
    self.guesses = []
    self.mistakes = 0
    self.mistakes_list = []
    self.win = False

  def guess_letter(self, letter):
    if letter in self.word:
      self.guesses.append(letter)
    else:
      self.mistakes += 1
      self.mistakes_list.append(letter)

  def is_game_over(self):
    return self.mistakes == 6 or self.word == ''.join(self.guesses)

  def print_hangman(self, letter):
    if letter in self.word: 
      print('Correct!')
    else:
      print('Incorrect!')
    print("")
    display_word = ''
    for char in self.word:
        if char in self.guesses:
            display_word += char
        else:
            display_word += '_'
    print(display_word)
    print("")
    incorrect_guesses = ', '.join(self.mistakes_list)
    print('Incorrect guesses:', incorrect_guesses)
    print('Lives remaining:', (6 - self.mistakes))
    print("")


def main():
  print ('Welcome to Hangman!')
  while True:
      try:
        difficulty = int(input('Enter the difficulty level between 1 (easiest) and 10 (hardest): '))
        if 1 <= difficulty <= 10:
          break
        else:
            print('Invalid difficulty level. Please enter a number between 1 and 10.')
      except ValueError:
       print('Invalid input. Please enter a valid number.')  

  words_list = [word.lower() for word in words.words() if difficulty - 1 <= len(word) <= difficulty + 1]
  word = random.choice(words_list).lower()
  hangman = Hangman(word)

  while not hangman.is_game_over():
    print('Guess a letter: ', end='')
    letter = input().lower()
    hangman.guess_letter(letter)
    hangman.print_hangman(letter)

  if set(word) <= set(hangman.guesses):
      print('You won!')
  else:
      print('You lost! The word was:', word)

if __name__ == '__main__':
  main()


  # Add function to reject/not punish for repeated guesses?