#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import os


# In[4]:


os.getcwd()


# In[5]:


file_path = "/Users/liusenyuan/Desktop/方正证劵/indicator_data.xlsx"
df = pd.read_excel(file_path)
df


# In[166]:


retList_300 = [0]
for i in range(1, len(df['沪深300'])):
    currentDateValue = df['沪深300'][i]
    lastDateValue = df['沪深300'][i-1]
    retList_300.append((currentDateValue / lastDateValue) - 1)

print(retList_300)


# In[147]:


absolute_value_300 = [1]
retList_300.pop(0)
for i in range(len(retList_300)):
    absolute_value_300.append((retList_300[i] + 1) * absolute_value_300[i])

print(absolute_value_300)


# In[75]:


ARR_300 = (df['沪深300'][3488]/df['沪深300'][0])**(242/3489)-1
#print(ARR_300)


# In[76]:


import math
std_list = [0,0.006136800935498066]
volatility_300 = np.std(std_list,ddof=1)*math.sqrt(242)
#print(volatility_300)


# In[77]:


sharpe_300 = ARR_300/volatility_300
#print(sharpe_300)


# In[73]:


drawdown_300 = [0]
for i in range (1,len(absolute_value_300)):
    drawdown_300.append(absolute_value_300[i-1]/max(absolute_value_300[0:i])-1)
#print(drawdown_300)


# In[78]:


max_drawdown_300 = min(drawdown_300)
#print(max_drawdown_300)


# In[148]:


retList_zz = [0]
for i in range(1, len(df['中债新综合财富指数'])):
    currentDateValue = df['中债新综合财富指数'][i]
    lastDateValue = df['中债新综合财富指数'][i-1]
    retList_zz.append((currentDateValue / lastDateValue) - 1)

print(retList_zz)


# In[142]:


absolute_value_zz = [1]
retList_zz.pop(0)
for i in range(len(retList_zz)):
    absolute_value_zz.append((retList_zz[i] + 1) * absolute_value_zz[i])

print(absolute_value_zz)


# In[60]:


ARR_zz = (df['中债新综合财富指数'][3488]/df['中债新综合财富指数'][0])**(242/3489)-1
#print(ARR_zz)


# In[61]:


std_list2 = [0,0.0005009884302094036]
volatility_zz = np.std(std_list2,ddof=1)*math.sqrt(242)
#print(volatility_zz)


# In[65]:


sharpe_zz = ARR_zz/volatility_zz
#print(sharpe_zz)


# In[86]:


drawdown_zz = [0]
for i in range (1,len(absolute_value_zz)):
    drawdown_zz.append(absolute_value_zz[i-1]/max(absolute_value_zz[0:i])-1)
#print(drawdown_zz)


# In[87]:


max_drawdown_zz = min(drawdown_zz)
#print(max_drawdown_zz)


# In[162]:


retList_au = [0]
for i in range(1, len(df['AU9999'])):
    currentDateValue = df['AU9999'][i]
    lastDateValue = df['AU9999'][i-1]
    retList_au.append((currentDateValue / lastDateValue) - 1)

print(retList_au)


# In[150]:


absolute_value_au = [1]
retList_au.pop(0)
for i in range(len(retList_au)):
    absolute_value_au.append((retList_au[i] + 1) * absolute_value_au[i])

print(absolute_value_au)


# In[90]:


ARR_au = (df['AU9999'][3488]/df['AU9999'][0])**(242/3489)-1
#print(ARR_au)


# In[91]:


std_list3 = [0,0.002316886946448271]
volatility_au = np.std(std_list3,ddof=1)*math.sqrt(242)
#print(volatility_au)


# In[92]:


sharpe_au = ARR_au/volatility_au
#print(sharpe_au)


# In[93]:


drawdown_au = [0]
for i in range (1,len(absolute_value_au)):
    drawdown_au.append(absolute_value_au[i-1]/max(absolute_value_au[0:i])-1)
max_drawdown_au = min(drawdown_au)
#print(max_drawdown_au)


# In[168]:


non_rebalence_absolute = []
for i in range (len(df['沪深300'])):
    non_rebalence_absolute.append(retList_300[i]+retList_zz[i]+retList_au[i]+1)
print(non_rebalence_absolute)


# In[110]:


nr_ARR = non_rebalence_absolute[3488]**(242/3490)-1
print(nr_ARR)


# In[169]:


nr_retList = [0]
for i in range(1, len(df['AU9999'])):
    currentDateValue = non_rebalence_absolute[i]
    lastDateValue = non_rebalence_absolute[i-1]
    nr_retList.append((currentDateValue / lastDateValue) - 1)

print(nr_retList)


# In[131]:


nr_max_dd = []
nr_max_dd = min(non_rebalence_absolute)
#print(nr_max_dd)


# In[132]:


nr_std_list = [0,nr_retList[len(nr_retList)-1]]
nr_volatility = np.std(nr_std_list,ddof=1)*math.sqrt(242)
#print(nr_volatility)


# In[133]:


nr_sharpe = nr_ARR/nr_volatility
#print(nr_sharpe)


# In[170]:


rebalence_absolute = []
for i in range (len(df['沪深300'])):
    rebalence_absolute.append((absolute_value_300[i]+absolute_value_zz[i]+absolute_value_au[i])/3)
print(rebalence_absolute)


# In[171]:


rebalance_ARR = rebalence_absolute[3488]**(242/3490)-1
print(rebalance_ARR)


# In[172]:


r_retList = [0]
for i in range(1, len(df['AU9999'])):
    currentDateValue = rebalence_absolute[i]
    lastDateValue = rebalence_absolute[i-1]
    r_retList.append((currentDateValue / lastDateValue) - 1)

print(r_retList)


# In[174]:


nr_max_dd = []
nr_max_dd = min(rebalence_absolute)
print(nr_max_dd)


# In[175]:


r_std_list = [0,r_retList[len(r_retList)-1]]
r_volatility = np.std(r_std_list,ddof=1)*math.sqrt(242)
print(r_volatility)


# In[178]:


r_sharpe = rebalance_ARR/r_volatility
print(r_sharpe)

