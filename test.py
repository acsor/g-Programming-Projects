#!/usr/bin/python3

import unittest
from unittest import TestCase

from problem_picker import ProblemReader


class ProblemReaderTest(TestCase):
    TEST_DIR = "test_fixtures"

    def test_list_components(self):
        """
        Tests that the list of problem suggestions extracted from an arbitrary
        file are those expected.
        """
        filename = self.TEST_DIR + "/README.md"
        expected_list = (
            "Name Generator", "Higher or Lower / Heads or tails", "Temperature Converter", "Calculate your Age in Seconds",
            "Simple Encryption / Decryption", "FizzBuzz", "Rock Paper Scissors and/or Rock Paper Scissors Lizard Spock",
            "Hangman", "Love Calculator", "Pseudorandom Quote Generator",
            "Password Generator", "Atomically Correct Time from an internet clock", "Haiku Generator",
            "Magic Eight Ball", "Collatz Conjecture", "Reverse a string",
            "Count the Vowels in a string", "Count the words in a string", "Minesweeper",
            "Connect Four", "BMI Calculator", "4chan Thread Downloader (Images)",
            "Sodoku Generator / Solver", "Maze Game and Solution Algorithm", "Decimal to Binary",
            "Picross Solver", "Eulerian Path", "Fibonnaci Sequence Algorithm",
            "Calculate and Print the Factorial of 100", "Encryption Collection. Implement all of the tools in the Rumkin Collection: http://rumkin.com/tools/cipher/", "Blackjack",
            "Text Adventure Game", "Generate an ASCII image of a Christmas tree to a user given height.", "Area Calculator",
            "Benfords Law", "Hunt the Wumpus", "Static Website Generator",
            "Crossword Game", "NTP Server", "Stronger Password Generator (With less chance of predicting an outcome)",
            "Find the largest number in an array, and print its position", "ASCII Analogue Clock", "Dijkstra's Algorithm",
            "Text to Morse translator. Bonus points for generating the sound.", "Noughts and Crosses / Tic Tac Toe / X and O", "Snake Game",
            "FTP Client (TCP or UDP with ACK)", "Telnet Server", "IMP Interpreter",
            "Tetris", "Conway's Game of Life", "Web Crawler", "Text Editor", "RSS Feed Creator", "Evaluate Binomial Coefficients",
            "Reverse Polish Notation (RPN) Calculator", "Output the Mandlebrot Set in ASCII", "Sorting Algorithm",
            "Convert Markup to HTML", "The N Queens Problem", "Details Validatior using Regular Expressions. Validate Phone numbers, emails, names etc.",
            "Linked List", "Mastermind", "Random Image Generator", "last.FM Scrobbler", "Klingon Translator", "Prime Number generator using a Sieve",
            "Markov Chain", "Graphical Digital Clock (GUI)", "Oil Spill Game", "Algorithm to calculate Triangle Numbers",
            "Calculate a users typing speed", "Name Art in ASCII", "Towers of Hanoi", "Quine", "IRC Bot", "Brainfuck Interpreter",
            "Sorting Algorithm Audibilization and/or Visualisation", "Chip-8 Emulator", "Geekcode Generator (3.12)",
            "Define, translate and rotate a shape with an arbitrary amount of vertices", "Pong with Variable Vectors",
            "Battleships with an Artificial Intelligence (NPC) opponent. Make sure they're beatable.",
            "Simple Rougelike. Mega chapeau for multiplayer over LAN.", "TCP chat program with basic encryption (XOR)",
            "Incremental Economy Simulator (Look up Time of Exploration)", "Encryption / Decryption Hiding text in an image",
            "Calculate Pascals Triangle", "Sine Wave Generator from Pseudorandom Numbers", "Pacman Clone with Ghost AI", "Flappy Birds Clone",
            "Fast Fourier Transform", "Graphical Digital Clock (GUI) that allows the user to set alarms and change colors",
            "Binary Search / Binary Search Tree", "Nintendo Oil Panic", "Generate the Sierpinski Triangle", "Calculate the Dot and Cross of two Vectors",
            "Little Man Computer Simulator", "Basic LISP Interpreter", "Hailstone Sequence",
        )
        p = ProblemReader(filename)
        computed_list = tuple(p)

        self.assertTupleEqual(expected_list, computed_list)

    def test_end_before_start_tag(self):
        """
        Tests that ProblemReader correctly raises ValueError
        when an end tag is incorrectly placed before a start tag.
        """
        filename = self.TEST_DIR + "/End_before_start_tag.md"
        p = ProblemReader(filename)

        with self.assertRaises(ValueError):
            next(iter(p))

    def test_no_start_tag(self):
        """
        Tests that ProblemReader correctly raises ValueError
        when no start tag (<ol>) is found in a source file.
        """
        filename = self.TEST_DIR + "/No_start_tag.md"
        p = ProblemReader(filename)

        with self.assertRaises(ValueError):
            next(iter(p))

    def test_missing_source_file(self):
        """
        Tests that ProblemReader.__init__() correctly raises ValueError
        when the filename argument points to an unexisting or unreadable file.
        """
        filename = "@!#111101011"

        with self.assertRaises(ValueError):
            ProblemReader(filename)


if __name__ == "__main__":
    unittest.main()
