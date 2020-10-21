
'''
Prime number iterator. Can print out all prime numbers included
form 0 to target number. It tells how many prime numbers are 
in that range, how many iterations had been done
and also prints out whether the target number is prime.
'''

from IPython.display import clear_output

'''
Imported module to clear_output from one session to the next one.
'''



'''
Functions defitions
'''


def insert_num():

    '''

    Ask for an integer number in a loop until you insert correct data.
    it then returns num once there is no except.

    '''
    while True:

        try:

            num = int(input(f"""

            Please insert one number, to print the list of the prime numbers
            included in its range and the total number of primes.

            """))

        except ValueError:

            print('Wrong input, please type an integer')
            continue

        else:

            return num


def count_primes(num):

    '''

    This function cotains 2 for loops, one for all numbers from 2 to num
    and devideseach of them for the devisors contained in the second loop.
    The count variable counts the number of primes and the iterations
    are the number of divisons made in the process.
    It also prints out whether the number inserted is a prime.

    '''

    count_numbers = 1
    print(2)
    iterations = 0
    divisors = int((num) // 1)
    for number in range(3, num + 1, 2):
        control = 0
        for divisor in range(3, divisors +1, 2):
            if number % divisor == 0:
                control += 1

            else:

                pass

            iterations += 1

        if control == 1:
            count_numbers += 1

            if number == num:
            
                print(f'{num} is a prime number!!')

            else:
            
                print(number)


    print(f"""

        The total number of primes within the first {num} numbers is {count_numbers}.
        The total number of iterations is {iterations}.

        """)


def another_num():

    '''
    This function returns True in case the user is willing to check for another number.
    Will return False instead if 'n' or 'N' will be inserted.
    It contains a while loop in case the user inserts an input that doesn't
    conform with 'y' or 'n'.
    '''
    num_on = True

    while num_on:

        next_number = input("Would you like to check another number? Please insert 'Y' or 'N'    ")

        if next_number.upper() == 'Y':

            return True

        elif next_number.upper() == 'N':

            return False

        else:
            clear_output()
            print("Sorry I don't understand what you are saying! Yes or No? ")
            





'''
START
Program starts by assigning num variable by insert() function.
At the end of the iterations NEXT_GAME variable will call a function that will ask for another number scan.
'''


while True:

    NUM = insert_num()
    count_primes(NUM)
    print('\n')
    NEXT_GAME = another_num()

    if NEXT_GAME:

        clear_output()
        print("Great! Let's begin!")
    else:

        print('\n')
        print('\t Thank you so much for using this programme! See you soon!')
        break


