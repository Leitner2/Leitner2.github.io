''' Exercise #2. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
D = 5  # Replace the assignment with a postive integer to test your code.

# Write the rest of the code for question 1 below here.

A = []
c = 1
while c <= D:
    A.append(c**2)
    c = c+1
print A


# End of code for question 1
#### do not delete the next line ###
#assert isinstance(A, list)


#########################################
# Question 2 - do not delete this comment
#########################################

b = 4  # Replace the assignment with a postive integer to test your code.

# Write the rest of the code for question 2 below here.

B = [1, 2, 3, 4, 7] # Replace the assignment with other lists to test your code.
i = 1
while i < len(B):
    if B[i]%b == 0 :
        print i
        break
    else:
        i=i+1

if i == len(B):
    print -1


# End of code for question 2



#########################################
# Question 3 - do not delete this comment
#########################################

C = [0,1,2,3,4,5] # Replace the assignment with other lists to test your code.


# Write the rest of the code for question 3 below here.
if len(C) ==0:
    print 0
if len(C)==1:
    print C
d = 1
B = []
if len(C) > 1:
 while d < len(C):
    B.append(C[d-1]*C[d])
    d=d+1
 print sum(B)




# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

N = 17  # Replace the assignment with a postive integer > 1, to test your code.

# Write the rest of the code for question 4 below here.
if N==1:
    print 'no'
i=2
while i<N:
    if N%i== 0:
        print 'no'
        break
    else:
        i=i+1
if i==N:
    print 'yes'
# no need for that line under
#if N==1 :
    #print 'yes'



# End of code for question 4


#########################################
# Question 5 - do not delete this comment
#########################################

E = [2, 10, 17, 20, 21] # Replace the assignment with other strings to test your code.
# Write the rest of the code for question 5 below here.
i = 0
while i < (len(E)-2):
    current_num = abs(E[i]-E[i+1])
    ne_num = abs(E[i+1]-E[i+2])
    if ne_num >= current_num:
        print 'no'
        break
    i = i + 1
if i+2 == len(E):
    print 'yes'






# End of code for question 5


#########################################
# Question 6 - do not delete this comment
#########################################

str_list = ["The RED ball", "A RED ball", "A red ball", "FRED", "AAA RED"] # Replace the assignment with other lists to test your code.

str_list_RED = []
# Write the rest of the code for question 6 below here.
for i in range(len(str_list)):
    if "RED" in str_list[i-1]:
        temp = str_list[i-1].split(" ")
        a = 0
        for a in range(len(temp)):
          if temp[a] == "RED":
              str_list_RED.append(str_list[i-1])

str_list_RED.sort()
str_list_RED.reverse()

print str_list_RED




# End of code for question 6
#### do not delete the next line ###
#assert isinstance(str_list_RED, list)