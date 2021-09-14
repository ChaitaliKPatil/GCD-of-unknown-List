#finding out GCD of unknown list elements using NumPy Array
import timeit as tit
import numpy as np
num=int(input("Count the numbers for which GCD is to be calculated: "))
arr_2=np.array([])
for _ in range(int(num)):
    mem=int(input("Enter the nos: \t"))
    arr_2=np.append(arr_2,mem)
#print(arr_2)
arr_2.sort()
#print(arr_2)
min1=int(np.amin(arr_2))
min1_index=np.where(arr_2==min1)
#print(min1_index)
arr_3=np.array([])
for x1 in range(1,min1+1):
    count=0
    for i in arr_2:
        if int(i)%x1==0:
            #print(x1)
            count=count+1
        #print(count,'\n-------------------\n')
        if count==num:
            arr_3=np.append(arr_3,x1)
            #print(arr_3,'@@@@')
print('G.C.D for above',num,'numbers is: ',arr_3[-1])
