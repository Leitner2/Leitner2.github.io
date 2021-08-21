# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def quick_sort (list,l,r) : 
    if r <= l:
        return None
    else:
        q=Partition (list,l,r)
        quick_sort(list,l,q)
        quick_sort(list,q+1,r)


def Partition(A , l ,r):
    pivot = A[l]
    i=l-1
    j=r+1
    done = False
    
    while(done==False):
        
        if A[j]<=pivot:
            j=j-1
       
        if A[i]>=pivot:
             i=i+1
        
        if i<j :
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
        else:
            done = True
    return j
            

a=[2,3,6,7,20,1,30,22]
quick_sort(a , 1 , 6)
print(a)
            
    