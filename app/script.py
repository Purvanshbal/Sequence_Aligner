# Your actual script code goes here
# For example:
import numpy as np
def add(a, b):
    return a + b

def check_input(seq):
    for s in seq:
        if s not in ['A', 'C', 'G', 'T']:
            return False


    return True

def make_score_matrix(array, gap_penalty):
    array = np.reshape(np.array(array), (4, 4))
    mapping = {0:'A', 1:'G', 2:'C', 3:'T'}
    score = {}

    for i in range(array.shape[0]):
        char = mapping[i]
        score[char] = {}
        for j in range(array.shape[1]):
            score[char][mapping[j]] = array[i][j]
        
        score[char]['-'] = gap_penalty
    
    score['-'] = {}
    
    for i in range(array.shape[0]):
        score['-'][mapping[i]] = gap_penalty

    score['-']['-'] = 1

    return score



    
    
   

