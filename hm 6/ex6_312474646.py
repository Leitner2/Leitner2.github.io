''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def recursive_len(lst):
    # Delete the word 'pass' and write the rest of the code for question 1 below here.
    if len(lst) == 0:
        return 0
    return 1 + recursive_len(lst[1:])

print recursive_len([1,2,3,4,5,9])

	
#########################################
# Question 2 - do not delete this comment
#########################################
def is_palindrome(s):
    # Delete the word 'pass' and write the rest of the code for question 2 below here.
    if len(s) == 1 or len(s) == 0:
        return True
    if s[0] != s[len(s)-1]:
        return False
    s = s.strip(s[0])
    return is_palindrome(s)

print is_palindrome('abccba')

	
#########################################
# Question 3 - do not delete this comment
#########################################
def sum_geometric(a_1, n, q):
    # Delete the word 'pass' and write the rest of the code for question 3 below here.
    if n == 0:
        return 0
    if n == 1:
        return a_1
    return a_1 + sum_geometric(a_1*q , n-1 , q)

print sum_geometric(2,3,4)

#########################################
# Question 4a - do not delete this comment
#########################################
def climb_combinations(n):
    # Delete the word 'pass' and write the rest of the code for question 4a below here.
    if n <= 1:
        return 1
    return climb_combinations(n-1) + climb_combinations(n-2)

print climb_combinations(10)
	
#########################################
# Question 4b - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    # Delete the word 'pass' and write the rest of the code for question 4b below here.
    if n <= 1:
        return 1
    if memo==None:
        memo={}
    if n not in memo:
        memo[n] = climb_combinations_memo(n-1, memo) + climb_combinations_memo(n-2, memo)
    return memo[n]

print climb_combinations_memo(100)

#########################################
# Question 5 - do not delete this comment
#########################################
def get_first_index(s, c):
    # Delete the word 'pass' and write the rest of the code for question 5 below here.
    if len(s) == 1 and s!= c:
        return -(len(s)+1)
    if s is '':
        return -1
    else:
     if s[0] == c:
        return 0
     count = 1 + get_first_index(s[1:],c)
     if count > 0:
        return count
     else:
        return count - (count+1)

print get_first_index('asfads' , 'd')


#########################################
# Question 6 - do not delete this comment
#########################################
def calc_max_baggage (weights, W):
    # Delete the word 'pass' and write the rest of the code for question 6 below here.
    if len(weights) == 0 or W<=0:
        return 0
    if len(weights) == 1 and weights[0]<W:
        return 1
    weights.sort()
    if sum(weights) > W:
        return calc_max_baggage(weights[:-1] , W)
    else:
        return len(weights)


print calc_max_baggage([1,2,3,4,5,1] , 13)




