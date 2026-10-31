# Problem 1: NFT Name Extractor
"""
UMPIRE

U:
Input is list of dictionary
output is the list - dictionary's name

Match:

P:
names = []
iterate through the list: - > {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    name.append(dic_name.value) 

I:

Review:

E:
no name key in the dictionary


"""
def extract_nft_names(nft_collection):
    names = []
    for name_list in nft_collection:
        # print(name_list.get("name")) #.get() will skip the error if the name is not there
        names.append(name_list["name"])
    return names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

# Problem 2: NFT Collection Review
"""
UMPIRE

U:
Review the provided code and find the error that is leading to incorrent outputs
Explain the bug and fix the code
# Input: list of dictionaries
# Output: list of name-value


Match:

P:
Go though each line and find if the syntax/logic is implemented correct for the end goal of the function

I:
Identify the bug: It returned every single chars list, full strings "nft_names += nft["name"]"
Fix the code: instead of using += which adds one letter at a time, we use append which grabs the whole string

Review:

E:
no name key in the dictionary


"""

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:# {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
        # print("nft name: ", nft["name"])
        nft_names += nft["name"]
        # nft_names.append(nft["name"]) 
    return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

# Problem 3: Identify Popular Creators
"""
# NFT: None Foundable Token , Block Chain Artist are NFT Creators

U:
We're trying to identify the creator with the most amount of NFTs in a given collection

P:
Loop through each collection and increment the name of creator for each NFT in that collection
Input: List containing dictionaries that represent NFTs
Output: A string of the name of that creator

Implement:
checked  = frequency dictionary init
for nft in collection
    check frequency
    if creator is in checked
        increment their value by +1
    else
        add that creator to checked (key-name:value-frequency)
        
max name = empty string
max value of -inf (negative infinity)
for creator in checked
    if creator value > max:
        max name is going to be that creator
        max value is going to be its value

return max name
"""
def identify_popular_creators(nft_collection):
    checked = {}
    for nft in nft_collection:
        if nft["creator"] in checked:
            nft["creator"] += 1
        else:
            nft["creator"] = 1
    
    max_name = ""
    max_value = float('-inf')
    for creator, count in checked.items():
        if count > max_value:
            max_value = count
            max_name = creator

    return max_name

            
#joseph, let's join discord and finish this question
#yall wanna connect on linkedin? www.linkedin.com/in/saito-c-69a3b23b7  ok
            
            

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))


# Problem 4: NFT Collection Statistics
"""
Understand:
i:a list of dics
o:ave val of all the item
  return 0 if emtpy list
eg: empty list, no val => 0

Match:
Plan:

float sum = 0
if not nft_collection:
    return 0
loop nft through the list: nft[0] = {dic list}
    sum += nft[i][value]
average = sum / len(nft_collection)
return average
"""

def average_nft_value(nft_collection):
    sum = 0
    if not nft_collection:# if not means if sth is not exist
        return 0
    for nft in nft_collection:
        sum += nft["value"]
    average = sum / len(nft_collection)
    return average
            
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))

# Problem 5: NFT Tag Search
"""
Understand: 
returns a list of NFTs that contain a specific tag from a collection of NFT collections.
Input: A list of NFT collections (each collection is a list of dictionaries) and a tag to search for.
Output: A list of NFTs (nft names-val) that contain the specified tag.
Plan:
1. Initialize an empty list to store the matching NFTs.
2. Iterate through each collection in the nft_collections list.
3. For each collection, iterate through each NFT (dictionary) in that collection.
4. Check if the specified tag is present in the "tags" list of the NFT.
5. If the tag is found, append the NFT name to the list of matching NFTs.

list_s = ["sunset", "landscape"]
if s in list_s:
"sunset" in list_s => True
"""

def search_nft_by_tag(nft_collections, tag):
    res = []
    for collection in nft_collections:
        for nft in collection:
            if tag in nft["tags"]:  #O(n)
                res.append(nft["name"])
    return res

nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))


# Problem 6: NFT Queue Processing
"""
U:
i:a list of dicts in origin order
o:a list of nft names in origin order - Queue
e:empty nft, return []
P:
res = []
loop through the nft list:
    res.append(nft["name"])
return res

"""
def process_nft_queue(nft_queue):
    res = []
    for nft in nft_queue:
        res.append(nft["name"])
    return res

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))



# Problem 7: Validate NFT Addition
"""
U:
i: a list of actions (add, remove) pair
o: return T if balenced pair, F otherwise
eg: order matters, add then remove 

[](){}

P:
pair_hashmap = {"add":"remove"}
add_stack = []
loop act through the actions:
    if act == add: append to add_stack
    else:
        #if add_stack: # if stack is not empty, len is > 0
        if not add_stack: # if stack is empty, len = 0
            return False
        else:
            add_stack.pop()
return True 

"""
def validate_nft_actions(actions):
    # pair_hashmap = {"add":"remove", "modify": "undo"}
    # add_stack = []
    adds = 0
    for act in actions:
        if act == "add":
            adds += 1
        else:
            if adds == 0:
                return False
            adds -= 1
    return True
def validate_nft_actions(actions):
    pair_hashmap = {"add":"remove"}
    add_stack = []
    for act in actions:
        if act == "add":
            add_stack.append(act)
        else:
            if not add_stack:
                return False
            else:
                add_stack.pop()
    return True

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))




# Problem 8: Find Closest NFT Values
"""


"""

# def min(nft_values, key = lambda x: abs(x - budget)):
#     closest_value = None
#     closest_diff = float('inf')
#     for value in nft_values:
#         diff = key(value)
#         if diff < closest_diff:
#             closest_diff = diff
#             closest_value = value
#     return closest_value
def find_closest_nft_values(nft_values, budget):

    smallest_value = min(nft_values, key=lambda x: abs(x - budget)) #O(N)
    nft_values.remove(smallest_value)#O(N)  # find the closest value to budget
    second_smallest_value = min(nft_values, key=lambda x: abs(x - budget)) #O(N) # find the second closest value to budget
    # second_smallest_value = float('inf')
    # for value in nft_values:
    #     if value != smallest_value and abs(value - budget) < abs(second_smallest_value - budget):
    #         second_smallest_value = value

    return [smallest_value, second_smallest_value]


nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))

# lambda practice
