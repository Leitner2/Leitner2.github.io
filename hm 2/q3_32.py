
# ~~~ This is a template for question 3  ~~~

#Imports:
import pandas as pd

#Path for data:
path='data_3.xlsx'
##NOTES IS ENGLISH IS THIS Q! HOPE ITS OK
#Implement HashTable class:
class HashTable:
    def __init__(self, size=int , hash_function_method=str, collision_handling=str,m=int,A=float,m_2=None,A_2=None): #Initiate all the parameter for the hash table.
        if not isinstance(size, (int)):  # check if  size is an int
            raise ValueError('size should be an int')
        if not isinstance((hash_function_method), (str)):  # check if  hash_function_method is an str
            raise ValueError('hash_function_method should be an str')
        if not isinstance((collision_handling), (str)):  # check if  collision_handling is an str
            raise ValueError('collision_handling should be an str')

        if not isinstance(m, (int)):  # check if  m is an int
            raise ValueError('m should be an int')
        if not isinstance(A, (float,int)):  # check if  A is an float
            raise ValueError('A should be an float')

        if m_2 is not None:
            if not isinstance(m_2, (int)):  # check if  m_2 is an int
                raise ValueError('m_2 should be an int')

        if A_2 is not None:
            if not isinstance(A_2, (float, int)):  # check if  A_2 is an float
                raise ValueError('A_2 should be an float')

        self.hash_function_method=hash_function_method
        self.collision_handling=collision_handling
        self.size = size
        self.keys =[[] for _ in range(size)] #Data structure for keys.
        self.data = [[] for _ in range(size)]#Data structure for values.
        self.m=m
        self.A=A
        self.m_2=m_2
        self.A_2=A_2
        self.num_keys=0
        #Check that all the parameters are given for a specific configuration of the hash table:
        if self.hash_function_method=="multiplication" and self.A ==float:
            raise ValueError('Need to define A')
        if self.collision_handling=="OA_Double_Hashing" and self.m_2 ==int:
            raise ValueError('Need to define m_2')
        if self.collision_handling=="OA_Double_Hashing" and self.hash_function_method=="multiplication" and self.A_2 ==float:
            raise ValueError('Need to define A_2')

###Part A###

    def hash_function(self,key):                #Logic of hash function.
        if self.hash_function_method=="mod":
            return key%self.m
        elif self.hash_function_method=="multiplication":
            return int(self.m*(key*self.A-int(key*self.A)))

    def hash_function_2(self,key):              #Logic of hash function, when using OA_Double_Hashing.
        if self.hash_function_method=="mod":
            return (self.m_2-key%self.m_2)
        elif self.hash_function_method=="multiplication":
            return int(self.m_2*(key*self.A_2-int(key*self.A_2)))


    def insert(self,key=int,value=str):
        if not isinstance(key, (int)):  # check if  key is an int
            raise ValueError('key should be an int')
        if not isinstance(value, (str)):  # check if  str is an int
            raise ValueError('value should be an str')

        counter=0                           #We will use the counter later to create our metric of efficiency.
        place= self.hash_function(key)
        if self.keys[place]==[] or self.keys[place]==[-1] :            #If we did not have any collision.
            self.keys[place]=[key]
            self.data[place]=[value]
            counter+=1
            self.num_keys += 1
            return counter
        elif self.keys[place]==[key]:       #Replacing the value.
            self.data[place]=[value]
            counter+=1
            return counter
        #hendeling collisions:
        elif self.collision_handling=="Chain":
            counter+=1
            for i in range(1,len(self.keys[place])):
                counter+=1
                if self.keys[place][i]==key:        #Replacing the value.
                    self.data[place][i]=value
                    self.num_keys += 1
                    return counter                  #Returns the amount of operations.
            self.keys[place].append(key)            #Using 'Chain'.
            self.data[place].append(value)
            self.num_keys += 1
            return counter                          #Returns the amount of operations.

        elif self.collision_handling=="OA_Quadratic_Probing":
            if self.num_keys==self.size:
                return "Hash Table is full"             #In open addressing, we can not have more keys then the size of the data structure.
            counter+=1
            for i in range(1,self.size):
                counter+=1

