# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:40:51 2019

@author: yonle
"""

def knapsack_bottom_up(items, maximum_weight): #מקבל רשימת פריטים ומשקל
       n=len(items) #משתנה אורך
       W=maximum_weight#משתנה משקל
       K = [[0 for x in range(W + 1)] for x in range(n + 1)] #מאתחל מטריצה כגודל הרשימה והמשקל
       for i in range(n + 1): #עובר על העמודות
          for w in range(W + 1): #עובר על הנתונים בעמודה
              if i == 0 or w == 0: #בודק האם מכיל מידע
                K[i][w] = 0#במידה ואין מאתחל כ-0
              elif items[i-1][0] <= w: #אם המשקל קטן מהמשקל שהתקבל כקלט
                K[i][w] = max(items[i-1][1] + K[i-1][w-items[i-1][0]],  K[i-1][w])#מפעיל מקסימום אפשרי למשבצת 
              else: 
                K[i][w] = K[i-1][w] 
  
       res= K[n][W]#הערך המקסימלי במשבת האחרונה
       w=W#משתנה משקל
       res1=res
       list_of_items=[]#רשימת פריטים שניקח
       for i in range(n, 0, -1): #עובר על המטריצה אחורנית
           if res <= 0: #תנאי עצירה
              break
       
           if res == K[i - 1][w]: 
              continue
           else: 
  
              list_of_items.append(items[i - 1][1]) #מכניס לרשימת הפריטים שמזהה שינוי במטריצה
              
            
              res = res - items[i - 1][1] 
              w = w - items[i - 1][0] 
  
       return res1 , list_of_items
    

items=[(3,7), (1,2) ,(4,5) ,(2,4)]
maximum_weight = 6
print(knapsack_bottom_up(items, maximum_weight))

def subset_sum_algo(numbers, subset_sum):
    list_of_tupels=[]#מאתחל רשימת טאפלים
    for i in numbers:
        list_of_tupels.append((i,i))#יטוצר טאפל כפול מכל איבר
    return knapsack_bottom_up(list_of_tupels, subset_sum)[0] == subset_sum#מחזיר נכון או לא תוך שימוש בפונקציה שרשמנו

items1=[1,3,5,7,9,3,2]
print(subset_sum_algo(items1,11))
    
        