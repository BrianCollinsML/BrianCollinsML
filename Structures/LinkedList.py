# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:45:17 2021

@author: Brian
"""

import random
import string

# Taken from https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python
# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):  
        self.head = None
  
    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
              current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    # add random digits to head
    def generate_rand_num(self, length, lower, upper):
        count = 0
        if not self.head:
            self.head = Node(data=random.randint(lower, upper))
            length -= 1
        current = self.head
        while count < length:
            n = Node(data=random.randint(lower, upper))
            current.next = n
            current = n
            count += 1

    # add random letters to head
    def generate_rand_str(self, length):
        count = 0
        if not self.head:
            self.head = Node(data=random.choice(string.ascii_letters[:26]))
            length -= 1
        current = self.head
        while count < length:
            n = Node(data=random.choice(string.ascii_letters[:26]))
            current.next = n
            current = n
            count += 1

    def make_linked(self, l):
        self.head = Node()
        self.head.data = l[0]
        runner = self.head

        for i in l[1:]:
            n = Node()
            runner.next = n
            runner = runner.next
            runner.data = i

    # return true if self is a palindrome
    def is_palindrome(self):
        # brute force: construct parallel, reverse linked list, and then loop thru both simultaneously
        # time O(n) storage O(n)

        # idea: loop through first half with fast/slow pointer, push into stack
        # as we loop through 2nd half, compare to the stack
        # since the stack is LIFO, only a palindrome will line up

        stack = deque()
        slow = self.head
        fast = self.head
        stack.append(slow.data)

        # this will work if linked list size is even
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            stack.append(slow.data)

        # we have the stack, and slow is at the proper place
        # first, check if the length is odd
        # if even, fast.next will exist. If not, odd
        if not fast.next:
            stack.pop()

        # loop through 2H list with slow, checking that it equals what's next in the stack
        slow = slow.next
        while slow:
            if slow.data != stack.pop():
                return False
            slow = slow.next

        # if we had it here, stack and the 2H list lined up
        return True

def sum_two_lists(l1, l2):
    
    runner1 = l1.head
    runner2 = l2.head
    
    sum_ll = LinkedList()
    
    carry = 0
    
    sum_ll.head = Node(data=(runner1.data+runner2.data)%10)
    if runner1.data + runner2.data > 10:
        carry = 1
    
    sum_runner = sum_ll.head
    
    runner1 = runner1.next
    runner2 = runner2.next
    
    while runner1:
        n = Node()
        n.data = (runner1.data + runner2.data + carry)%10
        if runner1.data + runner2.data > 10:
            carry = 1
        else:
            carry = 0

        sum_runner.next = n
        sum_runner = sum_runner.next
        
        runner1 = runner1.next
        runner2 = runner2.next
        
    if carry > 0:
        sum_runner.next = Node(data=carry)
        
    return sum_ll

def sum_two_lists_forward(l1, l2):
    
    runner1 = l1.head
    runner2 = l2.head
    
    sum_ll = LinkedList()
    
    sum_ll.head = Node()
    sum_runner = sum_ll.head
    
    data_ = runner1.data + runner2.data
    if data_ > 10:
        sum_runner.data = 1
        n = Node()
        sum_runner.next = n
        sum_runner = sum_runner.next
        sum_runner.data = data_%10
    else:
        sum_runner.data = data_
        n = Node()
        sum_runner.next = n
        sum_runner = sum_runner.next
    
    #at the start of the loop, we are on the currently populated node with sum_runner, 
    #but the other runners are on the next node
    runner1 = runner1.next
    runner2 = runner2.next
        
    while runner1:
        
        n = Node()
        data_ = runner1.data + runner2.data
        n.data = data_%10
        
        if data_ > 10:
            sum_runner.data+=1
            
        sum_runner.next = n
        sum_runner = sum_runner.next
        
        runner1 = runner1.next
        runner2 = runner2.next
        
    return sum_ll



'''
ll = LinkedList()
ll.generate(3, 0, 9)
ll.printLL()

print()

ll2 = LinkedList()
ll2.generate(3, 0, 9)
ll2.printLL()

print()


sum_ = sum_two_lists(ll, ll2)
sum_.printLL()

print()

sum_forward = sum_two_lists_forward(ll, ll2)
sum_forward.printLL()
'''