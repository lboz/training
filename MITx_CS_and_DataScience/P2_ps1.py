###########################
# 6.00.2x Problem Set 1: Space Cows 

import time

#================================
# Part A: Transporting Space Cows
#================================
# check the current directory
import os
os.getcwd()
os.chdir('C:\\Users\\User\\Documents\\Lia\\edx\\MIT_IntroductionToComputerScienceAndDataScience\\ps1')
os.getcwd()


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict
#load_cows('ps1_cow_data.txt')

#load_cows('C:/Users/User/Documents/Lia/edx/MIT_IntroductionToComputerScienceAndDataScience/ps1/ps1_cow_data.txt')


# Problem 1
def greedy_cow_transport(cows,limit):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    start = time.time()

    cow_train = [[]]
    cow_capacities = [limit]
    cowsSort = sorted(cows.items(), key=lambda x: -x[1])
    for name, weight in cowsSort:
        for i, capacity in enumerate(cow_capacities):
            if weight <= capacity:
                cow_capacities[i] = capacity - weight
                cow_train[i].append(name)
                break
        else:
            if weight <= limit:
                cow_train.append([name])
                cow_capacities.append(limit - weight)
    end = time.time()
    print(end - start)
    return cow_train


# Problem 2

def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

### Uncomment the following code  and run this file
### to see what get_partitions does if you want to visualize it:
'''
for item in (get_partitions(load_cows('ps1_cow_data.txt'))):
     print(item)
cows = load_cows('ps1_cow_data.txt')

'''
def brute_force_cow_transport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowsCopy = cows.copy()
    for cow in cows.keys():
        if cows[cow] > limit:
            del cowsCopy[cow]
    # parts = get_partitions(sorted(cows.items(), key=lambda c: -c[1]))
    cowsPartition = list(get_partitions(cowsCopy.keys()))
    bestSublist = []
    savedList = []
    for sublist in cowsPartition:
        for partition in sublist:
            partitionWeight = 0

            for cow in partition:
                partitionWeight += cows[cow]

            if partitionWeight > limit:
                bestSublist = savedList
                break
            else:
                if len(bestSublist) == 0 or len(sublist) <= len(bestSublist):
                    bestSublist = sublist[:]
        savedList = bestSublist

    return bestSublist

 
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    startG = time.time()
    print('Greedy: ', str(len(greedy_cow_transport(cows, limit))), 'trips')
    endG = time.time()
    print('Time Greedy: ', (endG - startG))
    startB = time.time()
    print('Brute force: ', str(len(brute_force_cow_transport(cows, limit))), 'trips')
    endB = time.time()
    print('Time Brute Force: ', (endB - startB))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
#print(cows)
compare_cow_transport_algorithms()

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))


