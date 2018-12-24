#!/usr/bin/env python
# coding: utf-8

# In[11]:


f = open('./hw3dataset/graph_4.txt', 'r')
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
aut_matrix = np.zeros(shape=(the_max,the_max))
print(aut_matrix)


# In[3]:


#aut矩陣
for edge in edges:
    split=edge.split(',')
    a=int(split[0])-1
    b=int(split[1])-1
    #print(a,b)
    aut_matrix[a][b]+=1
print(aut_matrix)


# In[4]:


#hub矩陣
hub_matrix=aut_matrix.T
print(hub_matrix)


# In[5]:


#初始aut
aut=np.ones([the_max,1])
print(aut)


# In[6]:


def get_hub(aut_matrix,aut):
    #get hub
    test=np.matmul(aut_matrix,aut)
    #print("after matmul",test)
    squre=0
    for i in test:
        squre+=np.square(i[0])
        #print(np.square(i))
    #print("sqrt_squre",np.sqrt(squre))
    sqrt=np.sqrt(squre)

    for i in range(the_max):
        test[i]=round(float(test[i])/sqrt,2)
        #i=float(i)/sqrt
        #print(i)
    #print(test)
    return test


# In[7]:


def get_aut(hub_matrix,hub):
    #get hub
    test=np.matmul(hub_matrix,hub)
    #print("after matmul",test)
    squre=0
    for i in test:
        squre+=np.square(i[0])
        #print(np.square(i))
    #print("sqrt_squre",np.sqrt(squre))
    sqrt=np.sqrt(squre)

    for i in range(the_max):
        test[i]=round(float(test[i])/sqrt,2)
        #i=float(i)/sqrt
        #print(i)
    #print(test)
    return test


# In[8]:


def get_answer(aut):
    count=0
    while True:
        print("count",count)
        count+=1
        hub=get_hub(aut_matrix,aut)
        aut=get_aut(hub_matrix,hub)
        #print("hub\n",hub)
        #print("aut\n",aut)

        hub2=get_hub(aut_matrix,aut)
        aut2=get_aut(hub_matrix,hub2)
        #print("hub2\n",hub2)
        #print("aut2\n",aut2)
        if (hub==hub2).all() and (aut==aut2).all():
            return aut2,hub2
        if count>=100:
            return aut2,hub2


# In[9]:


aut,hub=get_answer(aut)
print(hub,"\n\n",aut)

