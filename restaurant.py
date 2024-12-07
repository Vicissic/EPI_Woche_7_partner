"""Aufgabenstellung: Ein Restaurant soll eine Software bekommen, 
welche die Bestellungen verwaltet und die Rechnungen erstellt. Es 
soll für jeden Tisch einzeln betrachtet werden können. """

__author__ = "7419816, Velesco, 7742219, Kowalke Jeri"


class Product:
    def __init__(self, name, typ, category, price):
        self.name = name
        self.typ = typ
        self.category = category
        self.price = price


class Menu:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.products = []

    def create_menu(self):
        with open(self.csv_path, mode="r") as csv_file:
            next(
                csv_file
            )  # Die erste Zeile ist fuer unsere implementierung nicht relevant
            for row in csv_file:
                attribute_list = row.strip().split(";")
                self.products.append(
                    Product(
                        attribute_list[0],
                        attribute_list[1],
                        attribute_list[2],
                        attribute_list[3],
                    )
                )

    def get_product_info(self, product_name):
        for our_products in self.products:
            if our_products.name == product_name:
                return our_products
        print("Das Produkt '{product_name}' konnte nicht gefunden werden")
        return


a = Menu("food.csv")
a.create_menu()
print([i.name for i in a.products])
