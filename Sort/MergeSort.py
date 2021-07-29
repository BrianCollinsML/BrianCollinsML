# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:45:17 2021

@author: Brian
"""

import generators

#modifying arr in place throughout
#thus, merging two subarrays of arr
#first subarray is l...m
#second subarray is m+1...r
def merge(arr, l, m, r):
    
    #lengths of each subarray
    n1 = m - l + 1
    n2 = r - m
    
    #first, copy the contents of arr to temporary arrays
    Larr = []
    Rarr = []
    
    for i in range(l, m+1):
        Larr.append(arr[i])
        
    for i in range(m+1, r+1):
        Rarr.append(arr[i])
        
    #now, place these back into arr[l...r]
    
    #left iterator, right iterator, arr iterator
    Li = 0
    Ri = 0
    Ai = l

    while Li < n1 and Ri < n2:
        if Larr[Li] < Rarr[Ri]:
            arr[Ai] = Larr[Li]
            Li+=1
        else:
            arr[Ai] = Rarr[Ri]
            Ri+=1
        Ai+=1
        
    #copy remaining left elements if any
    while Li < n1:
        arr[Ai] = Larr[Li]
        Li+=1
        Ai+=1
        
    #copy remaining right elements if any
    while Ri < n2:
        arr[Ai] = Rarr[Ri]
        Ri+=1
        Ai+=1

def merge_sort(arr, l , r):
    
    if l < r:
        #find the median
        m = (l + r) // 2
        #sort the left half
        merge_sort(arr, l, m)
        #sort the right half
        merge_sort(arr, m+1, r)
        #merge the two
        merge(arr, l, m, r)