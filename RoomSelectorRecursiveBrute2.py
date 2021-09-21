# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:31:03 2021

@author: milan
"""
import numpy as np
import random

# finds the best paths recursively after generating the permutation matrix indexes

def perms (icols, permList, MinPaths,Min):
    if len(icols) == 1:
        
        permList.append(icols[0])
        PathTot = permTot(permList) 
        
        if PathTot < Min:
            Min = PathTot
            MinPaths = [permList]
        elif PathTot == Min:
            MinPaths.append(permList)
        return  MinPaths, Min
    else:
        
        for i in icols:
            jcols = list (filter (lambda cols: cols != i, icols))
            newList = permList + [i]
            MinPaths,Min = perms(jcols, newList, MinPaths,Min)
            
        return MinPaths,Min

# find ranking total along path selected

def permTot (path):
    Tot = 0
    for i in range(len(path)):
        Tot += Mat[i,path[i]]
    return Tot


#read ranking matrix from file function 

def ReadMat ():
    print("feature to be implemented soon try again")

# input ranking matrix function

def NewMat():
    
    RoomsNum = int( input ("how many rooms are there?"))
    people = []
    Mat = []
    print("please input the room rank list for each person")
    for i in range (RoomsNum):
        people.append( input("name:"))
        print("input your ranking of the rooms from 1 to ", RoomsNum)
        ranks = []
        for j in range (RoomsNum):
            print("room ", j+1)
            ranks.append( int (input( "rank:")))
        Mat.append(ranks)
            
    return  RoomsNum, people, Mat
    

# script 

# constructing the rankings data

matstate = input("write new matrix or read from file?[w/r]") 
if matstate == "w":
    roomsNumber, people,mat1 = NewMat()
    
elif matstate == "r":
    roomsNumber, people,mat1 = ReadMat()

Mat = np.matrix(mat1)
# finding the best paths

print("assigning your rooms")

MinPaths, Min =  perms (range(roomsNumber), [], [],roomsNumber**2)

# outputting all the results and choosing a one of the best paths

print ("there are ", len(MinPaths), " best arrangements of the rooms")
print("They have a mean Ranking of ",Min/roomsNumber )

randomBestPath = MinPaths[random.randint(0, len(MinPaths)-1)]
print("the random arrangement chosen is")


for person in range(roomsNumber):
    print (people[person], " gets room ", randomBestPath[person] +1 )

