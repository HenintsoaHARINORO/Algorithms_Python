import sys #get size
n =10 #amount of element in the array
data =[]
for i in range(n):
   a = len(data)
   b=sys.getsizeof(data)
   print('Length:{0:3d};Size in bytes:{1:4d}'.format(a,b))
   data.append(n)