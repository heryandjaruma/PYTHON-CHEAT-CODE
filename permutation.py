import numpy as np

def get_permutation_indexing(start_num:int, end_num:int): # IMPLICIT
    listed = list(range(start_num,end_num+1))
    combination = np.array(np.meshgrid(listed, listed)).T.reshape(-1,2)
    combination = np.sort(combination)
    combination = np.unique(combination, axis = 0)
    combination = [item for item in combination if item[0] != item[1]]
    return combination

for index, item in enumerate(get_permutation_indexing(1,6)):
    print(index, item)