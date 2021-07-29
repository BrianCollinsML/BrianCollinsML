# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:45:17 2021

@author: Brian
"""


import generators

def partition(arr, low, high):
    
    # index of smaller element
    small = low-1 
    pivot = arr[high]
    
    for i in range(low, high):
        
        #if current element is less than our pivot, increment where the smaller element is
        if arr[i] <= pivot:
            
            small+=1
            # swap elements
            arr[small], arr[i] = arr[i], arr[small]
            
    #now everything left of partition is smaller than it, and everything to the right is taller
    arr[small+1], arr[high] = arr[high], arr[small+1]
        
    return small+1

# pick a random element and partition the array around that element
def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        
        # pi = partitioning index
        # we know that arr[p] is at the right place
        pi = partition(arr, low, high)
        
        print(arr)
        # separately sort the elements below & above the partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)