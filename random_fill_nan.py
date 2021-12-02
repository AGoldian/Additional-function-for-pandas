import random

def nan_fill_random(column_name, nan):

    '''The function fills the list with random values from the available data, keeping the proportions.'''
    
    list_values = set(column_name)
    try : 
        list_values.remove(nan)
    except : 
        return(column_name)
    column_name = column_name.apply(lambda x: x if x != nan else random.choice(list(list_values)))

    return(column_name)