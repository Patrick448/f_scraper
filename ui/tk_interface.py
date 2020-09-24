import tkinter as tk
from tkinter import ttk
from ui.player import Player
from parsers.pronunciation_parser import Pronunciation
from parsers.word_page_parser import Word
from typing import List
from forvo.forvo_login import ForvoLogin



class AppGUI():

    test_file_dir = "C:/Users/patri/OneDrive/Desktop/test"

    def __init__(self, login: ForvoLogin):
        self.login = login


    def create_window(self):
        self.root = tk.Tk()
        self.root.title("Forvo Scraper")
        self.main = ttk.Frame(self.root)
        self.main.pack(side="top", fill="x", padx=5, pady=(4, 0))

    def show_window(self):
        self.root.mainloop()

    def create_word_menu(self, word_list: List[Word]):
        for word in word_list:
            self.add_item(word)

    def add_item(self, word: Word):

        item = ttk.Frame(self.main)
        item.pack(fill="x", expand=True)

        label = ttk.Label(item, text=word.text)
        label.config(font=("Microsoft YaHei", 12))
        label.pack(side="left", fill="x", expand=True)

        if word.status == -1:
            button = ttk.Button(item, text="Add", width=5, command=lambda: self.create_add_word_window(word))
            button.pack(side="right")
        elif word.status == 0:
            button = ttk.Button(item, text="...", width=5)
            button.pack(side="right")
        elif word.status == 1:
            see_button = ttk.Button(item, text="See", width=5, command=lambda: self.create_pronunciations_window(word))
            see_button.pack(side="right")
            new_button = ttk.Button(item, text="New", width=5, command=lambda: self.login.ask_new(word))
            new_button.pack(side="right")

    def create_pronunciations_window(self, word: Word):
        pron_window = tk.Toplevel(self.root)
        pron_window.title(word.text)
        main = ttk.Frame(pron_window)
        main.pack(side="top", fill="x", padx=5, pady=(4, 0))

        for pron in word.pronunciations:
            self.add_pronunciation_item(main, pron)

    def add_pronunciation_item(self, parent, pronunciation: Pronunciation):

        item = ttk.Frame(parent)
        item.pack(fill="x", expand=True)

        label = ttk.Label(item, text=f'{pronunciation.author} ({pronunciation.votes})')
        label.pack(side="left", fill="x", expand=True)
        
    
        play_button = ttk.Button(item, text="play", width=5, command= lambda: self.play_pronunciation(pronunciation))
        play_button.pack(side="right")
        download_button = ttk.Button(item, text="download", width=10, command=lambda: self.download_pronunciation(pronunciation))
        download_button.pack(side="right")

    def create_add_word_window(self, word: Word):
        add_word_window = tk.Toplevel(self.root)
        add_word_window.title(word.text)
        main = ttk.Frame(add_word_window)
        main.pack(side="top", fill="x", padx=5, pady=(4, 0))

        word_button = ttk.Button(add_word_window, text="Add as word", command=lambda: self.login.add(word.text, False))
        word_button.pack(side="top")
        phrase_button = ttk.Button(add_word_window, text="Add as phrase", command=lambda: self.login.add(word.text, True))
        phrase_button.pack(side="top")

    def play_pronunciation(self, pronunciation: Pronunciation):
        pronunciation_file = self.login.download_file(pronunciation)
        Player.play(pronunciation_file)
    
    def download_pronunciation(self, pronunciation):
        self.login.download_file_to(self.test_file_dir, pronunciation)

    def add_word(self):
        pass



#AppGUI.create_window()
