# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 11:41:10 2019
youtube video: 
https://www.youtube.com/watch?v=JRCay58jOso
1h53
@author: LB


TBD:
    - convert A -> B -> C  using Graph Theory
    - add examples in input - ex: 5 kg to lb...

"""

# Given a set of pairs of conversions (kg to lb, kg to g, m to feet, etc), 
# continually ask the user for input in one of the following formats:
#  - "5 kg in lb" this will print the conversion to the specified unit
#  - "5 kg to ALL" this will print all conversions that are possible
#  - "5 kg to lb g" this will print all conversions to specified units 

# Direct conversions only - if we know kg to g and g to lb,
#  we won't be able to find kg to lb (unless there is a direct entry for how 
#  to convert these).
# User enters "q" without quotes to quit. 


''' 1 to 1 conversion only'''


mapping = {("kg","g"): 1000,
           ("kg","lb"): 2.20462,
           ("g","ct"): 5,
           ("g","oz"): 0.035273,
           ("kg","oz"): 35.273,
           ("m","ft"): 3.28084,
           ("km","mi"): 0.621371,
           ("m","yd"): 1.09361}

# function to generate more efficient dict
def unroll_dict(d):
    mapping_unrolled = {}
    for k in d.keys():
        
        if k[0] not in mapping_unrolled:
            # when k not in d create new list and add first value
            mapping_unrolled[k[0]] = []
            mapping_unrolled[k[0]].append((k[1],d[k]))
        else:
           # when key is already in d- append to list
            mapping_unrolled[k[0]].append((k[1],d[k]))
    
        if k[1] not in mapping_unrolled:
            mapping_unrolled[k[1]] = []
            mapping_unrolled[k[1]].append((k[0],1.0/d[k]))
        else:
            mapping_unrolled[k[1]].append((k[0],1.0/d[k]))
    return mapping_unrolled
#print(unroll_dict(mapping))
    
def convert_units(user_input):

    # transforms the str input to a list (5 kg in lb)
    val_list = user_input.split()
    # lower case transform
    val_list = [x.lower() for x in val_list]
    val = val_list[0]
    unit = val_list[1]
    unit2 = val_list[3:]
    allFlag = False
    
    if 'all' in unit2:
        allFlag = True
    elif len(val_list) == 2:
        allFlag = True
        
    conversion = "" 
    # if unit not in dictionary
    if unit not in mapping_unrolled.keys():
        print("No conversion found")  
        return

    # check unit in the unrolled dictionary
    if allFlag:
        for map_vals in mapping_unrolled[unit]:
            conversion += str(map_vals[1] * float(val)) + ' ' + map_vals[0] + '\n'
    else:
        for map_vals in mapping_unrolled[unit]:
            if map_vals[0] in unit2:
                conversion += str(map_vals[1] * float(val)) + ' ' + map_vals[0] + '\n'
        
    # if unit not in dictionary
    if conversion == "":
        print("No conversion found") 
    else:
        print(conversion)
# end of function

# beginning of program
user_input = input("Enter something to convert: ") 

mapping_unrolled = unroll_dict(mapping)
while user_input != 'q':
    convert_units(user_input)
    user_input = input("Enter something to convert: ")   
