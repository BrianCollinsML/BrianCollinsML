# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:45:17 2021

@author: Brian
"""

import random
import string
import generators

from collections import deque
 
# A single node of a singly linked list
class stack:
    # constructor
    def __init__(self): 
        self.stack = deque()
    
    def pop(self):
        return self.stack.pop()
    
    def push(self, n):
        self.stack.append(n)
        
    def peek(self):
        #print('peeking')
        #print(self.stack)
        tmp = self.stack.pop()
        self.stack.append(tmp)
        #print('end peek')
        return tmp
    
    def isEmpty(self):
        return (len(self.stack) == 0)
    
    def printStack(self, **args):
        print(self.stack, **args)
        
    def min_on_top(self):
        #brute force: put min items in another stack, make sure the smallest items are on the bottom of the temp stack
        #do so by transferring between the two stacks as many times as needed
        
        #the bottom of temp_stack is the current smallest value
        temp_stack = stack()
        
        #min tracks the current smallest value
        cur_min= self.pop()
        
        temp_stack.push(cur_min)
        
        while self.stack:
            print('loop')
            self.printStack()
            temp_stack.printStack()
            item = self.pop()
            if item <= cur_min:
                #it needs to get to the bottom
                #print('evaluating and')
                #temp_stack.printStack()
                while temp_stack.stack and (temp_stack.peek() > item):
                    #move the top of temp_stack to the top of our main stac
                    self.push(temp_stack.pop())
                temp_stack.push(item)
            else:
                #it can go on top of temp_stack
                temp_stack.push(item)
        
        #push temp_stack back onto our stack
        while temp_stack.stack:
            self.push(temp_stack.pop())


# given a set of 3 stacks, we want all disks on the last tower
# stacks is a list of the 3 stacks
# at each step, we assume that 0...k-1 disks are in the proper (ascending) order on stack 3 (the target stack)
# and disks K...n are in their starting positions on stack 1


# we want to move n disks from stack 1 to the target stack
def move_disks(stacks, disks, start_stack, target_stack, buffer_stack):
    if disks == 1:
        stacks[target_stack].push(stacks[start_stack].pop())
        return stacks
    # always, we want to first move disks 1 ... n-1 to the buffer stack,
    stacks = move_disks(stacks, disks - 1, start_stack, buffer_stack, target_stack)
    # move disk n to target stack,
    stacks = move_disks(stacks, 1, start_stack, target_stack, buffer_stack)
    # and then move disks 1 ... n-1 from the buffer stack to the target stack
    stacks = move_disks(stacks, disks - 1, buffer_stack, target_stack, start_stack)

    return stacks

'''
n = 10

stack_list = generators.gen_towers(n)
for i in stack_list:
    i.printStack()

stack_list = move_disks(stack_list, n, 0, 2, 1)
print("\n")

for i in stack_list:
    i.printStack()

s = stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.pop()

s.min_on_top()

s.printStack()
'''