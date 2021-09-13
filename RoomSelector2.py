# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:34:56 2021

@author: milan
"""
from scipy.optimize import linear_sum_assignment as lsa
import numpy as np

"""each entry in mat are each persons rankings of rooms 1 to 10.
1 is 1st or best, and 10 is last/worst """

"""
for rooms out of budget they were given a rank of 100 so they cant get thos rooms. 
to keep it fair these rankings were changed from the middle not the end
so the remaining top ranked toom is still 1, and bottom ranked room still 10 instead of 9
"""

#edit mat for your groups data. 
#eg 5 people would have 5 entries of 5 numbers 1 to 5. 
mat = np.array([[1,2,3,4,5,6,7,8,9,10],[3,2,4,5,1,6,8,7,9,10], [6,5,7,4,8,3,2,9,10,1],
       [3,2,4,5,6,1,7,10,8,9], [7,8,5,6,9,4,3,2,1,10],[1,2,3,4,5,6,7,8,9,10],
       [3,2,4,5,1,6,8,7,9,10], [6,5,7,4,8,3,2,9,10,1],[3,2,4,5,6,1,7,10,8,9],
       [7,8,5,6,9,4,3,2,1,10] ])


row_ind, col_ind = lsa (mat) 

for person in row_ind:
    
    print("person ", person, "gets room ", col_ind[person] +1 )
    
""" this is nicer but only gives one solution where there may be many
"""

