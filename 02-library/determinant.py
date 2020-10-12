#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:51:46 2020

@author: stephanieforbes
"""

import numpy as np

def submat(A,i,j):
    """creates and returns 2x2 submatrix of A"""
    
    return [row[:j] + row[j+1:] for row in (A[:i] +A[i+1:])]


def determinant(A,n):
    """returns the determinant of a size n matrix A"""
    
    I = np.eye(n)
    
    if n == 1:
        return A[0][0]
    
    
    for i in range(n):
        for j in range(n):
            if A[i][j] != I[i][j]:
                s = False
            else:
                s = True
    if s == True:
        return 1

            
    
    if n == 2:
        det = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
        
        print(A)
        
        return det
    
    recur = 0
    
    for i in range(n):
        
        recur += pow(-1,i) * A[0][i] * determinant(submat(A,0,i), n-1)
        #recursively calculates the determinant of each 2x2 matrix within the nxn matrix 
        print(recur)
    det = recur
    
    
    return det 