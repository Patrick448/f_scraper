import pickle
import logging

logger = logging.getLogger('app.data')


class Cookies:
    DATA_FILE = 'data.json'

    @classmethod
    def save(cls, cookies):
        with open(cls.DATA_FILE, "wb") as file:
            pickle.dump(cookies, file)
            logger.debug(f"Saved cookies to '{cls.DATA_FILE}'")

    @classmethod
    def get(cls):
        try:
            logger.debug(f"Trying to load '{cls.DATA_FILE}'")

            with open(cls.DATA_FILE, "rb") as file:
                data = pickle.load(file)
                logger.debug(f"Pickle loaded cookies from '{cls.DATA_FILE}'")

        except FileNotFoundError as e:
            logger.error(e)
            raise CookiesNotFoundError(f"Cookies file '{cls.DATA_FILE}' was not found")

        except EOFError as e:
            logger.error(e)
            raise CookiesNotFoundError(f"Could not read {cls.DATA_FILE}")

        return data


class WordHistory:
    # TODO: plain text file would make more sense, using readline and append etc
    HISTORY_FILE = 'word_history.txt'

    @classmethod
    def save(cls, word):

        with open(cls.HISTORY_FILE, "a", encoding='utf-8') as file:
            file.write(word)

        logger.debug(f"Saved word to '{cls.HISTORY_FILE}'")

    @classmethod
    def get(cls):
        try:
            logger.debug(f"Trying to load '{cls.HISTORY_FILE}'")

            with open(cls.HISTORY_FILE, "r", encoding='utf-8') as file:
                words = [line.strip() for line in file.readlines()]

        except FileNotFoundError as e:
            logger.error(e)
            raise CannotLoadHistoryError(f"Words history file '{cls.HISTORY_FILE}' was not found")

        except EOFError as e:
            logger.error(e)
            raise CannotLoadHistoryError(f"Could not read {cls.HISTORY_FILE}")

        else:
            logger.debug(f"Loaded words from '{cls.HISTORY_FILE}'")

        return words


class CookiesNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(f"{message}")


class CannotLoadHistoryError(Exception):
    def __init__(self, message):
        super().__init__(f"{message}")