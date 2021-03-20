#Dussin Francesco 4Ai 03-20-2021

#task
"""
Realizzare una gestione di "lista della spesa" con questi argomenti:

nome
quantità
prezzo_singolo
Le funzionalità che devono essere presenti sono:

aggiungi prodotto
ricerca di un prodotto nella spesa
stampa costo totale della spesa
"""

# create a list and display it - only for clearity
# add an item to the list

def List_Adder(Shopping_List):
    Looper_Variable = input("number of times you would like to add a new item to the list")
    while Looper_Variable > 0:
        Food_variable = input("insert item")
        Shopping_List.append(Food_variable)
        Looper_Variable -= 1

def List_Remover(Shopping_List):
    Looper_Variable = input("choose an item to remove from the list")
    Item_Removed = Shopping_List.pop(Looper_Variable)
    print("item removed:" + Item_Removed)

def List_Printer(Shopping_List):
    for i in Shopping_List:
        print("-" + i + "-")

def list_Menu():
    print("ADDING METHOD")
    print("REMOVING METHOD")
    print("PRINTING METHOD")

Shopping_List = ["food0", "food1", "food2", "food3", "food4"]
#tupla


list_Menu()
Choose_Action = int(input("choose an action"))

while(Choose_Action != 0):
    if(Choose_Action == 1):

List_Adder(Shopping_List)
List_Remover(Shopping_List)
