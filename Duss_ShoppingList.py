# file Duss_ShoppingList.py
# Author Dussin Francesco(you@domain.com)
# brief
# version 0.1
# date 2021-03-20++
# copyright Copyright(c) 2021

#task
#Realizzare una gestione di "lista della spesa" con questi argomenti:
#nome
#quantità
#prezzo_singolo

#Le funzionalità che devono essere presenti sono:
#aggiungi prodotto
#ricerca di un prodotto nella spesa
#stampa costo totale della spesa

# create a list and display it - only for clearity
# add an item to the list

# TO-DO && STATUS
# MENU || V
# REMOVE || V
# ADD || XV err
# PRINT || V
# COST || X
# SEARCH || X

import webbrowser
import urllib

#Shopping_List = [["a-food01", 1, 11], ["b-food012", 2, 22], ["c-food0123", 3, 33], ["d-food01234", 4, 44], ["e-food012345", 5, 55]]
#{'name': 'foods', 'quantity': 'n_items', 'cost': 'price'}
Shopping_Dictionary = {}

def List_Printer(Shopping_Dictionary):
    if(len(Shopping_Dictionary) == 0):
        print("total cost of the elements in the dictionary is 0")
    else:
        for i in Shopping_Dictionary:
            print(
                "quantity: ", Shopping_Dictionary[i][0], "cost: ", Shopping_Dictionary[i][1])

def List_Adder(Shopping_Dictionary):
    food_name = input("name of the product : ")
    food_quantity = int(input("quantity of the product : "))
    food_cost = int(input("cost of the product : "))
    if(food_name in Shopping_Dictionary.keys()):
        Shopping_Dictionary[food_name] = (food_quantity + 1, food_cost * 2)
    else:
        Shopping_Dictionary[food_name] = [food_quantity, food_cost]

def List_Remover(Shopping_Dictionary):
    remover_variable = input("choose an item to remove from the list\n")
    del(Shopping_Dictionary[remover_variable])
    #Shopping_Dictionary.pop(Shopping_Dictionary[Remover_Variable])

def List_Searcher(Shopping_Dictionary):
    searcher_variable = input("enter a name - searching method\n")
    for i in Shopping_Dictionary:
        if(i in Shopping_Dictionary.keys()):
            print("item found : ", i, " - ", Shopping_Dictionary.keys())

def List_T_Cost_Printer(Shopping_Dictionary):
    if(len(Shopping_Dictionary) == 0 ):
        print("total cost of the elements in the dictionary is 0")
    else:
        for i in Shopping_Dictionary:
            print("quantity: ", Shopping_Dictionary[i][0],"cost: ", Shopping_Dictionary[i][1])
            dfgfdsdgfzd = Shopping_Dictionary[i][1]
            print("kpop", dfgfdsdgfzd)

def list_Menu():
    print("1-ADDING METHOD")
    print("2-REMOVING METHOD")
    print("3-PRINTING METHOD")
    print("4-SEARCHING METHOD")
    print("5-PRICE METHOD\n")

list_Menu()
Choose_Action = int(input("1-choose an action\n"))
if(Choose_Action < 0 or Choose_Action > 5):
    exit()

#List_Adder(Shopping_Dictionary)
while(Choose_Action != 0):
    if(Choose_Action == 1):
        List_Adder(Shopping_Dictionary)
        Choose_Action = int(input("2-choose an action\n"))

    elif(Choose_Action == 2):
        List_Remover(Shopping_Dictionary)
        Choose_Action = int(input("3-choose an action\n"))

    elif(Choose_Action == 3):
        List_Printer(Shopping_Dictionary)
        Choose_Action = int(input("4-choose an action\n"))

    elif(Choose_Action == 4):
        List_Searcher(Shopping_Dictionary)
        Choose_Action = int(input("5-choose an action\n"))

    elif(Choose_Action == 5):
        List_T_Cost_Printer(Shopping_Dictionary)
        Choose_Action = int(input("0-choose an action\n"))

    elif(Choose_Action > 5 or Choose_Action < 0 or Choose_Action == 0):
        print("program killed")
