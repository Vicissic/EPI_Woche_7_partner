"""
Hier ist die main Funktion definiert, die das ganze System startet und stoppt.
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
    :return: None
    """
    tables = {}  # Dictionary, wo alle Tische mit ihren Bestellungen
    # aufgelistet werden.

    while True:
        show_tables(tables)
        table_name = input(
            "Which table do you want to order for, get the check from "
            "or add to a previous order? (Please input name of table or "
            "type 'q' to abort): "
        )
        if table_name == "q":
            print("\nThanks for using our software and have a nice day")
            break
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
                if table_name in tables:
                    print(
                        f"the table {table_name} has been removed "
                        f"from available tables"
                    )
                    print(
                        f"The receipt can be found in the "
                        f"file {table_name}_receipt.txt"
                    )
                    table.get_receipt(receipt_path=f"{table_name}_receipt.txt")
                    tables.pop(table_name)
                    break


if __name__ == "__main__":
    # Test für show_table (nicht so sinnvoll meiner Meinung nach)
    # tables = {"tabl1": ["Beer", "Burger"], "tabl3": ["Cola"]}
    # show_tables(tables)

    # Test in der Konsole (test_inputs.txt, main.py, restaurant.py
    # muss im selben Ordner liegen)
    # 'python main.py < text_inputs.txt' in einer Unix-Konsole ausführen

    main()