###Part B###
                new_place=self.hash_function(place+i**2)

                if self.keys[new_place]==[key]:         #Replacing the value.
                    self.data[new_place]=[value]
                    return counter                      #Returns the amount of operations.
                elif self.keys[new_place]==[] or self.keys[new_place]==[-1]:
                    self.keys[new_place]=[key]          #Using 'OA_Quadratic_Probing'.
                    self.data[new_place]=[value]
                    self.num_keys+=1
                    return counter                      #Returns the amount of operations.

        elif self.collision_handling=="OA_Double_Hashing":
            if self.num_keys==self.size:
                return "Hash Table is full"             #In open addressing, we can not have more keys then the size of the data structure.
            counter+=1
            for i in range(1,self.size):
                counter+=1
                new_place=(self.hash_function(key)+i*self.hash_function_2(key))%self.m
                if self.keys[new_place] == [key]:       #Replacing the value.
                    self.data[new_place] = [value]
                    return counter                      #Returns the amount of operations.
                elif self.keys[new_place]==[] or self.keys[new_place]==[-1]:
                    self.keys[new_place]=[key]
                    self.data[new_place]=[value]        #Using 'OA_Double_Hashing'.
                    self.num_keys+=1
                    return counter                      #Returns the amount of operations.

    def delete(self,key=int):
        if not isinstance(key, (int)):  # check if  key is an int
            raise ValueError('key should be an int')

        counter = 0                                     #We will use the counter later to create our metric of efficiency.
        place = self.hash_function(key)
        if self.keys[place] == [key]:
            self.keys[place]==[-1]
            del self.data[place]
            counter += 1                                #If we did not have any collision.
            self.num_keys -= 1                          #Update the number of keys in the hash table.
            return counter                              #Returns the amount of operations.

        elif self.collision_handling == "Chain":
            if self.keys[place] == []:
                counter += 1
                return "Data is not in Hash Table",counter  #Data is not in Hash Table, Returns the amount of operations.
            counter+=1
            for i in range(1,len(self.keys[place])):
                counter += 1
                if self.keys[place][i] == key:
                    del self.keys[i]                   #Go over all keys in a specific place in the hash table.
                    del self.data[place][i]
                    self.num_keys -= 1                 #Update the number of keys in the hash table.
                    return counter                     #Found and deleted, Returns the amount of operations.
            return "Data is not in Hash Table",counter #Data is not in Hash Table, Returns the amount of operations.

        elif self.collision_handling == "OA_Quadratic_Probing":
            counter+=1
            for i in range(1, self.size):
                counter += 1
                new_place = self.hash_function(place + i * i)
                if self.keys[new_place] == []:              #If we have an empty slot, this means that we do not have the key in the table.
                    break
                if self.keys[new_place] == [key]:
                    self.keys[new_place]=-1
                    del self.data[new_place]                #Go over all places the key can be - using OA Quadratic Probing.
                    self.num_keys -= 1                      #Update the number of keys in the hash table.
                    return counter                          #Found and deleted, Returns the amount of operations.
            return "Data is not in Hash Table",counter      #Data is not in Hash Table, Returns the amount of operations.

        elif self.collision_handling == "OA_Double_Hashing":
            counter+=1
            for i in range(1, self.size):
                counter += 1

###Part C###
                new_place = (self.hash_function(key)+i*self.hash_function_2(key))%self.m

                if self.keys[new_place] == []:              #If we have an empty slot, this means that we do not have the key in the table.
                    break
                if self.keys[new_place] == [key]:
                    self.keys[new_place]=-1                #Go over all places the key can be - using OA Double Hashing.
                    del self.data[new_place]
                    self.num_keys -= 1                      #Update the number of keys in the hash table.
                    return counter                          #Found and deleted, Returns the amount of operations.
            return "Data is not in Hash Table"  ,counter    #Data is not in Hash Table, Returns the amount of operations.

    def member(self, key=int):
        if not isinstance(key, (int)):  # check if  key is an int
            raise ValueError('key should be an int')

        counter = 0                                         #We will use the counter later to create our metric of efficiency.
        place = self.hash_function(key)
        if self.keys[place] == [key]:                       #If we did not have any collision.
            counter += 1
            return True, counter                            #Returns True and the amount of operations.

        elif self.collision_handling == "Chain":
            if self.keys[place] == [] or self.keys[place] == [-1] :
                counter += 1
                return False, counter                       #Go over all keys in a specific place in the hash table,
                                                            #if the key is in it return True and the amount of operations,
            counter+=1                                      #elsr False and the amount of operations
            for i in range(1,len(self.keys[place])):
                counter += 1
                if self.keys[place][i] == key:
                    return True,counter
            return False,counter

        elif self.collision_handling == "OA_Quadratic_Probing":
            counter+=1
            for i in range(1, self.size):

                counter += 1                                    #Go over all places the key can be - using OA Quadratic Probing,
                new_place = self.hash_function(place + i * i)   #if the key is in it return True and the amount of operations,
                if self.keys[new_place] == []:                  #If we have an empty slot, this means that we do not have the key in the table.
                    break
                if self.keys[new_place] == [key]:               #else False and the amount of operations.
                    return True,counter
            return False,counter

        elif self.collision_handling == "OA_Double_Hashing":
            counter+=1
            for i in range(1, self.size):                                                          #Go over all places the key can be - using OA Double Hashing,
                counter += 1                                                                       #if the key is in it return True and the amount of operations,
                new_place = (self.hash_function(key) + i * self.hash_function_2(key)) % self.m     #else False and the amount of operations.
                if self.keys[new_place] == []:                                                     #If we have an empty slot, this means that we do not have the key in the table.
                    break
                if self.keys[new_place] == [key]:
                    return True,counter
            return False,counter


