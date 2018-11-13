'''
This file reads the input pixel values, trained weights from the excel file
and will do MAC to get activation point of each neuron. The MAC is followed by 
a ReLu fuction or sigmoid function. The trained weights and input pixels are obtained 
from the MATLAB training code.  

There are 401 input neurons along with 1 bias. 26 neurons in the middle layer along with 
1 bias and 10 output neurons. 
'''
import csv
import re
import numpy as np
import pandas as pd
from math import exp

list1_80=[]
list2_80=[]
list4_80=[]

#reading the first layer weights from excel file
with open('Theta1.csv', encoding='utf-8-sig') as file1:
    reader=csv.reader(file1)
    for row in reader:
        list1_80.append(row)
#file1.close()

#reading the output layer weights from excel file
with open('Theta2.csv', encoding='utf-8-sig') as file3:
    reader=csv.reader(file3)
    for row in reader:
        list4_80.append(row)
#file3.close()
       
#reading the inputs
with open('X_value.csv', encoding='utf-8-sig') as file2:
    reader=csv.reader(file2)
    for row in reader:
        list2_80.append(row)
#file2.close()
       
#sigmoid function        
def sigmoid(num_80):
    num_80=float(num_80)
    deno_80=1+exp(-num_80)
    ans_80=1/deno_80
    return ans_80

count=0
for i in list2_80:
    i.insert(0,1)

list3_80=[]

#relu function
def reLu(num_80):
    if num_80<0:
        return 0
    else:
        return num_80    

#MAC for hidden layer
for m in list2_80:
    temp_list_80=[]
    for n in list1_80:
        
        c=[float(a)*float(b) for a,b in zip(n,m)]
        sum=0
        #print(c)
        for i in c:
            sum=sum+i
           # print(sum)
        ans_80=sigmoid(sum)
        
        temp_list_80.append(sum)
        
    #print(temp_list_80)
    temp_list_80.insert(0,1)
    #print(temp_list_80)
    list3_80.append(temp_list_80)

# print(len(list3_80))
# print(len(list3_80[0]))

#MAC for output layer
list5_80=[]
for m in list3_80:
    temp_list_80=[]
    for n in list4_80:
        
        c=[float(a)*float(b) for a,b in zip(n,m)]
        sum=0
        for i in c:
            sum=sum+i
           # print(sum)
        ans_80=sigmoid(sum)
        
        temp_list_80.append(sum)        
    list5_80.append(temp_list_80)

# #print('we ARE HERE ************************')
# with open('reLu.csv', 'w',newline='') as f1:

#     for rows in list5_80:
#         writer = csv.writer(f1)
#         writer.writerow(rows)
#         #print('write completed')
# f1.close()


#print((list5_80[0])) 


final_list_80=[]
for i in list5_80:
    t_list_80=i.copy()
    sorted=False
    while not sorted:
        sorted=True
        for j in range(len(t_list_80)-1):
            if (t_list_80[j]>t_list_80[j+1]):
                sorted=False
                temp=t_list_80[j]
                t_list_80[j]=t_list_80[j+1]
                t_list_80[j+1]=temp
    c=t_list_80[-1]


    for k in range(len(i)):
   
        if i[k]==c:
            final_list_80.append(k)
            break

with open('sigmoid.csv', 'w',newline='') as f1:
    writer = csv.writer(f1)
    writer.writerow(final_list_80)
f1.close()

print(final_list_80)
print(len(final_list_80))
