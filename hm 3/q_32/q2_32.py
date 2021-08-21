# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
### Exercise 3 - q2: Graphs ###

### Template ###

#import libraries:
import pandas as pd
import  numpy as np 
#Load  data:
df_edges_raw = pd.read_csv('C:\\Users\\hm3\\edges.csv')#קריאת קבצים
df_name_id = pd.read_csv('C:\\Users\\hm3\\name_id_data.csv')

#Handle data:
def set_id_instead_names(df_name_id, df_edges):
    df_edges_copy = df_edges.copy()
    for char_id in df_name_id['id']:
        char_name = df_name_id.iloc[char_id]['name']
        df_edges_copy.loc[df_edges_copy['Source']==char_name, 'Source'] = char_id
        df_edges_copy.loc[df_edges_copy['Target']==char_name, 'Target'] = char_id
    return df_edges_copy

#please note that this function might take few seconds to finish
df_edges = set_id_instead_names(df_name_id, df_edges_raw)
edges=[tuple(x) for x in df_edges.to_records(index=False)]


#a. create adjacency matrix
#Build function for creating adjacency matrix:
def creat_adjacency_matrix(edges):#יוצר מטריקס
    matrix= np.zeros ((len (df_name_id), len (df_name_id)))#יוצר מטריצת אפסים בגודל המתאים
    for tup in edges:#עובר על כל הטאפלים
        matrix[int(tup[0]), int(tup[1])] = 1
        matrix[int(tup[1]),int(tup[0])] = 1#מכניס 1 למקום המפגש הרלוונטי
    return matrix
    

#Use adjacency matrix function on data:

#b. create adjacency dictionary
#Build function for creating adjacency dict:

def creat_adjacency_dict(edges):#יוצר מילון
   dic= {}
   for tup in edges:#עובר על כל הטאפלים
       if tup[0] in dic:#האם טאפל קיים
           dic[tup[0]].append(tup[1])#מוסיף
       else:
           dic[tup[0]]=[tup[1]]#יוצר ומכניס
       if tup[1] in dic:#כנל
           dic[tup[1]].append(tup[0])
       else:
           dic[tup[1]]=[tup[0]]
   return dic


#Use adjacency dict function on data:


#c. BFS
#Build class Queue:
class Queue:#מימוש תור
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#Build BFS function:    
    
def BFS(edges, v):
    dic_new = creat_adjacency_dict(edges)#ניצור מילון עב פונקציה שנכתבה
    visited = []#מערך ביקור
    visited.append(v)#הכנסת השורש למערך ביקור
    queue = Queue()#אתחול תור
    queue.enqueue(v)  #הכנסת שורש
    while queue.isEmpty()==False:#כל עוד התור לא ריק
        vertex = queue.dequeue()#מוציא ומכניס למשתנה
        for w in dic_new[vertex]:#עובר על השכנים במילון
            if w not in visited:#עובר על השכנים
                visited.append(w)#מכניס
                queue.enqueue(w)#מכניס לתור
    return visited#מחזיר מערך

#Use BFS function on data, start as v=1:
print(BFS(edges,1))

#d. DFS
#Build DFS function:

def Dfs(g,edges=list):
    dic_new = creat_adjacency_dict(edges)#יוצר מילון
    l=len(dic_new)#משתנה אורך
    visited=[]#מערך ביקור
    color=['w'] *l#מגדיר צבע לבן כאורך המילון
    for i in dic_new.keys():#עובר על המפתחות
        if color[i] is 'w':#אם לבן
            dfs_visit(i, color, visited, dic_new)#קריאה לפונקצית עזר

    return visited#מערך ביקורים


def dfs_visit(i, color, visited, dic_new):#מקבל אינדקס , רשימת צבע מערך ומילון
    color[i] = 'g'  #משנה צבע אינדקס לאפור
    visited.append(i)  #מכניס למערך ביקורים
    neigh = dic_new[i]#רשימת שכנים של מי שביקרנו
    for v in neigh:#מעבר על השכנים
        if color[v] is 'w':#אם לבן
            dfs_visit(v, color, visited, dic_new)#קריאה נוספת לפונקציה
    color[i] = 'b'#שינוי לשחור

    return None 

    

#Use DFS function on data:
#print (DFS(edges))

#Bonus Section:
