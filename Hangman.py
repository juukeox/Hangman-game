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
    print('Incorrect guesses:', self.mistakes_list)
    print('Lives remaining:', (6 - self.mistakes))
    print("")


def main():
  print ('Welcome to Hangman!')
  print ('Enter the difficulty level between 1 (easiest) and 10 (hardest): ', end='')
  difficulty = int(input())
  if difficulty < 1 or difficulty > 10:
    print('Invalid difficulty level. Please enter a number between 1 and 10.')
    return
  words_list = [word.lower() for word in words.words() if difficulty - 1 <= len(word) <= difficulty + 1]
  word = random.choice(words_list).lower()
  hangman = Hangman(word)

  while not hangman.is_game_over():
    print('Guess a letter: ', end='')
    letter = input()
    hangman.guess_letter(letter)
    hangman.print_hangman(letter)

  if set(word) <= set(hangman.guesses):
      print('You won!')
  else:
      print('You lost! The word was:', word)

if __name__ == '__main__':
  main()


  # show guessed letters and don't take it as a mistake.