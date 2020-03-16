#!/usr/bin/env python
# coding: utf-8

# # # Regresinya Sam MetNum

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x = np.array([4, 6, 8, 10, 14, 16, 20, 22, 24, 28])
y = np.array([30, 18, 22, 28, 14, 22, 16, 8, 20, 8])


# In[3]:


print(y)
print(x)


# In[4]:


m, b = np.polyfit(x, y, 1)


# In[10]:


plt.plot(x, y, 'o')
plt.plot(x, m*x + b)


# 

# In[11]:


n = len(y)
xy = x*y
xx = x**2


# In[14]:


b = (n*xy.sum()-x.sum()*y.sum())/(n*xx.sum()-(x.sum())**2)
b


# In[15]:


a = y.mean()-b*x.mean()
a


# In[17]:


print("y = {: .4f}x+{: .4f}".format(b,a))


# In[18]:


yDt = (y-y.mean())**2
yD = (y - a - b*x)**2


# In[20]:


r = np.sqrt((yDt.sum()-yD.sum())/yDt.sum())
r


# In[21]:


R2 = r**2
R2


# In[22]:


yreg = b*x+a
yreg


# In[23]:


ax = plt.plot(x,y,'r+')
plt.plot(x,yreg,'b')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')


# In[ ]:




