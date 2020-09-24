import re

from locators.locators import PronunciationLocators


class Pronunciation:
    def __init__(self, pronunciation_tag, word):
        self.tag = pronunciation_tag
        self.word = word

    def __repr__(self):
        return f"Pronunciation by {self.author}, {self.author_from}, {self.votes} votes, id:{self.id}"

    @property
    def author(self):
        locator = PronunciationLocators.AUTHOR
        author = self.tag.select_one(locator).string

        return author

    @property
    def id(self):
        locator = PronunciationLocators.DOWNLOAD_TAG
        download_tag = self.tag.select_one(locator)
        file_id = download_tag.attrs.get('data-p4')

        return file_id
    
    @property
    def forvo_pronunciation_name(self):
        locator = PronunciationLocators.DOWNLOAD_TAG
        download_tag = self.tag.select_one(locator)
        pronunciation_name = download_tag.attrs.get('data-p2')

        return pronunciation_name


    @property
    def votes(self):
        locator = PronunciationLocators.VOTES
        votes_string = self.tag.select_one(locator).text.strip()
        num_votes = int(re.match(r'-?(\d+)', votes_string).group(0))

        return num_votes

    @property
    def author_from(self):
        locator = PronunciationLocators.AUTHOR_FROM
        author_from = self.tag.select_one(locator).string

        return author_from
