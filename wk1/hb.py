# Q1
    # Complete the 'check_list' function below.
    #
    # The function is expected to return a BOOLEAN.
    # The function accepts INTEGER_ARRAY nums as parameter.
    #

def check_list(nums):
    # Write your code here
    """
    U:check if there're at lease #len nums
        that are >= len
    Big O(n)
    I: loop the list, for i in l
        have a counter
         if i >= len
            counter++
        if final counter < len:
            return false 
        return true 
    E:
    
    
        
    """
    # counter = 0
    # for i in nums:
    #     if i >= len(nums):
    #         counter += 1
    # if counter < len(nums):
    #     return False
    # return True

    # optimize: return False instantly if the 
    # first encounter in the list is smallere that len
    """
    counter = 0
    for i in nums:
        if i < len(nums):
            return False
        if i >= len(nums):
            counter += 1
    if counter < len(nums):
        return False
    return True
    """

lst = [1, 2, 3, 4]
print(check_list(lst))

lst = [4, 4, 4, 4]
print(check_list(lst))

lst = [5, 6, 7, 8]
print(check_list(lst))

"""
    I-Big O():If sorted, binary search
        
    
    
""" 






# Q2 # first_repeating_substring 
"""


"""
def first_repeating_substring(s, k):
    # Write your code here
    """
    hash map ?
    U:
       appear at least twice 
    
    I:
    
    E:
    
Input: s = "abcabcabc" k = 3
Expected Output: 0

Example Usage 2:
Input: s = "banana" k = 2
Expected Output: 1 
"""
 
    



# Q3

def special_array(nums):
    # Write your code here
   """
    U:
        return the number x if there're x number(counter) of n in list,
                            that satisfy n >= x;  
        otherwise return -1

        what's x looks like?
            x <= len
            x <= max

             
    I:O(n)
        count the counter

        if counter < X, return -1
        return x

      x is smaller then Max()
      counter = x in the end, return x  
        X is within the range of 0 to len of list
              x  t  len Max ct
        [0]   -1 1    1  0      0  
        [1]   1  1    1  1
        [2]   1  1    1  2      
        [0,0] -1 2    2  0
        [0,1] 1  2    2  1 
        [3,5] x  2    2  5

    sort first, 
    
    x (0, len+1)
    t = len
    
    //while x >=0
    have a counter
        if max < len, return -1
        else:
    loop through the lst backward:
        //start fr the max(lst), going down to test
        if ls(len-i) < t:
            t = 
            counter +1
   
    E:
    
    Optimization: Binary Search - logN
    """
    
nums.sort()




"""
Example 1:
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:
Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.

Example 3:
Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.

"""