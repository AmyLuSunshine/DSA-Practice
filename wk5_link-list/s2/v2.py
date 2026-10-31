# Problem 1: Calculate Tournament Placement
"""
    Class:
        with attributes:
            character (name)
            kart type?
            race_outcomes: place in race
            
    Inputs:
        List of opponents (other Player objects) with same amount of race outcomes
        
    Output:
        Return the average rank in the tournament
"""

class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        # Get the averages of the other players
        opponent_avgs = []
        for opponent in opponents:
            opponent_avgs.append(sum(opponent.race_outcomes) / len(opponent.race_outcomes))
        
        # Check for lowest average and return that player
        lowest_player = 1
        lowest_avg = sum(self.race_outcomes) / len(self.race_outcomes)
        lowest_opponent = opponent_avgs.index(min(opponent_avgs)) + 2
        lowest_opp_avg = min(opponent_avgs)
        
        if lowest_opp_avg < lowest_avg:
            lowest_player = lowest_opponent
            # my laptop died
        return lowest_player
    
player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(player1.get_tournament_place(opponents))

# Problem 2: Update Linked List Sequence




# Problem 3: Insert Node as Second Element



# Problem 4: Increment Linked List Node Values




# Problem 5: Copy Linked List
# Problem 6: Making the Cut
# Problem 7: Remove Racer
# Problem 8: Array to Linked List


# Problem 9: Convert Singly Linked List to Doubly Linked List





# Problem 10: Find Length of Doubly Linked List from Any Node