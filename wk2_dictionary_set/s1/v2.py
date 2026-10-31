# Problem 12 Sort the Performers
"""
    U
    input: list of names, list of duration
    output: reordered list of names, based on duration in descending order High->low

    P
    hashmap - dic = {}, key-duration, value-name#
    for loop create the dic cobmibe names and duration
    
    sortkey = sorted(dic.keys(), reverse=True)

    result = []
    for loop through the sortkey list: num
        result.append(dic[num])
    return result

    
    # dic.value --> return a list
    # newdic = sorted(dic.value, reverse=True)
    #     mary; 180
    #     jogn: 165
    #     emma: 170
    #     dict.values()= [180,165,170]
        dict[value] xxx ---> dict[key] vvvv

    
"""
from collections import defaultdict # so you can use defaultdict
def sort_performers(performer_names, performance_times):
    """
    :type performer_names: List[str]
    :type performance_times: List[int]
    :rtype: List[str]
    """

    #  hashmap - dic = {[],[],[]}, key-duration, value-name#
    perform = defaultdict(list) #dic, it's val is already a lsit
    #     for loop create the dic cobmibe names and duration
    for name, times in zip(performer_names, performance_times): #parallel iteration using zip and tuple unpacking
        perform[times].append(name)

    """for i in range(len(performance_times)):
    
        perform[performance_times[i]].append(performer_names[i])
        # perform[performance_times[i]] = (performer_names[i]) # not work if 2 ppl have same duration"""
            
    #     sortkey = sorted(dic.keys(), reverse=True)
    sort_perform = sorted(perform.keys(), reverse = True)
    
    result = []
    #     for loop through the sortkey list: num
    for time in sort_perform:
        for name in perform[time]:# for element in perform[time]
            result.append(name) # dic[kay] returns a list = [a, b, c] emtire list
    return result

# performer_names1 = ["Mary", "John", "Emma"] # ['Mary', 'Emma', 'John']
# performance_times1 = [180, 165, 170, 165]

# performer_names2 = ["Alice", "Bob", "Bob"]
# performance_times2 = [155, 185, 150]

# # if two ppl have the saem duration
performer_names3 = ["Mary", "John", "Emma", "Bob"]
performance_times3 = [180, 165, 170, 165]

# print(sort_performers(performer_names1, performance_times1)) # expect: ["Mary", "Emma", "John"]
# print(sort_performers(performer_names2, performance_times2)) # expect: ["Bob", "Alice", "Bob"]
print(sort_performers(performer_names3, performance_times3))# expect: ["Mary", "Emma", "John", "Bob"]


