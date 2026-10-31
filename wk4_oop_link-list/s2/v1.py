# Problem 1: Planning Your Daily Work Schedule
"""
U:Find two sums fr the list that exactly = available time
    Input: list of nums
    output: T F
P:  
    set(): distinguish
  create a set seen = set(): #remove duplicate
    loop through the list of nums
        if available_time - num in seen:
            # seen[num] = available_time - num
            return T
            
        if not seen:
            add number in set
    return F
E:
empty list , is covered

O(n) -> both time and space

"""
def find_task_pair(task_times, available_time):
    pair = set()
    for time in task_times:
        if available_time - time in pair:
            return True
        pair.add(time)
    return False

task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))

# Problem 2: Minimizing Workload Gaps
'''
U: 
Input: a list of tuples where each tuple represents a 
work session with a start and end time (both in 24-hour format 
as integers, e.g., 1300 for 1:00 PM)
Output: the smallest gap (in minutes) between any two consecutive work sessions
Edge Cases:

Plan:
- Initialize a gap variable
  0        1    2    3 
  [t[1], t2[0]]
- Loop through the work_sessions  list[::2]
- Calculate current gap: Next Tuple[0] - Current Tuple[1]
    
- if current gap < previous gap
    - Update the gap
- Convert the gap to minutes
    hrs: num1 / 100 - num2/100 = 1*60
    minut: num % 100 - num2 % 100 = min
return hrs + minuts
    
    - eg, 1100 - 1030 = 70 ( 30 minutes) = 70/100*60
    - 1300 - 1100 = 200 (120 minutes) = 200/100*60

    1100 - 1030
    11 - 10 = 1
    00 - 30 = -30 + 60  = 30 minutes

for i in range(len(work_sessions)):
    gap = worksessions[i+1][0] - worksessions[i][1]
    hrs = gap / 100 * 60 + gap %100
'''


def find_smallest_gap(work_sessions):
    min_gap = 1440
    for i, session in enumerate(work_sessions):
        gap = (session[i+1][0]/100 - session[i][1]/100)*60 + (session[i+1][0]%100 - session[i][1]%100)
        if gap < min_gap:
            min_gap = gap
    return min_gap
  

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))



# Problem 3: Expense Tracking and Categorization++





# Problem 4: Analyzing Word Frequency





# Problem 5: Validating HTML Tags





# Problem 6: Task Prioritization with Limited Time





# Problem 7: Frequent Co-working Spaces





# Problem 8: Track Popular Destinations