class LoginLocators:
    CSRF_TOKEN = "form.form div.actions input[name='_CSRF_TOKEN']"
    CSRF_INDEX = "form.form div.actions input[name='_CSRF_INDEX']"


class WordPageLocators:
    MANDARIN_SECTION = '#language-container-zh'
    PRONUNCIATION_LOCATOR = '#language-container-zh ul.show-all-pronunciations li'
    TITLE = 'title'


class PronunciationLocators:
    AUTHOR = 'span.ofLink' # might return more than one tag, but should be the first one
    DOWNLOAD_TAG = 'p.download span'
    VOTES = 'span.num_votes'
    AUTHOR_FROM = 'span.from'