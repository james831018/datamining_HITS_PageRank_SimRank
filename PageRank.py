#!/usr/bin/env python
# coding: utf-8

# In[1]:


#讀取資料
f = open('./hw3dataset/graph_3.txt', 'r')
all_lines=f.readlines()
edges=[]
the_max=0
for line in all_lines:
    line=line.strip('\n')
    edges.append(line)
    split=line.split(',')
    a=split[0]
    b=split[1]
    print(a,b)
    if int(a)>the_max:
        the_max=int(a)
    if int(b)>the_max:
        the_max=int(b)
    #print(".."+line+"..")
#print(f.readlines())
print(edges,the_max)


# In[2]:


#初始矩陣
import numpy as np
matrix = np.zeros(shape=(the_max,the_max))
print(matrix)


# In[3]:


#aut矩陣
for edge in edges:
    split=edge.split(',')
    a=int(split[0])-1
    b=int(split[1])-1
    #print(a,b)
    matrix[a][b]+=1
print(matrix)


# In[4]:


#parent矩陣
for i in range(the_max):
    row_total=0
    for j in range(the_max):
        row_total+=matrix[i][j]
    if row_total!=0:
        for j in range(the_max):
            matrix[i][j]=matrix[i][j]/row_total
matrix=matrix.T     
print(matrix)


# In[5]:


matrix=matrix*(1-0.15)+(0.15/the_max)
print(matrix)


# In[6]:


#初始aut
rank=np.ones([the_max,1])
rank=rank/the_max
print(rank)


# In[7]:


def get_rank(matrix,rank,thre):
    count=0
    
    while True:
        count+=1
        print(count)
        iteration1=np.matmul(matrix,rank)
        iteration2=np.matmul(matrix,iteration1)
        
        rank=iteration2
        #for i in range(the_max):
        #    iteration1[i][0]=round(iteration1[i][0],3)
        #    iteration2[i][0]=round(iteration2[i][0],3)

        #print("iteration1\n",iteration1)
        #print("iteration2\n",iteration2)
        is_continue=0
        for i in range(the_max):
            if abs(iteration1[i][0]-iteration2[i][0])>thre:
                is_continue=1
        
        if is_continue==0:
            return iteration2

        if count>=100:
            return iteration2


# In[8]:


a=get_rank(matrix,rank,0.005)
print(a)

