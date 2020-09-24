import logging
from ui.player import Player
from parsers.file_parser import CSVParser
from ui.ui_colors import Color


class Menu:
    test_file_dir = "C:/Users/patri/OneDrive/Desktop/test"
    OPTIONS = """-----MENU-----

a to add
g to get
v to get words from vocab.txt
h to get words from history

Type:"""

    def __init__(self, flogin):
        self.flogin = flogin

    @staticmethod
    def list_menu(iterable, recursive, quit_cmd, final_func=None):
        menu_str = ''

        for index, element in enumerate(iterable):
            menu_str += f'{index}: {element}\n'

        print(menu_str)
        user_input = input(f"Select one or type '{quit_cmd}' to exit: ")

        while user_input != quit_cmd:
            cmd = int(user_input)
            selected_element = iterable[cmd]

            if recursive:
                recursive -= 1
                Menu.list_menu(selected_element, recursive, quit_cmd)
            else:
                final_func(selected_element)

            print(menu_str)
            user_input = input(f"Select one or type '{quit_cmd}' to exit: ")

    @staticmethod
    def menu_from_list(iterable):
        menu_str = ''
        for index, element in enumerate(iterable):
            menu_str += f'{index+1}: {element}\n'

        return menu_str

    def menu_from_words(self, words):
        words_menu = Menu.menu_from_list(words)
        print(words_menu)
        user_input = input("Number or 'q' to quit, or x to add all: ")

        while user_input != 'q':

            if user_input == 'x':
                print("Adding word list...")
                for word in words:
                    if word.status == -1:
                        print(f"Adding {word.text}")
                        self.flogin.add(word.text, True)
            
            else:
                selected_word = words[int(user_input) - 1]
                pronunciations = selected_word.pronunciations
                prons_menu = Menu.menu_from_list(pronunciations)
                print(prons_menu)

                if selected_word.status == 1:
                    user_input = input("Number or 'q' to quit: ")

                    while user_input != 'q':
                        selected_pron = pronunciations[int(user_input) - 1]
                        pronunciation_file = self.flogin.download_file(selected_pron)
                        Player.play(pronunciation_file)

                        user_input = input("Type 'd' to download to the specified directory: ")
                        if user_input == 'd':
                            self.flogin.download_file_to(self.test_file_dir, selected_pron)

                        user_input = input("Number or 'q' to quit: ")

                elif selected_word.status == -1:
                    user_input = input("Word not on Forvo. Type 'a' to add (-1 for phrase, -0 for word): ")
                    cmds = user_input.split('-')

                    if cmds[0] == 'a':
                        is_phrase = True if int(cmds[1]) else False
                        self.flogin.add(selected_word.text, is_phrase)

            print("\n" + words_menu)
            user_input = input("Number or 'q' to quit: ")

    def menu(self):

        user_input = input(self.OPTIONS)
        # test = Test(self.flogin)

        while user_input != 'q':
            command = user_input.split('-')

            if command[0] == 'v':
                csv_parser = CSVParser('vocab.txt')
                words_from_file = csv_parser.get_column(0)
                words = self.flogin.get_words(words_from_file)
                self.menu_from_words(words)

            elif command[0] == 'h':
                words = self.flogin.get_words_from_history()
                self.menu_from_words(words)

            elif command[0] == 't':
                # test.test(command[1:])
                pass

            elif command[0] == 'a':
                is_phrase = True if int(command[2]) else 0
                self.flogin.add(command[1], is_phrase)

            elif command[0] == 'g':
                word = self.flogin.get_word(command[1])
                self.menu_from_words([word])
                """for p in word.pronunciations:
                    print(p)"""

            user_input = input("Type command: ")