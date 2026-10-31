''def lineup(artists, set_times): 
 
    input: 2 lists of strings
    output: dictionary
    edge case: empty lists/dictionary 
    plan: make dictionary, combine the lists

    lineup = {}
    for i in range(len(artists)): 
        lineup[artists[i]] = set_times[i]

    return lineup


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
'''
'''

'''
'''
def get_artist_info(artist, festival_schedule):
    return festival_schedule.get(artist, ('Not Found'))
    #     return '{"message": "Artist not found"}'
    # else: 
    #     return festival_schedule.get(artist)

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
'''
'''
Undestand:
input: dictionary
output : integer number (summation of all values)
edge cases: there is no ticket

Plan:
define a varibale sum to add all the values
use for loop over the dict
return the value
'''
'''
def total_sales(ticket_sales):
    sum = 0
    for tickets in ticket_sales.values():
        sum += tickets
    return sum
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))
'''
'''
Understand: inputs 2 dictionaries, outputs dictionary with same key-value pairs
Edge cases: Empty dictionaries and dictionaries without common pairs
Plan: Check the values between dictionaries if their keys are the same
Compare both items using .items()
Use for each loop
within each run of the loop check if that key exists within the other venue (if yes, check if the values match)
if so then return conflict (key and value)


'''
def identify_conflicts(venue1_schedule, venue2_schedule):
    for each somelist