"""
Finding minimum value of an array
Steps
1. Initialise empty array
2. Take array as input
3. Create a for loop to iterate through every element in the array
4. Introduce variables to store current element and minimum value
5. Compare the variables, and return minimum value 
"""

'''
for i in my_array :
    if i < minVal:
        minVal = i
'''


'''
#bubble sort
def bubble():
    input_array = input("Enter an array (comma separated values): ")
    my_array = list(map(int, input_array.split(',')))
    #get number of elements in array    
    n = len(my_array)
    #two for loops cus u are looping through list twice
    for i in range(n-1)
        for j in range(0, n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
'''
#minVal = int(my_array[0])

'''
#selection sort
def sel():
    input_array = input("Enter an array (comma separated values): ")
    my_array = list(map(int, input_array.split(',')))
    n = len(my_array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
    return my_array
'''
#insertion sort
def ins():
    input_array = input("Enter an array (comma separated values): ")
    my_array = list(map(int, input_array.split(',')))
    n = len(my_array)

    if n <= 1: 
        return my_array

    for i in range(1, n):
        #allows for an index for the list
        key = my_array[i]
        #uses a variable to used as comparison for next element
        j = i - 1
        #while prev element is in bounds, and index is less than previous element
        while j >= 0 and key < my_array[j] :
           #swap current element with previous element
           my_array[j+1] = my_array[j]
           #j index will go back to the previous index position
           j -= 1
        #change new key to greater element
        my_array[j+1] = key
    return my_array   

sorted_array = ins()
print("Sorted array ", sorted_array)