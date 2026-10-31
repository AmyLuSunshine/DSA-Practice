# Problem 1: New Horizons
# Problem 2: Greet Player
# Problem 3: Update Catchphrase

# Problem 4: Set Character
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
	
    def set_catchphrase(self, new_catchphrase):
        # is valid,
        if len(new_catchphrase) < 20 and new_catchphrase.isalpha():
            for char in new_catchphrase:
                if not char.isalpha() or not char.isspace():
                    print("Invalid catchphrase")
                    return
                self.catchphrase = new_catchphrase
        # print("Catchphrase updated")
        if len(new_catchphrase) >= 20:
            print("Invalid catchphrase")
        
        print("Catchphrase updated")
        

        # print "Catchphrase updated".

        # Otherwise,print ....



alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)

alice.set_catchphrase("#?!")
print(alice.catchphrase)


# Problem 5: Add Furniture
# Problem 6: Print Inventory
# Problem 7: Group by Personality
# Problem 8: Telephone



# def message_received(start_villager, target_villager):
#     if not start_villager:
#        return "Error: No villager input"
#     current_villager = start_villager
#     while current_villager.neighbor:
#         if current_villager.neighbor == target_villager:
#           return True
#         else:
#           current_villager = current_villager.neighbor
#     return False



# Problem 9: Nook's Cranny
# Problem 10: Timmy and Tommy
# Problem 11: Saharah
# Problem 12: Print Players Linked List