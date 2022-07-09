#!/usr/bin/env python
# coding: utf-8

# In[ ]:


l = [[1, 2], [3, 4], [5, 6, 7]]
a = l[::-1]

for i in range(len(a1)):
    a[i]=a[i][::-1]
    
print(a)


# In[20]:


a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l = []


def flat(n):
    for i in n:
        if isinstance(i, list):
            flat(i)
        else:
            l.append(i)
    return l

flat(a)


# In[ ]:




