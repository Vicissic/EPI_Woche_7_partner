"""
Main aufruf
"""

__author__ = "7419816, Velesco, 7742219, Kowalke Jeri"

import restaurant as r


def show_tables(tables):
    """
    Soll die aktuellen Tische auflisten.

    :param tables: Dictionary von den Tischen
    :return: Ein Verzeichnis, wie viele Tische es gibt und wie
    sie heißen.
    """
    print("These are the current existing tables:")
    for i, table_name in enumerate(tables.keys()):
        print(f"({i}) {table_name} \n")
    return


def main():
    """
    Das hier wird die main methode, die das ganze System steuert.
    :return:
    """
    tables = {}

    while True:
        show_tables(tables)
        table_name = input("Which table do you want to edit or create?: ")
        if table_name in tables.keys():  # Fall, bereits existierender Tisch
            table = r.OrderTable("food.csv")
            table.add_previous_orders(tables[table_name])  # hinzufügen
            # von den alten Bestellungen zu der Liste orders

            new_order = table.get_orders()
            table.show_order(new_order)
            tables[table_name].append(new_order)

        else:  # Fall, wo der Tisch neu ist
            while True:
                inp = input("Do you want to edit the orders or do you want"
                            " the check? (order or check) \n"
                            "(or get back to Table select (q): ")
                if inp == "order":
                    table = r.OrderTable("food.csv")
                    order = table.get_orders()
                    table.show_order(order)
                    tables[table_name] = order
                    #  [order[i].product.name for i in range(len(order))] Nur ein Test
                elif inp == "check":
                    #new_order.get_receipt()  muss auch noch richtig gemacht werden
                    # TODO Tisch soll gelöscht werden und ich glaube, dass es insgesamt nur eine Rechnung gibt
                    # TODO also müssen es noch iwie einrichten, dass es pro Tisch eine rechnung gibt

                elif inp == "q":
                    break


main()
