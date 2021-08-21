# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
number_of_basic_operation = 0


def quick_sort_implementation(list):
    global number_of_basic_operation#מגדיר משתנה גלובאלי לספירת מספר הפעולות
    number_of_basic_operation = 0
    quick_sort(list , 0 , (len(list)-1))#מפעיל את הפונקציה , מקבלת את הרשימה , 0 כאינדקס התחלה ואורך הרשימה פחות 1
    sorted_array = list
    number_of_basic_operation += 2
    return sorted_array , number_of_basic_operation #מחזיר רשימה ממוינת ואת הקאונטר

def quick_sort(A , l , h):
    global number_of_basic_operation

    if l < h:#במידה והרשימה לא בנויה מאיבר אחד
         q = Partition(A, l, h)#הפעלת פוצקציה שתחזיר חוצץ
         quick_sort(A, l, q-1)#מפעיל את הפונקציה על ערך הרשימה ת חוצץ עליון כחסם לערכי הרשימה הקטנים
         quick_sort(A, q + 1, h)#מסדר את ערכי הרשימה הגדולים
         number_of_basic_operation += 3

def get_pivot(A,l,h):
    global number_of_basic_operation#הגדרת משתנה גלובאלי
    m = int((l+h)/2) #אינדקס של האיבר האמצעי
    pivot = h
    if A[l] < A[m]:#אם המספר באינדקס הראשון קטן מזה של האינדקס האמצעי
        if A[m] < A[h]:#אם המספר באינדקס האמצעי קטן מזה של האינדקס הגדול
            pivot=m#הציר שווה למספר האינדקס האמצעי
            number_of_basic_operation += 2
    else:
        if A[l] < A[h]:
            pivot = l#אחרת , הציר שווה לאינדקס המספר הקטן
            number_of_basic_operation += 2#סוכם פעולות בתנאי
    number_of_basic_operation += 3
    return pivot#מחזיר את הציר. הפונקציה מוצאת ציר מרכזי כערך אופטימאלי לביצוע פעולת החיתוך
    

def Partition(A, l, h):
    global number_of_basic_operation
    pivot=get_pivot(A,l,h)#מפעיל את פונקצית מציעת הציר
    pivot_val=A[pivot]#מגדיר משתנה ערך הרשימה במיקום הציר
    A[pivot] , A[l] = A[l] , A[pivot]#מחליף בין מיקום אינדקס הציר למיקום האינדקס הראשון ולהפך
    border=l#מגדיר משתנה כמספר האינדקס הראשון
    number_of_basic_operation += 5#מוסיף 5 לקאונטר כמספר פעולות הבסיס מחוץ ללולאה
    for i in range(l , h+1):
       if A[i]<pivot_val:
           border+=1
           A[i] , A[border] = A[border] , A[i]#מחליף בין ערכים שקטנים יותר מערך הרשימה במיקום הציר וככה יוצר סדר איברים הקטנים יותר מהציר
           number_of_basic_operation += 2#סוכם פעולות בסיס בלולאה
       number_of_basic_operation += 1#סוכם את פעולת הלולאה
    A[l],A[border]=A[border] , A[l]#החלפת משתנים
    
    return border#מחזיר את האינדקס שהלולאה עצרה בו , מציין את מיקום החציצה


a = [2, 3, 6, 7, 20, 1, 30, 22, 5, 12, 31, 44]
print(quick_sort_implementation(a))
