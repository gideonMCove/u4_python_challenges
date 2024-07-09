# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
import math
def time_time():
   

    def minsToSecs(minute):
        answer = minute * 60
        return(answer)
    def hoursToSecs(hour):
        answer = hour * 3600
        return(answer)
    def daysToSecs(day):
        answer = day * 86400
        return(answer)
    def daysToHours(day):
        answer = day * 24
        return answer
    
    print("How many hours are in the month of june?")
    print(daysToHours(30))
    print("How many minutes are in the monthy of august?")
    y = daysToHours(31) * 60
    print(y)
    

time_time()
    

# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------

def mid(k):
    length = len(k)
    if length % 2 == 0:
        return ""
    else:
        middle = length // 2
        return k[middle]
print(mid("odd"))
print(mid("gideon"))

# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------


def ccNumber():
    newNumber = ""
    card = input("Enter your credit card number! ").strip()
    creditCardNumber = card[:-4]
    print(creditCardNumber)
    for creditCardNumber in creditCardNumber :
        newNumber = newNumber + "*"
    hiddenCard = newNumber + card[-4:]
    return hiddenCard
    
print(ccNumber()) #SUPER HARD! but also the best one.


# ---------------------------------



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
def online_count(object):
    print("objects", object)
    count = 0
    for key in object :
        print("key", key)
        if object[key] == "online" :
            count += 1

    return(count)
print(f"The number of people online: {online_count(statuses)}")





# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
def discount (a,b):
   b = b/100
   amount = a - (a *b)  
   return amount
print(discount(754,13))
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
def pythagoreanTheorum (a, b):
    hypotenouse = (a ** 2) + (b ** 2)
    return math.sqrt(hypotenouse)
print(pythagoreanTheorum(6,8))
# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
def fibonacciSequence (a,b):
    c = a + b
    d = c + b
    e = d + c
    f = e + d
    g = f + e
    h = g + f
    i = h + g
    j = i + h
    k = j + i
    return(c,d,e,f,g,h,i,j,k)
print(fibonacciSequence(7,8))
# ---------------------------------
