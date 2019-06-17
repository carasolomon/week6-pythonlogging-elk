# Programmer: Tacara Solomon
""" This program sorts numbers using three diffrent methods. Logging has been added to the program"""
import logging
import logstash
import sys
import time

logger = logging.getLogger('python-logstash-log')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.LogstashHandler('52.14.84.187', 5959, version=1))

# Bubble sort function
def bubbleSort(list):
    # First pass through list 
    for i in range(len(list) - 1):
        # Second pass through list
        for j in range(len(list) - 1 - i):
            # Checks if number to the left is greater than the number to the right
            if list[j] > list[j + 1]:
                # If number is greater, switch places
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
    
    
#  Selection sort function
def selectionSort(list):
    # First pass through list
    for i in range(0, len(list) - 1):
        # Minimum number  is first number
        minNum = i
        # Second pass through list
        for j in range(i + 1, len(list)):
            # If next number is less than current number, change the minimum number
            if list[j] < list[minNum]:
                minNum = j
          # If current minimum number is not equal to current number, switch places      
        if minNum != i:
             list[i], list[minNum] = list[minNum], list[i]
    return list           
             
    
# Insertion sort function
def insertionSort(list):
    # First pass through list
    for i in range(1, len(list)):
        # Gets first index
        j = i - 1
        # Checks number with next number and swaps if first number is larger
        # then moves to next number
        while list[j] > list[j + 1] and j >= 0:
            list[j], list[j +1] = list[j + 1], list[j]
            j -= 1
    return list

# Menu function
def menu():
    print("""----------Menu----------
This program accepts an entered list and sorts it with 3 different sorts.
Enter how many numbers the list will have, then enter each number to add to the list.
Once the list is entered, choose one of the following methods to sort the list.
------------------------
Enter 'bubble' to use bubble sort on list
Enter 'selection' to use selection sort on list
Enter 'insertion' to use insertion sort on list
""")

# Get list input
def getList():
    # Creates new list and gets numbers from user to append to the new list
    # then returns the list for use
    new_list = []
    lenOfList = int(input('How many numbers will the list have? '))
    for number in range(lenOfList):
        number = int(input('Enter the number to add to the list: '))
        new_list.append(number)
    return new_list
    


# Main function
def main():
    # Display menu for program
    menu()
    logger.info('Displayed menu')
    # Input list
    listToSort = getList()

    # Gets response for sort method
    response = input('Enter list method: ').split()
    method = response[0].strip().lower()
    logger.info('Recieved user input ')
     # Uses chosen method
    if method == 'bubble':
        print(bubbleSort(listToSort))
        logger.info('Method chosen is bubble')
            
    elif method == 'selection':
        print(selectionSort(listToSort))
        logger.info('Method chosen is selection')   
    elif method == 'insertion':
        print(insertionSort(listToSort))
        logger.info('Method chosen is insertion') 

        

main()
logger.info('Program started')      
