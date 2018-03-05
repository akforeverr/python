import math
l = input('enter the lenth: ')
b = input('enter the breath: ')
h = input('enter the height: ')
p=(l+b+h)/2
area = math.sqrt(p*(p-l)*(p-b)*(p-h))
print "the area of your triangle is ",area 
