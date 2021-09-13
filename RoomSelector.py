# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 12:12:56 2021

@author: milan
"""


""" 
make matrix each column is for a room
each row is a persons prefernce for that room
 loop through rows/ columns where the index sequence is the room selection/path
 sum the preferences along the path
 finding the paths with the minimum sum
 
"""
"""
has to check available paths
so fixes first person in row 0 column i of n
then second person (row 1) in column j of n without i 
then third person etc

loops have to loop over the numbers with the restrictions from the previous loop
"""
import random

columns = range(10)
minTot = 100

"""edit here enter your groups data"""   

    
people = ["lucy", "Olivia", "Tom","Rosa","Luke","Rory", "Kismat", "Kieron", "Milan","Megan"   ]

"""each entry in mat are each persons rankings of rooms 1 to 10. 
here Lucys entries are 8,7,1,2,6,9,10,5,3,4
 1 is for 1st so 1 is best, 10 is worst. 
Liv's are the enxt set of 10 and so on."""

mat = [[8,7,1,2,6,9,10,5,3,4],[4,5,1,2,6,9,10,7,3,8],[3,8,1,2,7,9,10,6,4,5],[9,7,10,8,3,5,6,1,4,2],[4,7,2,1,8,9,10,6,5,3],
       [4,7,3,2,6,8,9,10,5,1],[2,8,100,1,9,7,5,10,4,3], [100, 3, 100,100,9,1,2,10,100,100], [5,7,8,4,3,9,10,6,2,1], [4,8,3,1,5,7,10,6,9,2]  ]

"""for 10 people we need only 9 loops actually but there are 10 here. 
 remove/add more loops if theres less/more people
when editing pay attention to indexes given ie for _1 in..., _2cols = ... cols != _1, 
where _1 is a letter index and _2 is the next letter index """

for i in columns:
    
    jcols = list (filter (lambda cols: cols != i, columns))
    for j in jcols:
        
        kcols = list (filter (lambda cols: cols != j, jcols))
        for k in kcols:
            
            lcols = list (filter (lambda cols: cols != k, kcols))
            for l in lcols:
               
               
                mcols = list (filter (lambda cols: cols != l, lcols))
                for m in mcols:
                    
                    ncols = list (filter (lambda cols: cols != m, mcols))
                    for n in ncols:
                        
                        
                        ocols = list (filter (lambda cols: cols != n, ncols))
                        for o in ocols:
                            
                            pcols = list (filter (lambda cols: cols != o, ocols))
                            for p in pcols:
                                
               
                                qcols = list (filter (lambda cols: cols != p, pcols))
                                for q in qcols:
                                    
                                    rcols = list (filter (lambda cols: cols != q, qcols))
                                    for r in rcols:
                                        
                                        """edit pathTot for more/less people"""
                                        pathTot = mat[0][i] + mat[1][j] + mat[2][k] + mat[3][l] + mat[4][m] + mat[5][n]+ mat[6][o] + mat[7][p] +mat[8][q] + mat[9][r] 
                                        
                                        if pathTot < minTot:
                                            minTot = pathTot
                                            
                                            """edit this for more\less people"""
                                            roomsOrder = [[i,j,k,l,m,n,o,p,q,r]]
                                            
                                            print(minTot)
                                        elif pathTot == minTot:
                                            
                                            """edit this fore more\less people"""
                                            roomsOrder.append ([i,j,k,l,m,n,o,p,q,r])
print("the possible arrangements are \n" )
print (roomsOrder, "\n" )
print ("there are ", len(roomsOrder), "best arrangements of the rooms")
randomBestPath = roomsOrder[random.randint(0, len(roomsOrder)-1)]
print("the random arrangement chosen is", randomBestPath)
rooms = randomBestPath  



for person in range(10):
    print (people[person], " gets room ", rooms[person] +1 )
    
# rooms[person] +1 is the room
# rooms[person] is the index column of the room
#rooms is the list of indexes of rooms for each row
"""
matrix has rooms as columns
people as rows
and entries as preferences 

sums preferences [0] [i] + [1][j] etc 

eg [o] [1] is person one assigned room 2  (preference value)

"""

