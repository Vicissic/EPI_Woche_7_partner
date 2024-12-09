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
    """Erstellt das Menü als Liste von Produt Objekten

    :param csv_path: Der Path vom Menü als csv
    :param products: Liste von Produkten
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.products = []

    def create_menu(self):
        """Befüllt die Liste products mit Objekten Product durch lesen der csv Datei"""
        with open(self.csv_path, mode="r", encoding="utf-8") as csv_file:
            # Die erste Zeile ist fuer unsere implementierung nicht relevant
            next(csv_file)
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

    def get_product_info(self, product_name: str):
        """Findet das entsprechende Objekt falls es exisitiert, sonst None

        :param product_name: Der Name von was bestellt werden soll
        :return: Das entsprechende Objekt Product
        :rtype: Product Objekt
        """
        for our_products in self.products:
            if our_products.name == product_name:
                return our_products
        print(f"Das Produkt '{product_name}' konnte nicht gefunden werden")
        return None

    def show_menu(self):
        """Printet das Menü in der Konsole aus"""
        for product in self.products:
            print(
                f"{product.name},Preis:{product.price},Kategorie:{product.category},{product.typ}"
            )


class OrderProduct:
    def __init__(self, product: Product, quantity: int, extra_info: list = []):
        self.product = product
        self.quantity = quantity
        self.extra_info = extra_info  # Default leere Liste (pylint beschwert sich aber ich weiß nicht warum)

    def calc_price(self):
        """Berechnet Preis vom einzelnen bestellten Produkt

        :return: Preis
        :rtype: float
        """
        price_of_item = self.product.price
        for i in self.extra_info:
            if "extra" in i:
                price_of_item += 1
        return price_of_item * self.quantity


class OrderTable(Menu):
    """Bestellungen für einen einzelnen Tisch

    :param orders: Liste von OrderProducts
    :param order_finished: Ob die Bestellung noch ausgeführt werden soll oder nicht
    """

    def __init__(self, csv_path: str, orders=[], order_finished=False):
        super().__init__(csv_path)
        self.orders = orders
        self.order_finished = order_finished

    def check_product_in_menu(self, product_str: str):
        all_prod_list = [i.name.lower() for i in self.products]
        if product_str.lower() in all_prod_list:
            return True
        return False

    def get_prod_from_prod_str(self, product_str: str):
        for i in self.products:
            if product_str.lower() == i.name.lower():
                return i
        return False  # Sollte nicht vorkommen

    def get_orders(self):
        super().create_menu()
        super().show_menu()
        while not self.order_finished:
            prod_str = input(
                "Please input Product you would like to order [enter q if you are done ordering]: "
            )
            if prod_str == "q":
                break
            if not self.check_product_in_menu(prod_str):
                print("That product does not exist in our Menu, please try again")
                continue
            # TODO: fuege hier funktionalitaeten hinzu

        return self.orders


# a = Menu("food.csv")
# a.create_menu()
# print([i.name for i in a.products])
# a.show_menu()
b = OrderTable("food.csv")
b.get_orders()
