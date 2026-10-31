# Problem 1: Festival Lineup
def lineup(artists, set_times):
    mh = {}
    for i in range(len(artists)): #index
        mh[artists[i]] = set_times[i]
    return mh

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

# {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
# {}

# Problem 2: Planning App
def get_artist_info(artist, festival_schedule):
    """
    U:
    input: string of artist, dictionary of festival-schedule 
    output: return dictionay of artist's schedule 
        
    P:
    artist as key
    # for loop through the festival_schedule:
        if artist in schedule:
            return festival_schedule[artist]
        return {"message": "Artist not found"}
    Edgecase:
        artist not found
    """
    # for schedule in festival_schedule:
    if artist in festival_schedule:
        return festival_schedule[artist]
    return {"message": "Artist not found"}


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
# Problem 3: Ticket Sales
"""
U

P

I
"""



# Problem 4: Scheduling Conflict


# Problem 5: Best Set


# Problem 6: Performances with Maximum Audience


# Problem 7: Performances with Maximum Audience II


# Problem 8: Popular Song Pairs


# Problem 9: Stage Arrangement Difference Between Two Performances


# Problem 10: VIP Passes and Guests


# Problem 11: Performer Schedule Pattern


# Problem 12: Sort the Performers