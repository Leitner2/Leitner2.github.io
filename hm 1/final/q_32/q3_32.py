# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:39:16 2019

@author: yonle
"""

#imports
from q1_32 import quick_sort_implementation
from q2_32 import insertion_sort_implementation
import pandas as pd




#load data:
sheet1 = pd.read_excel('C:/Users/yonle/hm5/data_1.xlsx',sheetname='data_1_1')#קורא את ה קובץ אקסל החלוקה לגיליונות
sheet2 = pd.read_excel('C:/Users/yonle/hm5/data_1.xlsx',sheetname='data_1_2')
sheet3 = pd.read_excel('C:/Users/yonle/hm5/data_1.xlsx',sheetname='data_1_3')
sheet4 = pd.read_excel('C:/Users/yonle/hm5/data_1.xlsx',sheetname='data_1_4')
sheet5 = pd.read_excel('C:/Users/yonle/hm5/data_1.xlsx',sheetname='data_1_5')
#sort data and save results:
list1=[]#בונה רשימות ריקות
list2=[]
list3=[]
list4=[]
list5=[]

for line1 in sheet1['sort_me_1']:#מכניס לרשימות את הערכים בגליונות בחיתוך לפי שם תחילת העמודה
    list1.append(line1)

for line2 in sheet2['sort_me_2']:
    list2.append(line2)

for line3 in sheet3['sort_me_3']:
    list3.append(line3)

for line4 in sheet4['sort_me_4']:
    list4.append(line4)

for line5 in sheet5['sort_me_5']:
    list5.append(line5)

listA1=list1[::]#בונה רשימות מועתקות לטובת הפעלת הפונקיות 
listA2=list2[::]
listA3=list3[::]
listA4=list4[::]
listA5=list5[::]

##quick sort:
in_sheet1 , in_counter1 = quick_sort_implementation(list1)#מגדיר משתנים , אחד לקבל הרשימה המסודרת ואחד לקאונטר
in_sheet2 , in_counter2 = quick_sort_implementation(list2)
in_sheet3 , in_counter3 = quick_sort_implementation(list3)
in_sheet4 , in_counter4 = quick_sort_implementation(list4)
in_sheet5 , in_counter5 = quick_sort_implementation(list5)


##insertion_sort:
me_sheet1 , me_counter1 = insertion_sort_implementation(listA1)
me_sheet2 , me_counter2 = insertion_sort_implementation(listA2)
me_sheet3 , me_counter3 = insertion_sort_implementation(listA3)
me_sheet4 , me_counter4 = insertion_sort_implementation(listA4)
me_sheet5 , me_counter5 = insertion_sort_implementation(listA5)
#plot figure:
print("num 1 quick :" + str(in_counter1) + " insertion: "+ str(me_counter1))#מציג את הנתונים
print("num 2 quick :" + str(in_counter2) + " insertion: "+ str(me_counter2))
print("num 3 quick :" + str(in_counter3) + " insertion: "+ str(me_counter3))
print("num 4 quick :" + str(in_counter4) + " insertion: "+ str(me_counter4))
print("num 5 quick :" + str(in_counter5) + " insertion: "+ str(me_counter5))