''' Exercise #5. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def sum_nums(file):
    # Write the rest of the code for question 1 below here.
    f = open(file,'r')
    s = f.read()
    count=0
    for char in s.split():
        count = count + int(char)

    return count



print  sum_nums('C:\\Users\\yonle\\hm5\\nums.txt')




#########################################
# Question 2 - do not delete this comment
#########################################

def get_x_freqs(infile, outfile, x):
   # Write the rest of the code for question 2 below here.
   new_dic={}
   f=open(infile , 'r')
   if infile is None:
       raise ValueError("Invalid file name")
   for line in f:
       for char in line.split():
           if not new_dic.has_key(char):
               new_dic[char] = 1
           else:
               new_dic[char] = new_dic[char] + 1

   f.close()
   f = open(outfile , 'w')
   value = new_dic.values()
   value.sort(reverse=True)
   i=0
   while i < x:
    for key in new_dic:
          if new_dic[key] == value[i]:
            f.write(key)
            f.write(" ")
            f.write(str(value[i]))
            f.write("\n")
            i=i+1
            break

   f.close()
   f=open(outfile , 'r')
   return f.read()

print get_x_freqs('C:\\Users\\yonle\\hm5\\the_wheels_on_the_bus.txt' , 'C:\\Users\\yonle\\hm5\\trt.txt' , 3)


#########################################
# Question 3 - do not delete this comment
#########################################
def decode(in_file, out_file):
    # Write the rest of the code for question 4 below here.
    f = open(in_file , 'r')
    t = open(out_file , 'w')
    for line in f:
        for char in line.split():
            for i in char:
                if ord(i)>= 65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122:
                   if ord(i) == 65:
                      t.write(chr(90))
                   if ord(i) == 90:
                      t.write(chr(65))
                   if ord(i) == 97:
                      t.write(chr(122))
                   if ord(i) == 122:
                      t.write(chr(97))
                   else:
                      t.write(chr(ord(i)-1))
                else:
                    t.write(i)
            t.write(" ")
        t.write("\n")
    f.close()
    t.close()
    t=open(out_file , 'r')
    return t.read()

print decode('C:\\Users\\yonle\\hm5\\q4.txt' , 'C:\\Users\\yonle\\hm5\\q4empty.txt')

#########################################
# Question 4 - do not delete this comment
#########################################
def process_contacts(contacts_file):
    # Write the rest of the code for question 5 below here.
    f = open(contacts_file , 'r')
    name_dic = {}
    try:
     for line in f:
        temp = line.strip().split(",")
        if temp[0][0] == '#':
            break
        for i in range(len(temp)):
            if temp[i] == " " or len(temp) != 4:
                raise ValueError('invaild input file')

        if not name_dic.has_key(temp[3].strip('\n')):
            name_dic[temp[3].strip('\n')] = [temp[1]]
        else:
            if temp[1] not in name_dic[temp[3].strip('\n')]:
               name_dic[temp[3].strip('\n')].append(temp[1])
    except IOError:
        print "IOError"
    finally:
        f.close()
    return name_dic

print process_contacts('C:\\Users\\yonle\\hm5\\good.csv')
