class Color:
    HEADER = '\033[95m'
    BLUE = '\u001b[34m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def colorize(color):
        print(color, end='')

    @staticmethod
    def reset():
        print('\u001b[0m', end='')