###Part D###

Info_lst= [] #the list that will contain all the info from the excel file

try: #this func takes as an input the path to a data file with 3 sheets
    excel_data = pd.ExcelFile(path)
    sheet_names = excel_data.sheet_names
    for i in range(len(sheet_names)):
        Sheet_= excel_data.parse(sheet_names[i])
        keys_ = Sheet_["ID"].tolist()
        values_= Sheet_["Name"].tolist()
        Info_lst.append((keys_,values_))
        if len(keys_)==0: #if the sheet is empty raise ValueError
            raise ValueError ("sheet is empty")
except IOError:
    raise IOError("This file is not valid")

X = Info_lst[0]
Y = Info_lst[1]
Z = Info_lst[2]

#Hash tables for X
HashTable_X_1= HashTable(149 , "mod", 'Chain',149,0,0,0)
HashTable_X_2= HashTable(149 , "mod", "OA_Quadratic_Probing",149,0,0,0)
HashTable_X_3= HashTable(149 , "mod", "OA_Double_Hashing",149,0,97,0)
HashTable_X_4= HashTable(149 , "multiplication", 'Chain',149,0.589,0,0)
HashTable_X_5= HashTable(149 , "multiplication", "OA_Quadratic_Probing",149,0.589,0,0)
HashTable_X_6= HashTable(149 , "multiplication", "OA_Double_Hashing",149,0.589,97,0.405)
HashT_X = [HashTable_X_1, HashTable_X_2, HashTable_X_3, HashTable_X_4, HashTable_X_5, HashTable_X_6]

#Hash tables for Y
HashTable_Y_1= HashTable(149 , "mod", 'Chain',149,0,0,0)
HashTable_Y_2= HashTable(149 , "mod", "OA_Quadratic_Probing",149,0,0,0)
HashTable_Y_3= HashTable(149 , "mod", "OA_Double_Hashing",149,0,97,0)
HashTable_Y_4= HashTable(149 , "multiplication", 'Chain',149,0.589,0,0)
HashTable_Y_5= HashTable(149 , "multiplication", "OA_Quadratic_Probing",149,0.589,0,0)
HashTable_Y_6= HashTable(149 , "multiplication", "OA_Double_Hashing",149,0.589,97,0.405)
HashT_Y = [HashTable_Y_1, HashTable_Y_2, HashTable_Y_3, HashTable_Y_4, HashTable_Y_5, HashTable_Y_6]

#Hash tables for Z
HashTable_Z_1= HashTable(149 , "mod", 'Chain',149,0,0,0)
HashTable_Z_2= HashTable(149 , "mod", "OA_Quadratic_Probing",149,0,0,0)
HashTable_Z_3= HashTable(149 , "mod", "OA_Double_Hashing",149,0,97,0)
HashTable_Z_4= HashTable(149 , "multiplication", 'Chain',149,0.589,0,0)
HashTable_Z_5= HashTable(149 , "multiplication", "OA_Quadratic_Probing",149,0.589,0,0)
HashTable_Z_6= HashTable(149 , "multiplication", "OA_Double_Hashing",149,0.589,97,0.405)
HashT_Z = [HashTable_Z_1, HashTable_Z_2, HashTable_Z_3, HashTable_Z_4, HashTable_Z_5, HashTable_Z_6]

