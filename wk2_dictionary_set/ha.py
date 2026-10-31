def find_min_index_of_repeating(arr):
    # Write your code here
    """
    U:
    input: list of nums
    output: min idx of the repeated nums
    P:
    hash = {}
    loop through the arr:
        if not in hash:
            add to hash[1] = i -> key:num value: idx
        return hash[num]
    return None
    I:
    """
    result = {}
    for i, num in enumerate(arr):
        if num not in result:
            result[num] = i
        else:
            return result[num]
    return None   





# 2
def intersection(nums1, nums2):
    # Write your code here
    """
    U: 
    input is two list of nums, 1 and 2
    output is the repeated nums in ascending order 
    I:
    # turn list into set() to remove duplicate
    # n1: 1 2
    # n2: 2
    
    # sort nums1 and nums2 for ascending  O(n logn)
    
    visited = set() #hash set()   - O(1)
    loop through nums1:  O(n1)
        is not in visited:
            add to visited
    loop through nums2:  O(n2)
        if in visited:
            result.append(num)
    sort the result = []
    
    """
    visited = set() #hashset = dic w/ value
    result = []
    for n1 in nums1:
        if n1 not in visited:
            visited.add(n1) # hash and set use .add(), list use .append()
    pre = float('inf')
    nums2.sort()
    for n2 in nums2:
        if n2 != pre and n2 in visited:
            result.append(n2)
        pre = n2
    result.sort()
    return result
            
# 3
def roman_to_integer(s):
    # Write your code here
    """
    U: given Roman numeral, convert to int
    Special case:
      Roman is Descending order,  ++ 
      when see ascending order, idx+1 - idx
    Detail:
      compare two idx, remember to skip after in this situation
    P:
    have a predefined hashtable with 7 tables:key-Sybol,val-val
    result = 0
    
    loop through the idx fr Roman string,
        if roman[idx] < roman[idx+1]:
            result += roman[idx+1] - roman[idx]
            idx += 2
        else: 
            result += roman[idx]
    """
    result = 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    for idx in range(len(s)):
        if idx+1 < len(s) and roman[s[idx]] < roman[s[idx+1]]:
            result -= roman[s[idx]]
        else: 
            result += roman[s[idx]]
    return result
    