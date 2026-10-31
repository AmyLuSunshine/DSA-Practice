def most_endangered(species_list):
    # set the number to an infinity float
    min_population = float('inf')
    species = ''
    for i in range(len(species_list)):
        if species_list[i]["population"] < min_population:
            min_population = species_list[i]["population"]
            # species = species_list[i]["name"]
            species = species_list[i].get("name", "Does not existy")
            print(species)
    return species


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))


# Problem 2
'''
input: 2 strings
output: number



'''

def count_endangered_species(endangered_species, observed_species):
    list_A = list(endangered_species)
    list_B = list(observed_species)
    print(list_A)
    sum = 0
    for item in list_A:
        sum = sum + list_B.count(item)
       
    return sum

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2)) 


        

def count_endangered_species2(endangered_species, observed_species):
    animal = set(endangered_species)
    
    sum = 0 
    for a in observed_species:#loop through the string
        if a in animal:
            sum += 1
    return sum

print(count_endangered_species2(endangered_species1, observed_species1)) 
print(count_endangered_species2(endangered_species2, observed_species2)) 

def count_endangered_species2(endangered_species, observed_species):
    count_map = {}
    for char in observed_species: 
        if char not in count_map: 
            count_map[char] = 1
        else: 
            count_map[char] += 1
    
    total = 0
    for char in endangered_species: 
        if char in count_map: 
            total += count_map[char]
            
    return total
print(count_endangered_species2(endangered_species1, observed_species1)) 
print(count_endangered_species2(endangered_species2, observed_species2)) 

# Problem 3: Navigating the Research Station
def navigate_research_station(station_layout, observations):
    """
    U: 
    specific observe from the station,
    count the index diff, and add them up 

    I:
    data structure: dictionary with key value pair
    hash: make a 26 length dic, key is the char, value is the idx

    new variable count
    for char in observe:
        if char in station:
            count adds the idx value of that char key
    return count
    
    [0,1,2,3,4,5,6,7...25]
         2 ** + 2 - 0
       1   ** + 2 - 1
     0     ** + 1 - 0
    """
    station_hash = {}
    for idx,s in enumerate(station_layout):
        if s not in station_hash:
            station_hash[s] = idx

    prev = observations[0]
    diff = station_hash[prev]
    for o in observations:
        if o in station_hash:
            # print("M",prev, o, station_hash[prev],station_hash[o])            
            diff += abs(station_hash[o] - station_hash[prev]) 
            prev = o
    return diff 

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"
observations3 = "az"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))
print(navigate_research_station(station_layout2, observations3))
# Problem 4: Prioritizing Endangered Species Observations



# Problem 5: Calculating Conservation Statistics


# Problem 6: Wildlife Reintroduction



# Problem 7: Count Unique Species



# Problem 8: Equivalent Species Pairs

