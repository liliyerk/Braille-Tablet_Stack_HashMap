from tkinter import *
import winsound
import json
from HashMap import HashMap
from Stack import Stack

class Tablet:

    def __init__(self, cell_amount_hor, cell_amount_ver):
        self.cell_amount_hor = cell_amount_hor
        self.cell_amount_ver = cell_amount_ver

    def get_char_capacity(self):
        char_capacity = self.cell_amount_ver * self.cell_amount_hor
        return char_capacity


class Book:
    def __init__(self, text, ):
        self.text = text
        self.page_num = 0
        self.page_stack = Stack()

    def set_dimension(self, tablet):
        self.tablet = tablet

    def get_char_capacity(self):
        char_capacity = tablet.get_char_capacity()
        return char_capacity

    def translate_text(self):
        with open('pun_to_braille.json') as data_file:
            pun_to_braille_dict = json.load(data_file)
        pun_to_braille = HashMap()
        pun_to_braille.import_from_json(pun_to_braille_dict)

        with open('num_to_braille.json') as data_file:
            num_to_braille_dict = json.load(data_file)
        num_to_braille = HashMap()
        num_to_braille.import_from_json(num_to_braille_dict)

        with open('alpha_to_braille.json') as data_file:
            alpha_to_braille_dict = json.load(data_file)
        alpha_to_braille = HashMap()
        alpha_to_braille.import_from_json(alpha_to_braille_dict)

        translated_text = ""
        for char in self.text:
            if char == ' ':
                translated_text += ' '
                continue
            if alpha_to_braille.has_key(char):
                translated_text += alpha_to_braille.get(char)
            if num_to_braille.has_key(char):
                translated_text += num_to_braille.get(char)
            if pun_to_braille.has_key(char):
                translated_text += pun_to_braille.get(char)
        file = open("translated_text.json", "w")
        file.write(json.dumps(translated_text))
        file.close()

    def count_char(self):
        self.translate_text()
        with open("translated_text.json") as file:
            translated_text = json.load(file)
        translated_text = translated_text.split()
        char_count = 0
        for word in translated_text:
            char_count += len(word) + 1
        return char_count

    def get_translated_text(self):
        self.translate_text()
        with open("translated_text.json") as file:
            translated_text = json.load(file)
        return translated_text

    def separate_pages(self):
        translated_text = self.get_translated_text()
        char_capacity = self.get_char_capacity()
        char_count = len(translated_text)
        char_remain = len(translated_text)
        char_index = 0
        pages = []
        while char_remain > 0:
            if char_index + char_capacity < char_count:
                if translated_text[char_index + char_capacity] == " ":
                    pages.append(translated_text[char_index: char_index + char_capacity])
                    char_remain = char_remain - len(translated_text[char_index:char_index + char_capacity])
                    char_index = char_index + char_capacity

                else:
                    i = 1
                    while translated_text[char_index + char_capacity - i] != " ":
                        i = i + 1
                    pages.append(translated_text[char_index:char_index + char_capacity - i])
                    char_remain = char_remain - len(translated_text[char_index:char_index + char_capacity - i])
                    char_index = char_index + char_capacity - i
            else:
                pages.append(translated_text[char_index:])
                char_remain = char_remain - len(translated_text[char_index:])
        file = open("pages.json", "w")
        file.write(json.dumps(pages))
        file.close()

    def turn_on(self):
        winsound.Beep(200, 300)
        self.separate_pages()
        with open('pages.json') as data_file:
            pages_list = json.load(data_file)
        if self.page_num< len(pages_list):
            print(self.page_stack.push(pages_list[self.page_num]))


    def next_page(self):
        winsound.Beep(400, 300)
        with open('pages.json') as data_file:
            pages_list = json.load(data_file)
        if self.page_num +1 < len(pages_list):
            self.page_num += 1
            print(self.page_stack.push(pages_list[self.page_num]))



    def previous_page(self):
        winsound.Beep(600, 300)
        if self.page_num != 0:
            print(self.page_stack.pop())
            self.page_num -= 1

    def turn_off(self):
        winsound.Beep(300, 300)



class Buttons:
    def __init__(self, root):
        self.root = root

        topframe = Frame(root)
        topframe.pack()
        bottomframe = Frame(root)
        bottomframe.pack(side=BOTTOM)

        button1 = Button(bottomframe, text="Next Page", fg="red", command=self.next_page)
        button2 = Button(bottomframe, text="Previous Page", fg="green", command=self.previous_page)
        button3 = Button(topframe, text="Turn Off", fg="purple", command=self.turn_off)
        button4 = Button(topframe, text="Turn On", fg="blue", command=self.turn_on)

        button1.pack(side=LEFT)
        button2.pack(side=LEFT)
        button3.pack(side=LEFT)
        button4.pack(side=LEFT)

    def next_page(self):
        book.next_page()
        return

    def previous_page(self):
        book.previous_page()
        return

    def turn_on(self):
        book.turn_on()
        return

    def turn_off(self):
        book.turn_off()
        return

    def set_book(self, book):
        self.book = book

print("Please, input the book text")
book_text = input()
book = Book(book_text)
print("Please, input amount of characters horizontally")
h = int(input())
print("Please, input amount of characters vertically")
v = int(input())
tablet = Tablet(h, v)
book.set_dimension(tablet)
root1 = Tk()
a = Buttons(root1)
a.set_book(book)
root1.mainloop()