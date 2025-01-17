import os

from orca.settings import timeoutTime

os.system("clear")


class Book:
    def __init__(self, title, author, genre, price, stoc, discount):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stoc = stoc
        self.discount = discount

    def aply_discount(self, discount):
        self.price -= (self.price * discount) / 100
        return self.price

book1 = Book("Dunyoning ishlari", "O'tkir Hoshimov", "Badiiy")