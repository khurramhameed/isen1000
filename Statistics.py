# This is a Python program for performing simple statistical operations on a 
# list of numbers.
# 
# This class is part of ISE (ISAD1000/5004) Modularity worksheet.
# 
# Make sure you're up-to-date with your programming unit!
#
# (Note: yes, Python has built-in shortcuts for a lot of the code here, 
# like sum(), min() and max(), but just say for the sake of the exercise that 
# we want to implement these operations ourselves.)

import math
# This another comment
def mySum(sumLength, sumList):
    """Calculates the sum of the numbers in the sumList variable."""
    result = 0.0
    for i in range(sumLength):
        result += sumList[i]
    return result
def sum(a, b):
    print('Sum = ',a+b)
    print('This was a test for B2')
    
def mean(sumLength, sumList):
    """Calculates the mean (average) of the numbers in the sumList variable."""
    theSum = mySum(sumLength, sumList)
    return theSum / sumLength


def variance(sumList):    
    """
    Calculates the variance of a list of numbers. Stores the result in the 
    varianceResult variable.
    """
    sumSquares = 0.0
    sumLength = len(sumList)
    average = mean(sumLength, sumList)
    
    for i in range(sumLength):
        difference = sumList[i] - average
        sumSquares += difference * difference
        
    varianceResult = sumSquares / (sumLength- 1)
    return varianceResult
    

def stddev(dataList):    
    """Calculates the standard deviation of a list of numbers."""
    varianceResult = variance(dataList)        
    return math.sqrt(varianceResult)


def calcMax(dataList):
    """
    Determines the maximum value of a list
    """
    result = dataList[0]
        
    # Find the highest value in the list.
    for i in range(len(dataList)):
        element = dataList[i]
        if result < element:
        # If the next element is higher than the maximum so far, 
        # update the maximum.
            result = element
    return result

def calcMin(dataList):
    '''
        Find the lowest value in the list.
    '''
    result = dataList[0]
    for i in range(len(dataList)):
        element = dataList[i]
        if result > element:
        # If the next element is lower than the minimum so far, 
        # update the minimum.
            result = element

    return result
    
    
    
def product(dataList):
    """
    Calculates the product of a list of numbers lis
    """

    product = 1.0
    for i in range(len(dataList)):
        product *= dataList[i]
    return product

def geomean(dataList):
    prod = product(dataList)
    result = pow(prod, 1.0 / len(dataList))
    return result

def log(dataList):
    prod = product(dataList)
    result = math.log(prod)
    return result


        
if __name__ == "__main__":
    # Input list length
    listLength = int(input("Enter length of list: "))
    
    # Create new list and input each element
    dataList = []
    for i in range(listLength):
        nextNumber = float(input("Enter real number: "))
        dataList.append(nextNumber)
    
    operation = input("Select a calculation to perform: ")
    sumLength = listLength
    sumList = dataList
    
    # Determine which operation was chosen, and perform it.
    if operation == "min":
        result = calcMin(dataList)
        
    elif operation == "max":
        result = calcMax(dataList)
        
    elif operation == "sum":
        result = mySum(sumLength, sumList)
        
    elif operation == "mean":
        result = mean(sumLength, sumList)
        
    elif operation == "variance":
        result = variance(dataList)
        
    elif operation == "stddev":
        result = stddev(dataList)
        
    elif operation == "product":
        result = product(dataList)        
        
    elif operation == "geommean":
        result = geomean(dataList)
    
    elif operation == 'log':
        result = log(dataList)
        
    else:
        print("Unrecognised operation \"" + operation + "\".")
        result = 0.0
        
    print("Result = " + str(result))
