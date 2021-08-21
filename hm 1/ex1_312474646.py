''' Exercise #1. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
n = 5 # Replace ??? with a positive int of your choice.
d = 2.0 # Replace ??? with a float of your choice.
# Write the rest of the code for question 1 below here.

a = 1.0
s = n*(2*a + (n-1)*d)/2
print "the sum of the series is", s



#########################################
# Question 2 - do not delete this comment
#########################################
x = 8.25 # Replace ??? with a float of your choice.
# Write the rest of the code for question 2 below here.
if x-2 == 0: print "division by zero!"
if x-2 < 0: print "imaginary number!"

if x-2 > 0:
    a = 1/((x-2)**0.5)
    print 'num is' , a



#########################################
# Question 3 - do not delete this comment
#########################################
x = 150 # Replace ??? with a int of your choice.
# Write the rest of the code for question 3 below here.
if x%6==0:
    print "divisible by 6"
if x%3==0: 
 if x%2!=0:  print "disible by 3"
a = len(str(x))
if a%2==0:   print "even number of digit"
  
   
    

#########################################
# Question 4 - do not delete this comment
#########################################
my_string = 'abba' # Replace ??? with a string of your choice.
# Write the rest of the code for question 4 below here.
print my_string==my_string[::-1]



   
#########################################
# Question 5 - do not delete this comment
#########################################
my_string = 'asdfghjkw' # Replace ??? with a string of your choice.
# Write the rest of the code for question 5 below here.
a = len(my_string)
if a>10:
   print str.upper(my_string[0:a:2])
if a<=10:
    b=my_string * 10
    print b[:10]

    
    
    
    

#########################################
# Question 6 - do not delete this comment
#########################################
password = '12#pAss#gF123' # Replace ??? with a string of your choice.
# Write the rest of the code for question 6 below here.
b=str.lower(password)
print password[b.find('#pass#')+6:]

