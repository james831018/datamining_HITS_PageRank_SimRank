#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
from numpy import matrix


f = open('./hw3dataset/graph_5.txt', 'r')
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
edge_matrix = np.zeros(shape=(the_max,the_max))
print(edge_matrix)


# In[3]:


#simrank矩陣
for edge in edges:
    split=edge.split(',')
    a=int(split[0])-1
    b=int(split[1])-1
    #print(a,b)
    edge_matrix[a][b]+=1
print(edge_matrix)


# In[4]:


parent_matrix=edge_matrix.T
print(parent_matrix)


# In[5]:


#I矩陣
query_sim = matrix(numpy.identity(the_max))
print(query_sim)


# In[6]:


def get_queries(ad):
    line=parent_matrix[ad]
    #print(ad+1,"的parent：line",line)
    #series = get_queries_num(ad).tolist()[0]
    return [ x for x in range(the_max) if line[x] > 0 ]


    

def ad_simrank(a1, a2, C):#~~~已更新，算出s(a1,a2)
    #print("ad_simrank：",a1+1, a2+1)
    if a1 == a2 : 
        #print("返回1")
        return 1
    #print("parent_matrix\n",parent_matrix)
    #print(parent_matrix[a1-1].sum())
    #print(parent_matrix[a2-1].sum())
    
    if parent_matrix[a1].sum() * parent_matrix[a2].sum()==0:
        prefix=0
    else :
        prefix = C / (parent_matrix[a1].sum() * parent_matrix[a2].sum())

    postfix = 0
    
    #print("prefix",prefix)
    for query_i in get_queries(a1):   #a1的parent
        for query_j in get_queries(a2):   #a2的parent
    #        i = queries.index(query_i)
    #        j = queries.index(query_j)
            #returned=ad_simrank(query_i,query_j,C)
            #print("returned",returned)
            #postfix+=returned
            
            postfix += query_sim[query_i-1,query_j-1]
    #print("最終返回：",prefix,postfix,prefix* postfix)
    return prefix * postfix


def simrank(C=0.8, times=10):
    global query_sim

    for run in range(times):#做幾次
        # queries simrank
        new_query_sim = matrix(numpy.identity(the_max))#創建幾個元素的I矩陣
        #print("new_query_sim",new_query_sim)
        for qi in range(the_max):
            for qj in range(the_max):#對全部的元素
                #print("現在跑：",qi+1,qj+1)
                #i = queries.index(qi)
                #j = queries.index(qj)
                new_query_sim[qi-1,qj-1] = ad_simrank(qi, qj, C)



        query_sim = new_query_sim
        #ad_sim = new_ad_sim


# In[7]:


simrank()


# In[8]:


print(query_sim)


# In[12]:


print(query_sim[0])

