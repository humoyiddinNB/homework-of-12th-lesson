import os

os.system("clear")

class Book:
    def __init__(self, title, author, genre, price, stoc, discount = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stoc = stoc
        self.discount = discount

    def apply_discount(self):
        if self.discount:
            yangi_narx = self.price - (self.price * self.discount) / 100
            return f"{self.discount}% li chegirma amalga oshirildi :)\n{self.price} so'm    ✕\n{yangi_narx} so'm    ✔"
        return f"Afsuski chegirma mavjud emas"


class Customer:
    def __init__(self, name, e_mail):
        self.name = name
        self.e_email = e_mail
        self.my_orders = []

    def add_orders(self, qaysi_baza, book_title, how_many):
        for book in qaysi_baza.books:
            if book_title == book.title:
                if how_many <= book.stoc:
                    self.my_orders.append({"title" : f"{book_title}", "number" : f"{how_many}"})
                    return f"Kitob Savatchaga qo'shildi"
                return f"{book_title} kitobi {how_many} tadan kam"
        return f'Afsuski {book_title} kitobi topilmadi'


class StoreManager:
    def __init__(self):
        self.books = []
        self.customers = []

    def add_books(self, book):
        return self.books.append(book)

    def remove_books(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"Muvaffaqiyatli ochirildi"
        return f"Afsuski {title} kitobi topilmadi"

    def search_books(self, title):
        for book in self.books:
            if title == book.title:
                return f"{title} kitobi muvaffaqiyatli topildi. Sotuvda jami: {book.stoc}"
        return f"Afsuski bu kitobdan mavjud emas"

    def __str__(self):
        result = f"Barcha kitoblar:\n"
        for book in self.books:
            result += f"Nomi: {book.title}, Avtor: {book.author}, Janri: {book.genre}, Narxi: {book.price} UZS, sotuvda mavjud: {book.stoc} ta\n"
        return result


my_manager = StoreManager()


book1 = Book("Dunyoning ishlari", "O'tkir Hoshimov", "Badiy", 100_000, 50, 20)
book2 = Book("Ikki eshik orasi", "O'tkir Hoshimov", "Badiy", 150_000, 20, 10)
book3 = Book("Chol va Dengiz", "Ernest Xeminguey", "Badiy", 120_000, 30, 15)
book4 = Book("Alkimyogar", "Paulo Koelo", "Badiy", 170_000, 25, 12)
book5 = Book("Inson psixologiyasi", "Abraham Maslow", "Psixologiya", 200_000, 40, 25)
book6 = Book("Oq kema", "Chingiz Aytmatov", "Badiy", 130_000, 35, 18)
book7 = Book("Shaytanat", "Tohir Malik", "Detektiv", 100_000, 50, 30)
book8 = Book("Yo'ldagi belgilar", "O'tkir Hoshimov", "Badiy", 110_000, 60, 22)
book9 = Book("1984", "Jorj Oruel", "Fantastika", 180_000, 20, 8)
book10 = Book("Tafsiri Hilol", "Muhammadsodiq Muhammadyusuf", "Diniy", 50_000, 100, 90)


alll_books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]

for book in alll_books:
    my_manager.add_books(book)


customer1 = Customer("Humoyiddin Ne'matillayev", "humoyiddin71@gmail.com")
customer2 = Customer("Azizbek Xolmirzayev", "azizbek97@gmail.com")
customer3 = Customer("Dilshod Tursunov", "dilshod_t@gmail.com")
customer4 = Customer("Kamola Karimova", "kamola.karimova@outlook.com")
customer5 = Customer("Javohir Abdullayev", "javohir.abdullayev@mail.ru")
customer6 = Customer("Shaxnoza Umarova", "shaxnozaumarova@gmail.com")
customer7 = Customer("Bekzod Rustamov", "bekzod.rustamov@yahoo.com")
customer8 = Customer("Otabek Matniyazov", "otabek.matniyazov@gmail.com")
customer9 = Customer("Nigora Saidova", "nigora.saidova@hotmail.com")
customer10 = Customer("Islomjon Yuldashev", "islomjon.yuldashev@protonmail.com")


all_customs = [customer1, customer2, customer3, customer4, customer5, customer6, customer7, customer8, customer9, customer10]

for custom in all_customs:
    my_manager.customers.append(custom)



print(customer3.add_orders(my_manager, "Alkimyogar", 1))

print(customer1.add_orders(my_manager, "Chumolik sirlari", 2))

print(my_manager)

print(my_manager.search_books("Ikki eshik orasi"))

print(my_manager.remove_books("Ikki eshik orasi"))


print(book2.apply_discount())
