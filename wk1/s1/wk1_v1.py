# P1 Hundred Acre Wood
# define the function
def welcome():
    print("Welcome to The Hundred Acre Wood!")
# call the function
welcome()

# P2 Greeting
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

greeting("Michael")
greeting("Winnie the Pooh")

# P3 Catchphrase
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
         print(f"Sorry! I don't know {character}'s catchphrase!")

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)

# Problem 4: Return Item
def get_item(items, x):
    # Check if x is within the valid index range [0, len(items) - 1]
    if(0 <= x <= len(items)):
        print(items[x])
    else:
        print("None")

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)

# Problem 5: Total Honey
# U: return the sum of the number list
# P: use for loop to add each in order
# I: 

def sum_honey(hunny_jars):
    total = 0
    for i in hunny_jars:
        total += i
    print(total)

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)

sum_honey([12, 7, 31, 5])



# Problem 6: Double Trouble
def doubled(hunny_jars):
    for i in hunny_jars:
        hunny_jars[i-1] = i*2
    print(hunny_jars)

hunny_jars = [1, 2, 3]
doubled(hunny_jars)


# Problem 7: Poohsticks

"""
# XYZ
# REACTO
# UPI
U:
    input is a list of integers(like array) of race times, and a number as threshold time.
    Return the count of times in the list that's less than threshold.
P:
    Since a list is sorted already, so we loop through the list, 
    and count the times that's smaller than threshold

I:

Edgecase: race time is empty
Improve time complex:  threshod: len len+1 -1 0 test 

    mid = 4
    threshod = 4 
    l    
                          r   
              m
                    t     
    [1, 2, 3, 4, 5, 6, 7, 8]
              ^
     ^      

find first smallest element less than threshold as another question


"""
def count_less_than(race_times, threshold):
    # method 1: n, naive approach
    """count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count"""
    # method 2: log n, it's sorted aray/list, use binary search
    count = 0
    lp = 0
    rp = len(race_times)-1
    while lp <= rp:
        mid = (lp + rp)  // 2   # e.g. 7 // 2 = 3
        if race_times[mid] >= threshold:
            rp = mid - 1
        else:
            lp = mid + 1
        # count += 1
    return lp


# race_times = [1, 2, 3, 4, 5, 6]
# threshold = 4
# count_less_than(race_times, threshold)

# race_times = []
# threshold = 4
# count_less_than(race_times, threshold)

race_times =[1, 2, 3, 4, 5, 6, 7, 8]
threshold = -1
print(count_less_than(race_times, threshold))


# Problem 8: Pooh's To Do's
"""
Understand:


Plan:

"""


def print_todo_list(tasks):
	# input sanity check
    assert len(tasks)>0, "the task should be greater than 0!"

    print("Pool's To Dos:")
    """for idx, t in enumerate(tasks):
        # enumerate will return idx and element
        print(idx+1, ". ", t)"""

    for t in range(len(tasks)):
        print(t+1, ". ", tasks[t])

tasks = ["Count all the bees in the hive", 
"Chase all the clouds from the sky", 
"Think", 
"Stoutness Exercises"]
print_todo_list(tasks)

# tasks = []
# print_todo_list(tasks)



# Problem 9: Pairs
"""
even odd questions
return false if it's odd

"""
def can_pair(item_quantities):
    for i in item_quantities:
        if i % 2 != 0:
            return False
    return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))



# Problem 10: Split Haycorns
"""
I:
    divisors: 1 and itself, 2*3 = 6
    prime number (4 is not X):
        1 and itself (e.g., 2, 3, 5, 7, 11)
P:
    eg: 18
    1 18
    2 9    
    3 6
    5 X

    eg: 75
    1 75
    2 32.5
    3 25
    naive solution:
        loop through prime numbers, and divide the num

Solution:
     if num / 2++ > 0: continue   

    NAIEVE METHOD:1 
        hashmap() 
        set and map

    METHOD 2:
    range(start,end): start is inclusive, end is exclusive
    //: is integer division, drop the decimal
    floating point problem
    80 // 2 = 40, range end is not include, 
    82 // 2 = 41, 41 is not include, then 40 is include
Sort:
    two array, append and pre pend, then merge for sort 
    if want to scale solution, quantity is 10milliion,
        array is not scalable, so use link list (METHOD 4)
"""
def split_haycorns(quantity): # Has 5 solutions, OPTIMIZATION
    # method 2: n
    """arr = [1]
    # to include the end for range()
    for val in range(2,(quantity+2)//2):
        ans = val if quantity % val == 0 else 0
        # remove duplicates:ans >= quantity / val
        if ans != 0 and ans > quantity / val:
            if ans > quantity // val:
                arr.append(quantity // val)# append opposite divisor
                arr.append(ans)
            else:
                arr.append(ans)
                arr.append(quantity // val)
             
    if quantity != 1:
        arr.append(quantity) 
    return arr
    """
    # method 3: big o of square root n, faster  sqrt of n in math
    """
    OPTIMIZATION:

    ans = []
    for i in raneg(1, int(quantity ** 0.5)):
    if quantity % i == 0: divsors.append(i)
    divisors.append(quantity // i)
    if i != quantity // i
    def split_haycorns(quantity):
        
    """
    divisors = []
    # ** 0.5 squart root. power of 1/2, 
    for i in range(1, int(quantity ** 0.5) + 1): # 81 loop go(1,10) 1-9
     
        if quantity % i == 0:
            divisors.append(i)

            if i != quantity // i:
                divisors.append(quantity // i)
    return divisors 

quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))

quantity = 80
print(split_haycorns(quantity))
"""

"""


# Problem 11: T-I-Double Guh-ER
"""
U: remove tiger letter from the string and retrun rest
I - N^2: loop through string list
    if is not tiger letter, + in the new string 

I - O(N)
    split and work on same array
    pointer

    "trigger"
    [t,r,i,g,g,e,r]
    "tiger"
"""
def tiggerfy(s):
#    answer = ""
#         for i in s:
#         if i not in "tiger":
#             answer += i
#     return answer
    
    #  list(), type cast, make string an list
    # backward:last to 0, 0 index never change
    s = list(s)
    tiger = ['t','i','g','e','r'] # aray is a list in py
    tiger = {'t', 'i', 'g', 'e', 'r'} #set 
    i = len(s) - 1
    while i >= 0:  
        if s[i].lower() in tiger:
            s.pop(i)
        i -= 1
    return "".join(s)

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))


# Problem 12: Thistle Hunt
"""


"""
def locate_thistles(items):
    # lamda, no name function (sort)
    answer = []
    for idx,i in enumerate(items):
        if i == "thistle":
            answer.append(idx)
    return answer


items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))