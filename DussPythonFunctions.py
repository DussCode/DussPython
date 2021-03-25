# Author: Duss 4Ai 03-21-2021
# Scrivi un programma che presenti un menu per scegliere una delle seguenti opzioni:
#
# calcolo del fattoriale di un numero intero positivo (< 12) inserito da tastiera;
# visualizzazione dei numeri primi fino a n con n intero positivo inserito da tastiera;
# Potenza n-esima (n > 0 intero) di un numero reale a (!=0);
# Fine
#
#
# TO-DO && STATUS
# MENU || x
# FACTORIAL || x
# PRIMES || x
# POW || x
# SURPRISE || X y not

#######################################################################
import math
#######################################################################
def Fun_Menu():

    print("1-pow_input_SELF (evaluates for it's value)")
    print("2-Fun_Primes")
    print("3-Fun_Factorial")
    print("4-SURPRISE (:")
    print("5-pow_input_INPUT && pow_input_INPUT_TIMES (evaluates for a specified value)")
#######################################################################
def Fun_Pow_SELF(pow_input_SELF):

    counter_SELF = 0
    X_Self = pow(pow_input_SELF, pow_input_SELF)
    counter_SELF += 1
    print(X_Self)
    print(type(X_Self))
    if(counter_SELF == 1):
        exit()
#######################################################################
def Fun_Pow_INPUT(pow_input_INPUT, pow_input_INPUT_TIMES):

    counter_INPUT = 0
    X_Input = pow(pow_input_INPUT, pow_input_INPUT_TIMES)
    print(X_Input)
    print(type(X_Input))
    if(counter_INPUT == 1):
        exit()
#######################################################################
def Fun_Primes(starting_point, primes_input):

   for i in range(starting_point, primes_input):

      for p in range(2, i):

         if i % p == 0:

             break
         else:

            print(i, "<- starting + ending ->", primes_input)
#######################################################################
def Fun_Factorial(factorial_input):

    factorial_result = 1
    counter_Factorial = 0

    if(factorial_input < 0):
        print("Impossible")
    elif(factorial_input == 0):
        print("1")
    else:
        for i in range(1, factorial_input + 1):
            factorial_result = factorial_result * i
            counter_Factorial += 1
    print("result: ", factorial_result)
    if(counter_Factorial == 1):
        exit()
#######################################################################
def Fun_Surprise():

    print("SURPRISE ):")
#######################################################################

Fun_Menu()

Choose_Action = int(input("-choose an action\n"))

if(Choose_Action < 0 or Choose_Action > 5):
    exit()

#######################################################################

while(True):
    if(Choose_Action == 1):
        pow_input_SELF = int(input("---insert a number\n"))

        if(pow_input_SELF < 0 or pow_input_SELF > 11):
            print("---INVALID NUMBER - insert another number")
            pow_input_SELF = int(input("---insert a new number\n"))

        Fun_Pow_SELF(pow_input_SELF)

    if(Choose_Action == 2):
        primes_input = int(input("-----insert a number\n"))
        starting_point = 2

        if(primes_input < 0 or primes_input > 11):
            print("-----INVALID NUMBER - insert another number")
            primes_input = int(input("-----insert a new number\n"))

        Fun_Primes(starting_point, primes_input)

    if(Choose_Action == 3):
        factorial_input = int(input("--insert a number\n"))

        if(factorial_input < 0 or factorial_input > 11):
            print("--INVALID NUMBER - insert another number")
            factorial_input = int(input("--insert a new number\n"))

        Fun_Factorial(factorial_input)

    if(Choose_Action == 4): #useless
        Fun_Surprise()

    if(Choose_Action == 5):
        pow_input_INPUT = int(input("----insert a number\n"))
        pow_input_INPUT_TIMES = int(input("----insert a number\n"))

        if(pow_input_INPUT < 0 or pow_input_INPUT > 11):
            print("----INVALID NUMBER - insert another number")
            pow_input_INPUT = int(input("----insert a new number\n"))

        if(pow_input_INPUT_TIMES < 0):
            print("----INVALID NUMBER - insert another number")
            pow_input_INPUT_TIMES = int(input("----insert a new number\n"))

            Fun_Pow_INPUT(pow_input_INPUT, pow_input_INPUT_TIMES)

    if(Choose_Action > 5):
        exit()

    if(Choose_Action == 0):
        break

print("point number 4: FINE (:")
#######################################################################
