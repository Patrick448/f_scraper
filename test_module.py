import pygame
from pygame import mixer

from ui.menu import Menu
from parsers.file_parser import CSVParser


class Test:

    test_list = ['妈妈', '狗', '和设计师江苏阜宁', '不用哭', '我的妈妈', '看书', '爱情', '生活']
    test_result = []

    def __init__(self, forvo_login):
        self.flogin = forvo_login

    def test(self, args):
        if args[0] == 't':
            word = self.flogin.get_word('妈妈')
            for p in word.pronunciations:
                print(p)
                self.flogin.download_file(p)

        elif args[0] == 'l':
            words = []
            for word in self.test_list:
                words.append(self.flogin.get_word(word))

            self.list_menu_test(words)

        elif args[0] == 'pl':
            words = []
            for word in self.test_list:
                words.append(self.flogin.get_word(word))

            self.get_words_and_play_test(words)

        elif args[0] == 'tl':
            words = []
            for word in self.test_list:
                words.append(self.flogin.get_word(word))

            self.list_menu_test(words)

        elif args[0] == 'al':
            csv_parser = CSVParser('vocab.txt')
            words = []
            words_from_file = csv_parser.get_column(0)
            for word in words_from_file:
                words.append(self.flogin.get_word(word))

            self.list_menu_test(words)

    def get_words_test(self, words):
        for index, word in enumerate(words):
            print(f'{index+1}: {word}')

        user_input = input("Number or 'q' to quit: ")
        while user_input != 'q':
            for p in words[int(user_input)-1].pronunciations:
                print(p)

            user_input = input("Number or 'q' to quit: ")

    def get_words_and_play_test(self, words):
        for index, word in enumerate(words):

            print(f'{index+1}: {word}')

        user_input = input("Number or 'q' to quit: ")
        while user_input != 'q':
            pronunciation = words[int(user_input)-1].pronunciations[0]

            self.play_pron(pronunciation)

            user_input = input("Number or 'q' to quit: ")

    def play_pron(self, pron):
        mixer.init()
        mixer.music.load(self.flogin.download_file(pron))
        mixer.music.play()

        while mixer.music.get_busy():
            pygame.time.Clock().tick()

    def list_menu_test(self, words):

        words_menu = Menu.menu_from_list(words)
        print(words_menu)
        user_input = input("Number or 'q' to quit: ")

        while user_input != 'q':

            pronunciations = words[int(user_input) - 1].pronunciations

            prons_menu = Menu.menu_from_list(pronunciations)
            print(prons_menu)
            user_input = input("Number or 'q' to quit: ")

            while user_input != 'q':
                self.play_pron(pronunciations[int(user_input)-1])
                user_input = input("Number or 'q' to quit: ")

            print("\n"+words_menu)
            user_input = input("Number or 'q' to quit: ")
