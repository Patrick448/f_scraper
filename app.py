# coding=utf-8
import logging
from forvo.forvo_login import ForvoLogin
from ui.menu import Menu

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


while flogin.status is flogin.SESSION_STATUS_OFF:
    password = input('Password: ')
    flogin.login(password)

else:
    if flogin.status == flogin.SESSION_STATUS_ON:
        print("Logged in!\n")
        m.menu()

    elif flogin.status == flogin.SESSION_STATUS_ERROR:
        print("Can't connect!\n")

