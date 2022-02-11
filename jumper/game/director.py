# from game.terminal_service import TerminalService
from game.player import Player
from game.puzzle import Puzzle


class Director:
   """
   A person who directs the game. 
   
   The responsibility of a Director is to control the sequence of play.

   Attributes:
      hider (Hider): The game's hider.
      is_playing (boolean): Whether or not to keep playing.
      seeker (Seeker): The game's seeker.
      terminal_service: For getting and displaying information on the terminal.
   """

   def __init__(self):
      """
      Constructs a new Director.
      
      Args:
         self (Director): an instance of Director.
      """
      self._player = Player()
      self._is_playing = True
      self._player_guess = " "
      self._puzzle = Puzzle()
      self._guess_correct = False
      
   def start_game(self):
      """
      Starts the game by running the main game loop.
      
      Args:
         self (Director): an instance of Director.
      """
      while self._is_playing:
         self._get_inputs()
         self._do_updates()
         self._do_outputs()

   def _get_inputs(self):
      """
      Gets the letter guess from the player.

      Args:
         self (Director): An instance of Director.
      """
      self._player_guess = self._player.guess_letter()

   def _do_updates(self):
      """
      Has the puzzle check the letter guess from the player and checks to
      see if the puzzle has been solved. If so the game will end.

      Args:
         self (Director): An instance of Director.
      """
      self._guess_correct = self._puzzle.check_guess(self._player_guess)
      self._is_playing = not self._puzzle.is_solved()
      
   def _do_outputs(self):
      """
      Has the puzzle show the word with user guesses and has the player
      draw the jumper. Checks to see if the player is still alive. If the
      player is not alive the game will end.

      Args:
         self (Director): An instance of Director.
      """
      self._puzzle.show_word()     
      self._player.draw(self._guess_correct)
      self._is_playing = self._player.is_alive()