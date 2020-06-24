import cloudscraper
import json
import logging
import os.path

from requests import exceptions as req_exceptions
from bs4 import BeautifulSoup
from locators.locators import LoginLocators
from parsers.word_page_parser import Word, WordConst
from forvo.languages import Languages
from forvo.data import Cookies, CookiesNotFoundError, WordHistory, CannotLoadHistoryError

logger = logging.getLogger('app.forvo_login')


class ForvoLogin:

    LOGIN_URL = 'https://forvo.com/login/'
    WORD_ADD_URL = 'https://forvo.com/word-add/'
    WORD_CHECK_URL = 'https://forvo.com/word-add-ajax/'
    ACCOUNT_INFO_URL = 'https://forvo.com/account-info/'
    SESSION_STATUS_OFF = 0
    SESSION_STATUS_ON = 1
    SESSION_STATUS_ERROR = -1

    def __init__(self, username):

        logger.debug(f"Initializing {__name__}")

        self.language = Languages.MANDARIN_CHINESE
        self.username = username
        self.scraper = cloudscraper.create_scraper()
        self.status = self.SESSION_STATUS_OFF

        self.try_login()

    def try_login(self):
        try:
            logger.debug("Looking for cookies...")
            self.scraper.cookies = Cookies.get()

        except CookiesNotFoundError:
            logger.debug("Cookies not found")

        else:

            try:
                logged_only_page = self.scraper.get(self.ACCOUNT_INFO_URL).url
            except req_exceptions.ConnectionError:
                logger.error(f"Can't connect to {self.ACCOUNT_INFO_URL}")
                self.status = self.SESSION_STATUS_ERROR
            else:
                if logged_only_page == self.LOGIN_URL:
                    logger.debug("Cookies didn't work")

                else:
                    logger.debug("Cookies worked. Logged in.")
                    self.status = self.SESSION_STATUS_ON

    def login(self, password):
        logger.debug(f"Starting log in as {self.username}")
        page = self.scraper.get(self.LOGIN_URL)

        token_parser = TokenParser(page.text)
        csrf_token = token_parser.csrf_token
        csrf_index = token_parser.csrf_index

        login_data = {"login": self.username,
                      "password": password,
                      "remember": "on",
                      "_CSRF_INDEX": csrf_index,
                      "_CSRF_TOKEN": csrf_token}

        request = self.scraper.post(self.LOGIN_URL, data=login_data)

        if request.url == self.LOGIN_URL:
            logger.debug("Failed to log in")
        else:
            logger.debug("Logged in successfully")
            Cookies.save(self.scraper.cookies)
            self.status = self.SESSION_STATUS_ON

    @property
    def session(self):
        return self.scraper

    def close(self):
        self.scraper.close()

    def get_word(self, text):
        url = f"https://forvo.com/word/{text}/#{self.language['code']}"
        page = self.scraper.get(url).content

        return Word(page, text)

    def get_words(self, string_list):
        word_list = []
        for text in string_list:
            url = f"https://forvo.com/word/{text}/#{self.language['code']}"
            page = self.scraper.get(url).content
            word_list.append(Word(page, text))

        return word_list

    def add(self, text, is_phrase):

        data = {
            'word': text,
            'id_lang': self.language['idLang'],
            'modify': 0,
            is_phrase: 1 if is_phrase else 0
        }
        page = self.scraper.get(self.WORD_ADD_URL)

        if not self._exists(text):
            self.scraper.post(self.WORD_ADD_URL, data=data)
            self.save_to_history(text)

            print("Word added!")
            logger.debug("Word added")

    def get_words_from_history(self):
        words_text = WordHistory.get()
        return self.get_words(words_text)

    def save_to_history(self, word):
        WordHistory.save(word)

    def remove_from_history(self, word):
        pass

    def download_file(self, pronunciation):
        file_path = f'download/{pronunciation.id}.mp3'

        if not os.path.exists(file_path):
            with open(file_path, 'w+b') as file:
                url = f"https://forvo.com/download/mp3/{pronunciation.word}/{self.language['code']}/{pronunciation.id}"
                download = self.scraper.get(url).content
                file.write(download)

        return file_path

    def download_file_to(self, path, pronunciation):

        file_path = f'download/{pronunciation.id}.mp3'
        destination_path = f"{path}/pronunciation_{self.language['code']}_{pronunciation.word}.mp3"

        if os.path.exists(file_path):
            with open(file_path, 'r+b') as file_from:
                with open(destination_path, 'w+b') as file_to:
                    file_to.write(file_from.read())

        else:
            with open(destination_path, 'w+b') as file:
                url = f"https://forvo.com/download/mp3/{pronunciation.word}/{self.language['code']}/{pronunciation.id}"
                download = self.scraper.get(url).content
                file.write(download)

        return destination_path

    def _exists(self, text):
        data = {
            'f': 'checkExists',
            'text': text
        }
        request = self.scraper.post(self.WORD_CHECK_URL, data=data)
        response_dict = json.loads(request.text)

        try:
            logger.debug("Checking if 'langs' fied exists in the response for the 'checkExists' request")
            langs = response_dict['data']['langs']

        except KeyError:
            logger.error(f"'langs' field does not exists, therefore `{text}` has not been added for any language yet")
            matches_current_language = 0

        else:
            matches_current_language = len([lang
                                            for lang in langs
                                            if lang['idLang'] == self.language['idLang']])

            logger.debug(f"'word' in '{self.language['name']}' exists: {True if matches_current_language else False}")

        return True if matches_current_language else False


class TokenParser:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def csrf_token(self):
        csrf_token_tag = self.soup.select_one(LoginLocators.CSRF_TOKEN)
        csrf_token = csrf_token_tag.attrs.get('value')

        return csrf_token

    @property
    def csrf_index(self):
        csrf_index_tag = self.soup.select_one(LoginLocators.CSRF_INDEX)
        csrf_index = csrf_index_tag.attrs.get('value')

        return csrf_index
