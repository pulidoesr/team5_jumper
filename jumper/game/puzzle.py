import random
from game.terminal_service import TerminalService


class Puzzle:
    """The player looking for the letters . 
    
    The responsibility of a Puzzle is to keep track of the letters of the word.
    
    Attributes:
        guess_word (char): The word to guess.
        word_letters (List[char]): The list of letters of the word.
        word_list (List[char]): The list of words to select
    """

    def __init__(self):
        """Constructs a new Puzzle.
        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._selection = random.randint(0, 9)
        self._list_word = ['world', 'cars', 'window', 'door', 'cats', 'dogs', 'house', 'tower', 'court', 'palace']
        self._word = ''
        self._letters_word = []
        self._guess_word = []
        self._terminal_service = TerminalService()
        self._guessword = ''
        self._continue = True
    def get_puzzle(self):
        """ Gets the random word from list
            Build the list to check the letters
            Build the list to track the guesses
        """
        if self._word == '':
            self._word = self._list_word[self._selection]
            i = 0 
            while i < len(self._word):
                self._letters_word.append(self._word[i:i+1])
                self._guess_word.append("_ ")
                i += 1
        return self._word
        
    def check_guess(self, letter):
        """Use the letters of the word in the list
           Keep track of the letters found and their position
           Review if there is a repeated letter 
           Update the letter in the right position of the word
           Returns:
                   True or False (letter found)
        """
        self._is_found = False
        i = 0
        while i < len(self._word):
            if self._letters_word[i] == letter:
                if self._guess_word[i] == '_ ':
                   self._guess_word[i] = letter
                   self._is_found = True
                   break
            i += 1
        return self._is_found

    def show_word(self):
        """ Concatenate letters to show it
            Check if the word has been discovered
            Set the end of game if the word has been discovered 
         """
        i = 0
        self._guessword = ''
        while i < len(self._guess_word):
            self._guessword = self._guessword + self._guess_word[i]
            i += 1
        self._terminal_service.write_text(self._guessword)   
    def is_solved(self):
        if self._guessword == self._word:
           self._continue = False
        return self._continue

