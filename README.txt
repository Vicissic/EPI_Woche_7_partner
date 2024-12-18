RESTAURANT PROJEKT

## Inhalt dieser README
1. Was ist die Aufgabe des Projekts und wie benutzt man das Programm?
2. Was muss installiert sein, damit man das Programm nutzen kann?
3. Wer hat bei der Erstellung mitgewirkt?
***
1. 
Dieses Programm soll eine Systemsoftware für ein Restaurant sein. Primär ist es dafür da, Bestellungen pro Tisch aufzunehmen, zu speichern und anschließend die Rechnung dieser Bestellung auszugeben. Eine genauere Beschreibung und Analyse der Aufgabe kann man der 
PDF-Datei entnehmen.

***
Vorrausetzungen, um das Programm zu starten sind mindestens eine Version von Python 3.x installiert zu haben.
Im Ordner der Dateien muss sich außerdem noch eine csv-Datei "food.csv" mit den Daten des Menus befinden. 
 
Anleitung:
Vorab, das komplette User-Interface befindet sich in der Konsole.

Die Grundidee des Programmes ist:
1) Tisch auswählen/ erstellen
2.1) Neue Bestellungen aufnehmen oder 2.2) Rechnung erstellen und abschließen.
3.1) Betellungen aus dem Menu auswählen  bzw. bearbeiten (löschen)

Jeder dieser Punkte bezieht sich auf den Vorigen. Also in Punkt 2.x wird bestellt oder die Rechnung des Tisches geliefert, der in Punkt 1 ausgewählt wurde.

Zu jedem Zeitpunkt gibt es die Möglichkeit ein "Level" runter zu gehen. Also z.B. von 3.1)Bestellungen aus dem Menu auswählen, zu 2.x. Das passiert durch Eingabe von "q" in der Konsole.

Bei 1) wird der User aufgefordert einen Tisch zu erstellen oder zu bearbeiten. Die bereits existierenden Tische werden ihm dort angezeigt. Um einen zu bearbeiten, muss man den genauen Namen (Achtung Groß-/Kleinbuchstaben) in die Konsole schreiben, dann "befindet" man sich bei diesem Tisch. Wird etwas Anderes eingegeben, wird ein neuer Tisch mit dem eingegebenen Namen erstellt. 
Eingabe von "q" führt auf diesem Level zum Abbruch des gesamten Programmes.

Bei 2) entscheidet man, durch Eingabe von "order", ob man neue Bestellungen zu dem ausgewähltem Tisch machen will. Oder durch Eingabe von "check", erhält man die Rechnung des gewählten Tisches in einer "Name_Tisch"receipt.txt Datei. Achtung nachdem die Rechnung des Tisches erstellt wurde, ist der Tisch aus dem Speicher gelöscht. Also man hat keinen Zugriff mehr und ein neuer Tisch mit diesem Namen kann erstellt werden.
Man wird zurück zu Ebene 1) gebracht.
Eingabe von "q" führt zurück zur Tischauswahl (Level 1).

Durch Eingabe von "order" im vorherigen Schritt kommt man auf die Bestellebene 3). Hier kann man neue Objekte bestellen oder die bisher bestellten Objekte löschen.
Dem User wird hier das Menu angezeigt. Man bestellt ein Objekt, indem man genau den Namen des Produktes in die Konsole schreibt. Also z.B. "COLA (0.4)". Daraufhin kann man extra Wünsche zu dem Produkt fordern. 
Achtung Wünsche mit Zusatz müssen mit einem extra versehen werden.
Die Eingabe sieht z.B. also so "extra Käse" aus.
Wünsche ohne Zusatz werden ohne extra eingegeben: ("ohne Gurken")
Nur die Wünsche mit "extra" werden in der Rechnung berücksichtigt und entsprechend bepreist!
Zum Schluss wählt man die Anzahl dieses Produktes, mit! genau diesem Sonderwunsch, aus.
Darauf gelangt man wieder in die Ebene, wo man ein neues Produkt bestellen kann.
Gibt man statt eines Produktes, ein "r" in die Konsole, kommt man auf den Bearbeitungsmodus der Bestellungen. Dort werden alle bisher bestellten Produkte indiziert und man kann durch Auswahl eines Indexes diese Bestellung löschen. Durch "q" gelangt man wieder zur Bestellebene.
Eingabe von "q" führt zurück zur Entscheidung, ob man die Rechnung oder neue Bestellungen aufgeben will.

Es gibt keine bekannten Bugs. 
Erwähnen könnte man noch, dass es nicht möglich sein wird Tische q zu benennen. 
Oder, dass wenn man einen Tisch mit Namen x abschließt(Rechnung erstellt) und dann einen weiteren Tisch mit dem selben Namen erstellt und wieder abschließt, die vorherige Datei ersetzt wird. Also die Rechnung des vorherigen Tisches geht verloren.
***

Die Autoren sind Victor Velesco und Tonio Kowalke Jeri.