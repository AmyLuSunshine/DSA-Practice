# Problem 1: Counting Iron Man's Suits
"""
U:
i: list of string
o: return total count

P:
iteratively: go throgh for loop without use len()
treat input list as a stack[]
-create count 
-while list: # while [] - False
-pop() the input list
-count ++
return count 


recursively: 
Basecase: - stop the recursion, and bounce back
    # if not suits: 
    if idx == len(suits): return 0

Call the function by itself: helper func, iteration: 

return (1 + helper(idx+1) ) #helper func call itself

# another way is to slice the list, it create new list. big space issue and time complex
"""
def count_suits_iterative(suits):
    count = 0
    while suits:
        suits.pop()
        count += 1
    return count

#python tutor to see the value call stack
def count_suits_recursive(suits):
    #helper func
    def helper(idx):
        #recursion basecase: stop at the end of the len
        if idx == len(suits): return 0
        # print("idx",idx)
        # print("helper",1 + helper(idx+1))
        #recursion, func call itself when looping, as well count++
        return (1 + helper(idx+1)) 

    return (helper(0)) # idx = 0

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))

# Problem 2: Collecting Infinity Stones

"""
Understand:
Input: stones:List
Output: total_power:int

Match:
recusion

Plan:
helper function (i : int) -> 1+ function(i+1)
"""
def sum_stones(stones):
    def acc(i, n):
        if i == len(stones):
            return n
        n += stones[i]
        i += 1
        return acc(i, n)
    return acc(0, 0)

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))

# Problem 3: Counting Iron Man's Unique Suits
"""
U:
i: list of str
o: total num of distinct suits (no repeat)

Match:- seen similar problem ..

P:
set method: list string -> set(), return the len(set)

iteratively:

"""
def count_suits_iterative(suits):
    #create new set of what's seen
    seen = set()
    count = 0
    #loop through the string list
    for suit in suits:
        #if not seen, add to seen
        if suit not in seen:
            seen.add(suit)
            count += 1
    #return the length of seen set,len(seen)
    return count

def count_suits_recursive(suits):
    
    #define the helper function with parameter idx:
        #basecase: where recursion stops
        #stop when at the end of suits: idx == len(suit) return 0
        
        #recursion:helper()
        #
        #return helper(idx+1)
    




print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

# Problem 4: Calculating Groot's Growth




# Problem 5: Calculating the Power of the Fantastic Four




# Problem 6: Strongest Avenger




# Problem 7: Counting Vibranium Deposits





# Problem 8: Merging Missions





# Problem 9: Merging Missions II