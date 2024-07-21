#Always a good idea to list what the code must contain or do before programming it
"""
Fib numbers:

Two variables to hold the previous two Fibonacci numbers
A for loop that runs 18 times
Create new Fibonacci numbers by adding the two previous ones
Print the new Fibonacci number
Update the variables that hold the previous two fibonacci numbers

"""

"""
#Fibonacci Numbers with For Loops
#initialise two params 
prev2 = 0
prev1 = 1

#print out the numbers for every iteration
print(prev2)
print(prev1)
for fibo in range(19):
    #new number is sum of prev numbers
    newFibo = prev2 + prev1
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo
"""

"""
#Fibonacci Numbers with Recursion
#initialise a count for initial two numbers
print(0)
print(1)
count = 2

#create a funciton with two params
def Fib(prev1, prev0):
    #Uses the variable outside of function too
    global count
    #iterate to 19
    if count<= 19:
        newFibo = prev1 + prev0
        print(newFibo)
        prev0 = prev1
        prev1 = newFibo
        count += 1
        #Call on function again
        Fib(prev1, prev0)
    else: 
        return
Fib(1,0)
"""


#Fibonacci Sequence using Recursion
#F(n) = F(n-1) + F(n-2)
def F(n):
    if n<=1 :
        return n
    else :
        return F(n-1) + F(n-2)


print (F(19))