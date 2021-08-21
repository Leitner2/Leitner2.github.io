# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:38:08 2019

@author: yonle
"""
import numpy as np
import pandas as pd

class Heap(object):# הגזרת מחלקת ערימה
    def __init__(self):
        self.__array = []#רשימה ריקה לניהול המידע
        self.__last_index = -1#אינדקס אחרון

    def push(self, value): #מכניסים איבר לסוף הרשימה , יעלה במידה ולא עונה על הגדרות הערימה
        
        self.__array.append(value)
        self.__last_index += 1
        self.__siftup(self.__last_index)

    def pop(self):#מוציא את השורש , ומעביר את האיבר הרלוונטי לראשית הערימה
       
        if self.__last_index == -1:
            raise IndexError("Can't pop from empty heap")
        root_value = self.__array[0]
        if self.__last_index > 0:  # more than one element in the heap
            self.__array[0] = self.__array[self.__last_index]
            self.__siftdown(0)
        self.__last_index -= 1
        return root_value

    def peek(self):#הסתכלות בלבד על האיבר העליון
        
        if not self.__array:
            return None
        return self.__array[0]

    def replace(self, new_value):#החלפת השורש באיבר אחר לבחירתנו כל עוד הוא תואם את חוקי הרשימה
        if self.__last_index == -1:
            raise IndexError("Can't pop from empty heap")
        root_value = self.__array[0]
        self.__array[0] = new_value
        self.__siftdown(0)
        return root_value

    def heapify(self, input_list):#פונקצית היפיפיי שמסדרת את הרשימה שלנו עפ"י ערכי הפרמטרים וסוג הרשימה
      
        n = len(input_list)
        self.__array = input_list
        self.__last_index = n-1
        for index in reversed(range(n//2)):
            self.__siftdown(index)

    @classmethod
    def createHeap(cls, input_list):#יוצר ערימה ע"ב רשימה שנכניס , פונקצית רשות
        """
            create an heap based on an inputted list.
        """
        heap = cls()
        heap.heapify(input_list)
        return heap

    def __siftdown(self, index):#מוריד את הערכים הרלוונטים במידה וצריך
        current_value = self.__array[index]
        left_child_index, left_child_value = self.__get_left_child(index)
        right_child_index, right_child_value = self.__get_right_child(index)
       
        best_child_index, best_child_value = (right_child_index, right_child_value) if right_child_index\
        is not None and self.comparer(right_child_value, left_child_value) else (left_child_index, left_child_value)
        if best_child_index is not None and self.comparer(best_child_value, current_value):
            self.__array[index], self.__array[best_child_index] =\
                best_child_value, current_value
            self.__siftdown(best_child_index)
        return


    def __siftup(self, index):#מעלה את הערכים הרלוונטים במידה וצריך
        current_value = self.__array[index]
        parent_index, parent_value = self.__get_parent(index)
        if index > 0 and self.comparer(current_value, parent_value):
            self.__array[parent_index], self.__array[index] =\
                current_value, parent_value
            self.__siftup(parent_index)
        return

    def comparer(self, value1, value2):
        raise NotImplementedError("Should not use the baseclass heap\
            instead use the class MinHeap or MaxHeap.")

    def __get_parent(self, index):#החזרת הורה עפ"י אינדקס
        if index == 0:
            return None, None
        parent_index =  (index - 1) // 2
        return parent_index, self.__array[parent_index]

    def __get_left_child(self, index):#החזרת עלה שמאל לפי אינדקס
        left_child_index = 2 * index + 1
        if left_child_index > self.__last_index:
            return None, None
        return left_child_index, self.__array[left_child_index]

    def __get_right_child(self, index):#החזרת עלה ימין עפ"י הערך
        right_child_index = 2 * index + 2
        if right_child_index > self.__last_index:
            return None, None
        return right_child_index, self.__array[right_child_index]

    def __repr__(self):#רפר
        return str(self.__array[:self.__last_index+1])

    def __eq__(self, other):
        if isinstance(other, Heap):
            return self.__array == other.__array
        if isinstance(other, list):
            return self.__array == other
        return NotImplemented

class MinHeap(Heap):#הגזרת ערימת מינימום
    def comparer(self, value1, value2):
        return value1 < value2

class MaxHeap(Heap):#הגזרת ערימת מקסימום
    def comparer(self, value1, value2):
        return value1 > value2
    
    

temp=MinHeap()
temp.push(2)
temp.push(3)
temp.push(4)
temp.push(1)
temp.push(8)
print(temp)

###Part B###
class City(): # הגדרת מחלקת עיר המוגדרת ממזהה עיר ומרחק נתון
    def __init__(self, id, destenation):
        self.id = id
        self.destenation = destenation
    def get_id(self):
        return int(self.id)
    def get_destenation(self):
        return int(self.destenation)
    def __repr__(self):
        return str("id : " + str(self.id))


def TravelSmart(A , CityId):#פונקצית בדיקת המרחק
    num_of_cities = len(A)#מספר הערים הכולל
    original_city = CityId#משתנה עיר מקורית לטובת חישוב מרחק החזרה
    destenation = 0#קאונטר מרחק כולל
    temp=[]
    city_heap=MinHeap()#ערימת מינימום
    visited_cities=[]#רשימת ערים שביקרנו בהם
    while num_of_cities!=0:      
      for i in range(len(A)):#מעבר על שורה במטריצה
         if i not in visited_cities:  # תנאי שלא נכניס ערים שהיינו בהם
            city_heap.push(A[CityId][i].get_destenation())#הכנסת המרחק לערימת מינימום
            temp.append(A[CityId][i])#הכנסת העיר שבה ביקרנו
            temp.sort(key = lambda City : City.get_destenation())#סידור הערים ברשימה זמנית לפי מרחקם
      if num_of_cities == 1:#במידה ונשאר עיר אחרונה ואנחנו צריכים לחזור
          destenation+=A[CityId][original_city].get_destenation()#מרחק בין העיר האחרונה לזאת שיצאנט ממנה
          visited_cities.append(CityId)
      else: 
           city_heap.pop()#הסרת האיבר הראשון שלא רלוונטי
           destenation+=city_heap.pop() # לסכום את המרחק
           visited_cities.append(CityId)#הכנסת העיר לרשימה
           CityId=temp[1].get_id()    # החלפת העיר המזהה כך שנבנה על בסיסה ערימה חדשה
      num_of_cities-=1#עיר פחות
      city_heap=MinHeap()#הגדרת ערימה חדשה
      temp=[]
    return "the visited cities our : "  + str(visited_cities) + " and the total distance is "  + str(destenation)

      
    
    

###optional part###

###optional part###
    
#def TSP(A, start_city_id):
    
#	pass
	
 #   return visited_cities, destenation
A = np.array([[City(0,0),City(1,8),City(2,6)],
              [City(0,4),City(1,0),City(2,22)],
              [City(0,18),City(1,21),City(2,0)]])


print(TravelSmart(A , 1))
