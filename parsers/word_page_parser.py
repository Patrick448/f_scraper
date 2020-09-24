import re
import logging
from bs4 import BeautifulSoup
from locators.locators import WordPageLocators
from parsers.pronunciation_parser import Pronunciation
from forvo.constants import WordConst

logger = logging.getLogger('app.word')


class Word:

    def __init__(self, page, word):
        self.soup = BeautifulSoup(page, 'html.parser')
        self.text = word

    def __repr__(self):
        return f'<word: {self.text}, {self.status}>'

    @property
    def status(self):
        title_locator = WordPageLocators.TITLE
        title_text = self.soup.select_one(title_locator).text
        #pending_pattern = r'^How to pronounce.+'
        #not_added_pattern = r'Forvo - Page not found'
        

        #match_pending = re.match(pending_pattern, title_text)
        #match_not_added = re.match(not_added_pattern, title_text)

        language_container = self.soup.select_one("#language-container-zh")
        pronunciation_pending_container = self.soup.select_one(".waiting_pronunciations #zh")

        if pronunciation_pending_container:
            return WordConst.WORD_STATUS_PENDING
        elif not language_container:
            return WordConst.WORD_STATUS_NOT_ADDED
        else:
            return WordConst.WORD_STATUS_OK

    @property
    def id(self):
        locator = WordPageLocators.WORD_ID_LOCATOR
        id_div = self.soup.select_one(locator)
        id = id_div.attrs.get('data')

        return id

    @property
    def pronunciations(self):

        locator = WordPageLocators.PRONUNCIATION_LOCATOR
        pronunciation_tags = [e for e in self.soup.select(locator)
                              if e.attrs.get('class') is None]
        return [Pronunciation(e, self.text) for e in pronunciation_tags]
