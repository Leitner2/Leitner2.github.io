''' Exercise #3. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def is_in_range(lst, a, b):
  # Write the rest of the code for question 1 below here.
 if range(len(lst)) == 0:
      return True
 for i in range(len(lst)+1):
    if lst[i] <= a:
     return False
    if lst[i] >= b:
     return False
 else:
    return True

listchack=[-1,2,3,4]
num1=0
num2=6

print is_in_range(listchack, num1, num2)

	 
#########################################
# Question 2 - do not delete this comment
#########################################
def sentence_to_words(s):
	# Write the rest of the code for question 2 below here.
  temp = s.replace("#"," ")
  temp = temp.replace("$", " ")
  temp = temp.replace(".", " ")
  temp = temp.replace("!", " ")
  temp = temp.replace(",", " ")
  temp = temp.replace("?", " ")
  temp = temp.replace("%", " ")
  temp = temp.lower()
  s= temp.split()

  return s


a='sjdhfDhdsf#dskfDSGjdsf!sdf?dsf'
print sentence_to_words(a)


#########################################
# Question 3 - do not delete this comment
#########################################
def drop_duplicates(lst):
	# Write the rest of the code for question 3a below here.
  new_lst=[]
  for i in range((len(lst))):
     if lst[i] not in new_lst:
         new_lst.append((lst[i]))

  return  new_lst

abd=[1,3,4,5,6,7,3,4,2]
print drop_duplicates(abd)


def drop_duplicates_in_place(lst):
	# Write the rest of the code for question 3b below here.
    new_lst = []
    for i in range((len(lst))):
        if lst[i] not in new_lst:
            new_lst.append((lst[i]))
    lst[:] = new_lst
    #for i in range((len(new_lst))):
        #lst.append(new_lst[i])
    return lst

aer=[1,2,5,1,4,5,1,4]
drop_duplicates_in_place(aer)
print aer


#need to change the list itself 'good code'
#########################################
# Question 4 - do not delete this comment
#########################################

def gdc_pair(num1,num2):
    temp=range(num1)
    a=0
    for i in temp:
        if num1 % (i+1) == 0:
            if ((num2%(i+1))) == 0:
                a = i+1
    return a

def gcd(lst):
	# Write the rest of the code for question 4 below here.
    divider = 1
    i = 1
    for i in range(len(lst)-2):
        c = gdc_pair(lst[i-1],lst[i])
        b = gdc_pair(lst[i],lst[i+1])
        if c > b:
            divider=b
        if b >= c:
                divider=c
        if c == 1:
            return 1
        if b == 1:
            return 1

        else: return  divider

lst = [4,8,64,128]
print gcd(lst)

#########################################
# Question 5 - do not delete this comment
#########################################
def mul_mat_by_scalar(mat, alpha):
	# Write the rest of the code for question 5 below here.
     new_mat = []
     for i in range(len(mat)):
             temple1 = mat[i][0]
             temple2 = mat[i][1]
             temp=[]
             temp.append(temple1 * alpha)
             temp.append(temple2 * alpha)
             new_mat.append(temp)

     return  new_mat

try1 = [[1,2],[3,4],[5,6]]
dupli1 = 4

print mul_mat_by_scalar(try1,dupli1)


#########################################
# Question 6 - do not delete this comment
#########################################
def max_mat_square(mat):
	# Write the rest of the code for question 6 below here.
    maxtop=0
    for i in range(len(mat)-1):
        for n in range(len(mat[i])-1):
            max1 = mat[i][n] + mat[i][n+1] + mat[i+1][n] + mat[i+1][n+1]
            if max1 > maxtop:
                maxtop = max1

    return maxtop

testmat=[[1,2,4],[3,4,7],[5,6,-9]]
print  max_mat_square(testmat)


#########################################
# Question 7 - do not delete this comment
#########################################
def mat_mul(A, B):
    # Write the rest of the code for question 7 below here.
    num3 = 0
    num4 = 0
    summat = []
    temp = []
    for i in range(len(A)):
        for n in range(len(B[0])):
            for d in range(len(B)):
               num3 = A[i][d] * B[d][n]
               num4 = num4 + num3
            temp.append(num4)
            num4 = 0
        summat.append(temp)
        temp=[]



    return summat


try2=[[1,2,0] , [4,3,-1]]
try3=[[5,1],[2,3],[3,4]]

print mat_mul(try3,try2)

