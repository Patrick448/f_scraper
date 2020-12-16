# coding=utf-8
import logging
from forvo.forvo_login import ForvoLogin
from parsers.file_parser import CSVParser, ExcelParser
from ui.menu import Menu
from ui.tk_interface import AppGUI

# TODO: save recently added words to a file
# TODO: every time I log in, check if those words have been pronounced


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('app')

username = 'patrickcarvalho448@gmail.com'
password = ''

print(f'\nLogging in as {username}...')

flogin = ForvoLogin(username)
session = flogin.session
m = Menu(flogin)

#test
#ep = ExcelParser('C:/Users/patri/OneDrive/Desktop/Patrick/Vocab/VocabList-Mandarin.xlsx')
#print(ep.get_file_as_dict_list)
#dates = [item['date'] for item in ep.get_file_as_dict_list]

while flogin.status is flogin.SESSION_STATUS_OFF:
    password = input('Password: ')
    flogin.login(password)

else:
    if flogin.status == flogin.SESSION_STATUS_ON:
        print("Logged in!\n")

        csv_parser = CSVParser('vocab.txt')

        phrases_from_file = csv_parser.get_column(0)
        words_from_file = csv_parser.get_column(2)
        phrases_from_file.extend(words_from_file)
    
        words = flogin.get_words(phrases_from_file)

        app_gui = AppGUI(flogin)

        #test
        #app_gui.create_root()
        #app_gui.create_options_menu(["op1", "op2", "op3"])
        #app_gui.show_window()

        
        app_gui.create_window()
        app_gui.create_word_menu(words)
        app_gui.show_window()

        m.menu()



    elif flogin.status == flogin.SESSION_STATUS_ERROR:
        print("Can't connect!\n")

