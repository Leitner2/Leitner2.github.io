# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:55:23 2019

@author: yonle
"""

### Exercise 3 - q1: Dynamic Programming ###

### Template ###

#import libraries:

#a. main function

def knapsack_bottom_up(items, maximum_weight):
    list_of_items=[]
    l=len(items)
    if l == 0 or maximum_weight == 0 : 
        return 0
  
    if (items[l-1][0] > maximum_weight): 
        return knapsack_bottom_up(items[0:l-1], maximum_weight)
  
    
    else: 
        a= max(items[l-1][1] + knapsack_bottom_up(items[0:l-1] , maximum_weight-items[l-1][0]),knapsack_bottom_up(items[0:l-1], maximum_weight))
        return a

            
    

items=[(3,7), (1,2) ,(4,5) ,(2,4)]
maximum_weight = 6
print(knapsack_bottom_up(items, maximum_weight))






#b. subset-sum function (remember 3 code line is 3 points extra!)

#def subset_sum_algo(numbers, subset_sum):
    