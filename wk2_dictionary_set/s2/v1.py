# Problem 1: Manage Performance Stage Changes
""""
stage stack []
for cancel [],put all the cancled schedule in stack

if schedule, push to stage[]
if calcel, push to cancle[], if not cancle, continue
if reschedule, stage.push(cancel.pop())

Edge case: if cancel is empty? continue


# change = Schedule A
# change_list = change.split()
# change_list = [“Schedule”, “A”]
"""

# change = Schedule A
# change_list = change.split()
# change_list = 
def manage_stage_changes(changes):
    stage = []
    cancel = []
    for change in changes: #split first
        change_list = change.split() #split based on space, give list
        if change_list[0] == "Schedule":
            stage.append(change_list[1])
        elif change_list[0] == "Cancel":
            if stage:#just check if stage is not empty
                cancel.append(stage.pop())
        elif change_list[0] == "Reschedule": #use elif not else, in case some other cases
            if cancel:
                stage.append(cancel.pop())
    return stage


print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 


# Problem 2: Queue of Performance Requests
"""
Queue of Performance Requests

You are organizing a festival and want to manage the queue of requests to perform. Each request has a priority. 

Use a queue to process the performance requests in the order they arrive 
but ensure that requests with higher priorities are processed before those with lower priorities. 
Return the order in which performances are processed.

def process_performance_requests(requests):
    pass
Example Usage:

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
Example Output:

['Music', 'Dance', 'Drama']
['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']
"""
"""
import heapq # heap library
use queue 
find each priority
use max_heap here (most heap is min_heap, min number come out first)

min heap -> minimum numbers come out first
heap = [1, 2, 3]
heappop(heap) = heap
heap = [-3, -2, -1] #add negative - infort min_heap, to make a max_heap
heappop(heap) = -3*-1 = 3 
"""
import heapq

def process_performance_requests(requests):
    heap = [] # create an empty heap 
    
    for priority, performance in requests: # priority = 3, performance = "Dance", tuple(1,2)
        heapq.heappush(heap, (-priority, performance)) #add performance for alpha order incase two perm has same priority
    result = [] #list of string
    
    while heap:
        priority, perf = heapq.heappop(heap)
        result.append(perf)
    return result

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))


# Problem 3: Collecting Points at Festival Booths
# Problem 4: Festival Booth Navigation
# Problem 5: Merge Performance Schedules
# Problem 6: Next Greater Event
# Problem 7: Sort Performances by Type