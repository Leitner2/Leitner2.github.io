# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:38:37 2019

@author: yonle
"""
import pandas as pd

def insertion_sort_implementation(list):
    number_of_basic_operation1=0
    for i in range(1, len(list)):#לולאה כאורך הרשימה
        number_of_basic_operation1+=2
        for j in range(i - 1, -1, -1):#לולאה פנימית המתעדכנת מהלולאה החיצונית. מקיימת סדר מהגדול לקטן
            number_of_basic_operation1+=3#סוכם פעולות בתוך הלולאה עד כה
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]#החלפת משתנים במידה והערך במקום הגי' גדול יותר מהאינדקס העוקב
                number_of_basic_operation1+=9#סוכם פעולות השוואה והחלפת משתנים עד כה
            else:
                number_of_basic_operation1+=2
                break#במידה והתנאי לא מתקיים הלולאה החיצונים עוברת לערך הבא
    number_of_basic_operation1+=2
    sorted_array = list
    return sorted_array , number_of_basic_operation1#מחזיר רשימה ממוינת ואת הקאונטר

a=[2,5,8,1,35,23,643,12,30]
b=[2,5,8,1,35,23,643,12,30,421,1235]
print(insertion_sort_implementation(a))
