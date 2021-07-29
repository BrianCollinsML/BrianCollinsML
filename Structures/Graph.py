# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:13:16 2021

@author: Brian
"""

from collections import defaultdict
# put, full, get, empty
from queue import Queue
import random
  
# function for adding edge to graph
# using adjacency list here
# from https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/

class Graph(object):
    
    def __init__(self):
        self.adj_list = defaultdict(list)


    def addEdge(self,u,v):
        self.adj_list[u].append(v)
  
    # for printing
    def get_edges(self):
        edges = []
      
        # for each node in graph
        for node in self.adj_list:
              
            # for each neighbour node of a single node
            for neighbour in self.adj_list[node]:
                  
                # if edge exists then append
                edges.append((node, neighbour))
                
        return edges

    # one directional graph
    def generate_random_graph(self, num_nodes, max_edges):
        
        # n is the node we are adding edges to
        for n in range(num_nodes):
            likelihood = 0.8
            nope_set = set()
            nope_set.add(n)
            # each edge will be half as likely as the previous, starting at 80%
            for e in range(max_edges):
                
                #roll the die to add an edge
                if random.random() > likelihood:
                    #rolled too high
                    break
                likelihood = likelihood / 2
                #pick random nodes until we find one that isn't n or the previous connection
                connect = n
                while connect in nope_set:
                    connect = random.randint(0, num_nodes-1)
                #add an edge between n & connect
                self.addEdge(n, connect)
                nope_set.add(connect)
        
    # s = start
    # e = end
    # return True if there is a route, False if not
    def is_route(self, s, e):
        
        q = Queue()
        visited = set()
        visited.add(s)
        q.put(s)
        
        while not q.empty():
            node = q.get()
            #visited.add(node)
            #stop if we're here
            if node == e:
                return True
            for neighbor in self.adj_list[node]:
                if not neighbor in visited:
                    q.put(neighbor)
                    visited.add(neighbor)
                
        #if we exhausted the BFS, there is no route
        return False
            
        
'''
g = Graph()
g.generate_random_graph(10, 2)
print(g.get_edges())
print(g.is_route(0, 9))
'''