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


def main():
    """
    Das hier wird die main methode, die das ganze System steuert.
    :return:
    """
    tables = {}
    # ICH habe die Idee hinter dem Dictionary geändert, es soll nun
    # die Elemente {TABLE_NAME: ORDERPRODUCT_objekt} haben

    while True:
        show_tables(tables)
        table_name = input(
            "Which table do you want to order for, get the check from "
            "or add to a previous order? (Please input name of table or "
            "type 'q' to abort): "
        )
        if table_name == "q":
            print("Thanks for using our software and have a nice day")
            break
        # .keys() muss man nicht spezifizieren
        table = tables.get(table_name, r.OrderTable("food.csv"))
        while True:
            inp = input(
                "Do you want to edit orders or do you want"
                " the check? (input 'order' or 'check') \n"
                "(or get back to Table select ('q')): "
            )
            if inp == "q":
                break
            if inp == "order":
                table.order_finished = False
                table.get_orders()
                table.show_order()
                tables[table_name] = table
            elif inp == "check":
                tables.pop(table_name)
                print(f"the table {table_name} has been removed from available tables")
                print(f"The receipt can be found in the file {table_name}_receipt.txt")
                table.get_receipt(receipt_path=f"{table_name}_receipt.txt")
                break


if __name__ == "__main__":
    main()
