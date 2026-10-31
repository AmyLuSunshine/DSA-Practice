# Problem 1: Post Format Validator
"""
U:input: string of tags
    output: T for matching tags, F for unmatching tags
    Edge Case: Empty string, len is odd number(return F if so)

    every opeing has a closing
    
    (([])) - T
    ()[]{} - T
    ([)] - F
    (]) - F
    )( - F
    () - T

P:
    use stack data strcture
    loop over the string:
        if left tag, push to stack
        if right tag:
            if stack is empty, return F
            if stack.pop left not match to the next item right: reutnr F
"""


"""
def is_valid_post_format(posts):
    left_tag = [] #stack, use list in py, list= array
    l_tag = set(["(", "[", "{"])
    print("posts",posts)
    for tag in posts:
        if tag in l_tag:
            left_tag.append(tag)
            print("left_tag",left_tag)
       
        if not left_tag: return False  # i think this line may need to go inside the else - Heidy
        else:
            left_pop = left_tag.pop()
            print("left_pop",left_pop)
            print("left_tag",left_tag)
            if (left_pop == "(" and tag != ")"):
                print("()")
                return False
            elif (left_pop == "[" and tag != "]"):
                print("[]")
                return False
            elif (left_pop == "{" and tag != "}"):
                return False

            # if (left_tag[len(left_tag)-1] == "(" and tag == ")"):
            #     return False
            # elif  (left_tag[len(left_tag)-1] == "[" and tag == "]"):
            #     return False
            # elif  (left_tag[len(left_tag)-1] == "{" and tag == "}"):
            #     return False
    return True

print(is_valid_post_format("()"))  #T"""
# print(is_valid_post_format("()[]{}"))  #T
# print(is_valid_post_format("(]")) #F

# can think of another way to solve this
# it seems moving the if not left_tag : return false inside the else case works , try it out
# I dont remember what expected output was lol
# yes it seems we just needed to move the check iinside the else
# since the first if was for if we enounter an open tag
# and the else was for if we encounter a closing tag so thats where we check if the stack is empty --> return False
# feel free to DM me on slack for any other questions! 

# works!! print True!!! Thank you so much ~ Good night ~ 
# yaayyy! welcome going to head out now goodnight to you too !
def is_valid_post_format2(posts):
    left_tag = [] #stack, use list in py, list= array
    l_tag = set(["(", "[", "{"])
    print("posts",posts)
    for tag in posts:
        if tag in l_tag:
            left_tag.append(tag)
            print("left_tag",left_tag)
       
        else:

            if not left_tag: return False  # i think this line goes here

            left_pop = left_tag.pop()
            print("left_pop",left_pop)
            print("left_tag",left_tag)
            if (left_pop == "(" and tag != ")"):
                print("()")
                return False
            elif (left_pop == "[" and tag != "]"):
                print("[]")
                return False
            elif (left_pop == "{" and tag != "}"):
                return False
    return True

print(is_valid_post_format2("()"))


# Problem 2: Reverse User Comments Queue



# Problem 3: Check Symmetry in Post Titles




# Problem 4: Engagement Boost



# Problem 5: Content Cleaner



# Problem 6: Post Editor



# Problem 7: Post Compare