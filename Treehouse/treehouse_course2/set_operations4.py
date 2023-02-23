



# What do both omelets have in common?

denver.intersection(bacon)
denver & bacon


# What is unique to one of the omelets?

denver.difference(bacon)
denver - bacon


# What is unique to the other omelet?

bacon.difference(denver)
bacon - denver


uniques_list = list(set(duplicates_list))
sorted_uniques_list = sorted(set(duplicates_list))




def merge_lists(list_1, list_2):
    unique_list = set(list_1).union(list_2)
    return sorted(unique_list)

# or 

def merge_lists(list_1, list_2):
    unique_list = set(list_1) | set(list_2)
    return sorted(unique_list)




def subtract_lists(list_1, list_2):
    subtracted_list = set(list_1).difference(list_2)
    return sorted(subtracted_list)

def subtract_lists(list_1, list_2):
    subtracted_list = set(list_1) - set(list_2)
    return sorted(subtracted_list)


