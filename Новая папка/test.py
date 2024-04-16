import unittest
import tkinter as tk
from game import Game
import game
from unittest.mock import patch
import sys


class TestGame(unittest.TestCase):
    def setUp(self):
        self.win = tk.Tk()
        self.win.level = tk.Label(self.win)
        self.game = game.Game(self.win, 1, 'Vika')

    #Тест на правильный переход на уровень выше
    def test_level_up(self):
        self.game.level = 2
        self.game.level_up()
        self.assertEqual(self.game.level, 3)

    #Тест на правильный переход на уровень 1 после победы
    def test_level_up_4(self):
        self.game.level = 4
        self.game.level_up()
        self.assertEqual(self.game.level, 1)

    #тест на правельную генерацию значений
    @patch('random.randint', return_value=3)
    def test_generation(self, mock_randint):
        self.game.level = 1
        result = self.game.generation()
        expected = [3, 3, 3, 3, 3, 3]
        self.assertEqual(result, expected)

    #тест на неправельную генерацию значений
    @patch('random.randint', return_value=4)
    def test_generation_false(self, mock_randint):
        self.game.level = 1
        result = self.game.generation()
        expected = [3, 3, 3, 3, 3, 3]
        self.failIfEqual(result, expected)

    # @patch('game.Game.level_up')
    # @patch('game.Game.show_modal_window_true')
    # @patch('game.Game.show_modal_window_false')
    # @patch('tkinter.messagebox.showinfo')
    # @patch('tkinter.Entry.get', return_value='3')
    # def test_checking(self, mock_get, mock_showinfo, mock_false, mock_true, mock_level_up):
    #     self.game.arr = ['3', '3', '3', '3', '3', '3']
    #     print("Rec")
    #     self.game.checking()
    #     mock_level_up.assert_called_once()
    #     mock_true.assert_called_once()
    #     mock_false.assert_not_called()
    #     mock_showinfo.assert_not_called()





if __name__ == '__main__':
    unittest.main()