#this information will be use in part E
count_lst = [] # list that will contain the amount of operations to insert X,Y,Z to all Hash tables
X_data_counter= [] # a list that will contain the amount of operations to insert X to all Hash tables
Y_data_counter= [] # a list that will contain the amount of operations to insert Y to all Hash tables
Z_data_counter= [] # a list that will contain the amount of operations to insert Z to all Hash tables


#inset X data to all Hash tables
for Hash in HashT_X:  #starting a for loop to go over all X hash tables
    counting= 0 #counter variable that will sum operations to this hash table
    for j in range(len(X[0])):  #starting a for loop to go over all X data
        count = Hash.insert(key=int(X[0][j]),value=str(X[1][j])) #inset the ID and the Name to the Hash table
        counting += int(count)
    X_data_counter.append(counting)
count_lst.append(X_data_counter)

#inset Y data to all Hash tables
for Hash in HashT_Y:  #starting a for loop to go over all Y hash tables
    counting= 0 #counter variable that will sum operations to this hash table
    for j in range(len(Y[0])): #starting a for loop to go over all Y data
        count = Hash.insert(key=int(Y[0][j]),value=str(Y[1][j])) #inset the ID and the Name to the Hash table
        counting += int(count)
    Y_data_counter.append(counting)
count_lst.append(Y_data_counter)

#inset Z data to all Hash tables
for Hash in HashT_Z:  #starting a for loop to go over all Z hash tables
    counting= 0 #counter variable that will sum operations to this hash table
    for j in range(len(Z[0])): #starting a for loop to go over all Z data
        count = Hash.insert(key=int(Z[0][j]),value=str(Z[1][j])) #inset the ID and the Name to the Hash table
        counting += int(count)
    Z_data_counter.append(counting)
count_lst.append(Z_data_counter)



###Part E###

def print_Efficiency(X,Y,Z,count_lst): #this func using the info from count_lst and printing the Efficiency of each Hash table
    for i in range(6): #starting a for loop to go over all X counters from the insert funcs in part D
        print("Efficiency of Hash Table "+str(i+1)+" X: "+str(count_lst[0][i]/len(X[0]))) #dividing the the amount of operations takes to insert the data to the Hash table by the number of IDs
    print("\n")

    for i in range(6):  #starting a for loop to go over all Y counters from the insert funcs in part D
        print("Efficiency of Hash Table " + str(i+1) + " Y: "+str(count_lst[1][i] / len(Y[0]))) #dividing the the amount of operations takes to insert the data to the Hash table by the number of IDs
    print("\n")

    for i in range(6):  #starting a for loop to go over all Z counters from the insert funcs in part D
        print("Efficiency of Hash Table " + str(i+1) + " Z: "+str(count_lst[2][i] / len(Z[0]))) #dividing the the amount of operations takes to insert the data to the Hash table by the number of IDs
    print("\n")

print_Efficiency(X,Y,Z,count_lst)

###Part F###

def improve_Efficiency_x(X): #this func using the info from the data in part D- X data
    HashTable_X_improve= HashTable(233, "mod", 'Chain',233,0,0,0) #chaning m in hash table X_1 to improve the efficiency from part E
    counting = 0 #counter variable that will sum operations to this hash table
    for j in range(len(X[0])): #set X data to the new Hash table
        count = HashTable_X_improve.insert(key=int(X[0][j]), value=str(X[1][j])) #inset the ID and the Name to the Hash table
        counting += int(count)
    print("Efficiency of Hash Table X, improve = "+str((counting)/len(X[0])))

improve_Efficiency_x(X)

def improve_Z_Efficiency(Z): #this func using the info from the data in part D- Z data
    HashTable_Z_improve=HashTable(149 , "multiplication", 'Chain',149,0.61803398,0,0) #chaning A in hash table Z_4 to improve the efficiency from part E
    counting = 0 #counter variable that will sum operations to this hash table
    for j in range(len(X[0])): #set Z data to the new Hash table
        count = HashTable_Z_improve.insert(key=int(Z[0][j]), value=str(Z[1][j])) #inset the ID and the Name to the Hash table
        counting += int(count)
    print("Efficiency of Hash Table Z, improve = " + str((counting) / len(Z[0])))

improve_Z_Efficiency(Z)