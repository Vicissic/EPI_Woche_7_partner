"""Aufgabenstellung: Ein Restaurant soll eine Software bekommen, 
welche die Bestellungen verwaltet und die Rechnungen erstellt. Es 
soll für jeden Tisch einzeln betrachtet werden können. """

__author__ = "7419816, Velesco, 7742219, Kowalke Jeri"


class Product:
    def __init__(self, name: str, typ: str, category: str, price: float):
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
                price_prod = attribute_list[3]
                price_prod = float(
                    price_prod.replace(",", ".")
                )  # python nimmt keine Komma an
                self.products.append(
                    Product(
                        attribute_list[0],
                        attribute_list[1],
                        attribute_list[2],
                        price_prod,  # Kosten ist ein float
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
    def __init__(self, product: Product, quantity: int, extra_info: list):
        self.product = product
        self.quantity = quantity
        self.extra_info = extra_info

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

    def __init__(self, csv_path: str):
        super().__init__(csv_path)
        self.orders = []
        self.order_finished = False

    def check_product_in_menu(self, product_str: str):
        """Schaut ob das Produkt im Menü vorhanden ist

        :param product_str: Der Name vom Produkt
        :return: True or False
        :rtype: boolean
        """
        all_prod_list = [i.name for i in self.products]
        if product_str in all_prod_list:
            return True
        return False

    def get_prod_from_prod_str(self, product_str: str):
        """Gibt das Produkt Objekt basierend auf der string zurück

        :param product_str:
        :return: das entsprechende Produkt
        :rtype: Product Objekt
        """
        for i in self.products:
            if product_str == i.name:
                return i
        return Product("", "", "", 0)  # Sollte nicht vorkommen

    def extra_info(self, prod_str):
        """Funktion welche nach Sonderwünschen in der Konsole fragt

        :param prod_str: Der Name vom Produkt
        :type prod_str: str
        :return: Alle Sonderwünsche
        :rtype: list
        """
        # Could be a function of OrderProducts maybe?
        mod_list = []
        modification = input(
            f"Please enter a special request you would like to add to {prod_str}"
            "(Press enter if you have no additional requests): \n"
        )
        if modification != "":
            mod_list.append(modification)
            while True:
                modification = input(
                    f"Please enter another special request you would like to add to {prod_str}"
                    "(Press enter if you have no additional special requests): \n"
                )
                if modification == "":
                    break
                mod_list.append(modification)

        return mod_list

    def get_orders(self):
        """CLI welche nach Inputs fragt und Bestellungen sammelt

        :return:
        :rtype:
        """
        super().create_menu()
        super().show_menu()
        while not self.order_finished:
            prod_str = input(
                "Please input Product you would like to "
                "order [enter 'q' if you are done ordering]: \n"
                "order [enter 'r' if you want to remove some previous order]: \n"
            )
            if prod_str == "q":
                break
            if prod_str == "r":
                # TODO implement function deleting orders
                pass
            if not self.check_product_in_menu(prod_str):
                print("That product does not exist in our Menu, please try again \n")
                continue
            product = OrderTable.get_prod_from_prod_str(self, prod_str)
            mod_list = OrderTable.extra_info(self, prod_str)
            # TODO mache hier das Programm stabil, also implementiere hier wieder Abbruchbedingung
            quantity = int(
                input(
                    f"""Please input the amount of {prod_str} of you would like to order: """
                )
            )
            order = OrderProduct(product, quantity, mod_list)
            self.orders.append(order)

        return self.orders

    def calculate_sum(self):
        """Berechnet Summe der Preise aller Bestellungen

        :return: Die Summe
        :rtype: float
        """
        final_sum = 0
        for i in self.orders:
            final_sum += i.calc_price()
        return final_sum

    def get_receipt(self, receipt_path: str = "receipt.txt"):
        """Erstellt receipt.txt Datei

        :param receipt_path: Name der Datei
        """
        # kann man theoretisch schöner machen, aber die Theorie beachtet nicht
        # die Faulheit vom Verfasser
        with open(receipt_path, mode="w", encoding="utf-8") as receipt_file:
            receipt_file.write("product name" + "\t")
            receipt_file.write("quantity" + "\t")
            receipt_file.write("product price" + "\t")
            receipt_file.write("special requests" + "\t")
            receipt_file.write("price with special requests" + "\n")
            for order in self.orders:
                receipt_file.write(str(order.product.name) + "\t")
                receipt_file.write(str(order.quantity) + "\t")
                receipt_file.write(str(order.product.price) + "\t")
                receipt_file.write(str(order.extra_info) + "\t")
                receipt_file.write(str(order.calc_price()) + "\n")
            receipt_file.write(
                "\n"
                + "The total sum of your order is : "
                + str(OrderTable.calculate_sum(self))
            )


if __name__ == "__main__":
    ####WICHTIG UND NUTZVOLL:
    ####VICTOR NUTZT als Command im Terminal: "python restaurant.py < test_inputs.txt" als input
    ####für testen, damit man nicht immer wieder das selbe eingeben muss.
    #### Sonst wie gewohnt einfach python restaurant.py in die Konsole eingeben.
    ####classes.png erstellt mit Befehl "pyreverse -o png restaurant.py" (pylint dependency)
    # TODO: Implement Testfälle für alle Funktionen, UML Diagramm und Dokumentation
    b = OrderTable("food.csv")
    b.get_orders()
    b.get_receipt()
