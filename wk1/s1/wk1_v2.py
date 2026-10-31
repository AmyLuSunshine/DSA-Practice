#Problem 1: Reverse Sentence
# U: Reverse the order of the words in a sentence, return origin if one word
# P: if lenth is 1, return origin; 
    # input is a string, split the sentence up by space(.split), put into a list,
    # reverse function()
# I
# Edge case: if there's no word: return none
def reverse_sentence(sentence):
    if len(sentence) == 1:
        print(sentence)
    words = sentence.split()
    words.reverse()
    # ['fluff', 'with', 'stuffed', 'all', 'cubby', 'little', 'tubby']
    reversed_sentence = " ".join(words)
    print(reversed_sentence)

sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)



# Problem 2: Goldilocks Number
# U: give goldilocks num NOT the smallest, NOT the biggest, return rest;  
#                                                           return -1 if there is no such number.
# P: input is the list of distinct positive integers nums;  2 1 3
    # method 1
    #  find the max() and then remove() it  (alternative: pop the index ) 3
    #  find the min() and remove() it: 1
    
    # method 2
    # goldilocks,
    # find the max and min
    # golilocks copy all but not max and min ---- slice()    lst[A:B]
    # len(nums)


def goldilocks_approved(nums):


nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)



# Problem 3: Delete Minimum



# Problem 4: Sum of Digits




# Problem 5: Bouncy, Flouncy, Trouncy, Pouncy


# Problem 6: Squared



# Problem 7: NaNaNa Batman!



# Problem 8: Find the Villain



# Problem 9: Odd



# Problem 10: Up and Down






# Problem 11: Running Sum






# Problem 12: Shuffle
"""
U: split in half and then shuffle
I: use list slice[:], split into two lists
    create a new empty []
    then for range 0 - len/2:
        append from  both lists
"""
def shuffle(cards):
    half = len(cards)//2
    left = cards[:half]
    right = cards[half:]
    shuffled = []
    for idx in range(0,half):
        shuffled.append(left[idx])
        shuffled.append(right[idx])
    return shuffled

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))

"""
I: two pointers


"""
