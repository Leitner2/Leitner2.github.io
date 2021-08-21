# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:57:51 2019

@author: yonle
"""
import numpy as np
import pandas as pd

class Node(object): #בניית מחלקת חוליה , מורכבת מידע אישי ומצביע לחוליה הבאה
    def __init__(self,d,n=None):
        self.data=d
        self.next_node=n
    def get_next(self):
        return self.next_node
    def set_next(self,n): # מספר פונקציות פשוטות לניהול החוליה והגדרת ערכיה
        self.next_node=n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data=d
    

class Stack(object): # הגדרת מחלקת מחסנית
    def __init__(self , t=None):
        self.top = t
    def Empty(self):
        if self.top == None:
            return True
        else:
            return False
    def Top(self): # בדיקת ערך עליון במחסנית
        if (self.Empty()):
            return (str("stack_is_empty"))
        return self.top.get_data()
    
    def Push(self, x):# דחיפת איבר באמתעות הגדרת חוליה חדשה ושינוי המצביע שלה לחוליה העליונה הקודמת
        p = Node(x)
        p.set_next(self.top)
        self.top = p
        
    def Pop(self):# הסרה של האיבר העליון וקידום האיבר הבא לקדמת המחסנית
        if (self.Empty()):
            return (str("stack is empty"))
        else:
            x=self.top.get_data()
            self.top = self.top.get_next()
            return x
        
def MathCheck(x):# פונקצית הבדיקה
    stack_1=Stack()#הגדרת מחסנית 
    count=-1#הגדרת קאונטר להצבעה על האיבר הבעייתי
    for i in x:#מעבר על כל אותיות הקלט
        if i == "[" or i == "{"or i == "(":#תנאי להכנסת איברים למחסנית
            stack_1.Push(i)
    
    for i in x:# מעבר נוסף על האיברים 
        count+=1
        if i == "}" :# השוואת הסוגרים המתאימים לאיבר העליון המחסנית
           if stack_1.Pop() != "{":
                return("problem is mispalce of char '}' at index num " + str(count))#החזרת שגיאה במידת הצורך
               
        if i == "]":
           if stack_1.Pop() != "[":
                 return("problem is mispalce of char ']' at index num " + str(count))
    
        if i == ")" :
           if  stack_1.Pop() !=  "(":
                 return("problem is mispalce of char ')' at index num " + str(count))
    return ("the input is Ok")

            
             
    
try1 = LinkedList()   
try1.add(5)
try1.add(4) 
try1.add(3) 
try1.add(2) 
try2=Stack()
try2.Push(1)
try2.Push(5)
try2.Push(2)
try2.Push('a')
print(MathCheck("{4+8[6-3/(2+4]]}"))