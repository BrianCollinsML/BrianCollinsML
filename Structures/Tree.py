# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:04:48 2021

@author: Brian
"""

# Create a linked list of nodes at each depth

import random
import string
from collections import deque, defaultdict
from queue import Queue

# A Python class that represents an individual node
# in a Binary Tree
# https://www.geeksforgeeks.org/binary-tree-set-1-introduction/
class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

class Tree:
    def __init__(self):
        self.root = TreeNode(0)
    
    #80 chance of nodes at first depth, then half that from there on out
    def gen_random_tree(self, likelihood, divisor):
        
        self.add_nodes(self.root, likelihood, divisor)
        
    def add_nodes(self, tnode, likelihood, divisor):
        if random.random() < likelihood:
            tnode.left = TreeNode(random.randint(1, 100))
            self.add_nodes(tnode.left, likelihood/divisor, divisor)
        if random.random() < likelihood:
            tnode.right = TreeNode(random.randint(1, 100))
            self.add_nodes(tnode.right, likelihood/divisor, divisor)
        
    # return a linked list of nodes at each depth
    # post-order traversal
    def get_lists(self):
        
        depth_lists = []
        
        if not self.root:
            return
        
        #BFS with queue
        #q = Queue()
        #q.put(self.root)
        
        cur = LinkedList()
        parents = LinkedList()
        
        cur.insert(self.root)
        
        while cur.head:
            depth_lists.append(cur)
            parents = cur
            #loop through parents and add their children to cur
            parents_iter = parents.head
            cur = LinkedList()
            while parents_iter:
                if parents_iter.data.left:
                    cur.insert(parents_iter.data.left)
                if parents_iter.data.right:
                    cur.insert(parents_iter.data.right)
                parents_iter = parents_iter.next
        
        return depth_lists
    
    def print_lists(self, depth_lists):
        
        for level in depth_lists:
            i = level.head
            while i:
                print(i.data.val, end = "  ")
                i = i.next
            print("\n")
    
    '''
    def traverse_graph(self, tnode, depth, depth_lists):
        
        #first visit left
        depth_lists = self.traverse_graph(tnode.left, depth+1, depth_lists)
        #then visit right
        depth_lists = self.traverse_graph(tnode.right, depth+1, depth_lists)
        #then visit this node
        #add the node to the proper linkedlist
        depth_lists[depth].insert(tnode.val)
        
        return depth_lists
    '''

'''
#arr = gen_array(10)
t = Tree()

t.gen_random_tree(0.8, 1.5)

#dl_ = t.get_lists()
t.print_lists(t.get_lists())
'''