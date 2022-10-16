
import pandas as pd
import numpy as np
import os

os.getcwd()

file_path = "/Users/liusenyuan/Desktop/方正证劵/indicator_data.xlsx"
df = pd.read_excel(file_path)

#沪深300 indicator----------------------------
#收益率
retList_300 = [0]
for i in range(1, len(df['沪深300'])):
    currentDateValue = df['沪深300'][i]
    lastDateValue = df['沪深300'][i-1]
    retList_300.append((currentDateValue / lastDateValue) - 1)

print('沪深300收益率:\n',retList_300)

#净值
absolute_value_300 = [1]
retList_300.pop(0)
for i in range(len(retList_300)):
    absolute_value_300.append((retList_300[i] + 1) * absolute_value_300[i])
print('沪深300净值:\n',absolute_value_300)

#年化收益率
ARR_300 = (df['沪深300'][3488]/df['沪深300'][0])**(242/3489)-1
print('沪深300年化收益率：\n',ARR_300)

#波动率
import math
std_list = [0,0.006136800935498066]
volatility_300 = np.std(std_list,ddof=1)*math.sqrt(242)
print('沪深300波动率:\n',volatility_300)

#sharpe
sharpe_300 = ARR_300/volatility_300
print('沪深300夏普比率：\n',sharpe_300)

#最大回撤
drawdown_300 = [0]
for i in range (1,len(absolute_value_300)):
    drawdown_300.append(absolute_value_300[i-1]/max(absolute_value_300[0:i])-1)
max_drawdown_300 = min(drawdown_300)
print('沪深300最大回撤:',max_drawdown_300)

#中债新综合------------------------------------------
#
retList_zz = [0]
for i in range(1, len(df['中债新综合财富指数'])):
    currentDateValue = df['中债新综合财富指数'][i]
    lastDateValue = df['中债新综合财富指数'][i-1]
    retList_zz.append((currentDateValue / lastDateValue) - 1)
print(retList_zz)

#
absolute_value_zz = [1]
retList_zz.pop(0)
for i in range(len(retList_zz)):
    absolute_value_zz.append((retList_zz[i] + 1) * absolute_value_zz[i])
print(absolute_value_zz)

#
ARR_zz = (df['中债新综合财富指数'][3488]/df['中债新综合财富指数'][0])**(242/3489)-1
print(ARR_zz)

#
std_list2 = [0,0.0005009884302094036]
volatility_zz = np.std(std_list2,ddof=1)*math.sqrt(242)
print(volatility_zz)

#
sharpe_zz = ARR_zz/volatility_zz
print(sharpe_zz)

#
drawdown_zz = [0]
for i in range (1,len(absolute_value_zz)):
    drawdown_zz.append(absolute_value_zz[i-1]/max(absolute_value_zz[0:i])-1)
max_drawdown_zz = min(drawdown_zz)
print(max_drawdown_zz)


#AU9999--------------------------------------------
#
retList_au = [0]
for i in range(1, len(df['AU9999'])):
    currentDateValue = df['AU9999'][i]
    lastDateValue = df['AU9999'][i-1]
    retList_au.append((currentDateValue / lastDateValue) - 1)
print(retList_au)

#
absolute_value_au = [1]
retList_au.pop(0)
for i in range(len(retList_au)):
    absolute_value_au.append((retList_au[i] + 1) * absolute_value_au[i])
print(absolute_value_au)

#
ARR_au = (df['AU9999'][3488]/df['AU9999'][0])**(242/3489)-1
print(ARR_au)

#
std_list3 = [0,0.002316886946448271]
volatility_au = np.std(std_list3,ddof=1)*math.sqrt(242)
print(volatility_au)

#
sharpe_au = ARR_au/volatility_au
print(sharpe_au)

#
drawdown_au = [0]
for i in range (1,len(absolute_value_au)):
    drawdown_au.append(absolute_value_au[i-1]/max(absolute_value_au[0:i])-1)
max_drawdown_au = min(drawdown_au)
print(max_drawdown_au)

#不再平衡
#
non_rebalence_absolute = []
for i in range (len(df['沪深300'])):
    non_rebalence_absolute.append(retList_300[i]+retList_zz[i]+retList_au[i]+1)
print(non_rebalence_absolute)

#
nr_ARR = non_rebalence_absolute[3488]**(242/3490)-1
print(nr_ARR)

#
nr_max_dd = []
nr_max_dd = min(non_rebalence_absolute)
print(nr_max_dd)

#
nr_retList = [0]
for i in range(1, len(df['AU9999'])):
    currentDateValue = non_rebalence_absolute[i]
    lastDateValue = non_rebalence_absolute[i-1]
    nr_retList.append((currentDateValue / lastDateValue) - 1)
print(nr_retList)

#
nr_std_list = [0,nr_retList[len(nr_retList)-1]]
nr_volatility = np.std(nr_std_list,ddof=1)*math.sqrt(242)
print(nr_volatility)

#
nr_sharpe = nr_ARR/nr_volatility
print(nr_sharpe)

#每天再平衡
#
rebalence_absolute = []
for i in range (len(df['沪深300'])):
    rebalence_absolute.append((absolute_value_300[i]+absolute_value_zz[i]+absolute_value_au[i])/3)
print(rebalence_absolute)

#
rebalance_ARR = rebalence_absolute[3488]**(242/3490)-1
print(rebalance_ARR)

#
r_retList = [0]
for i in range(1, len(df['AU9999'])):
    currentDateValue = rebalence_absolute[i]
    lastDateValue = rebalence_absolute[i-1]
    r_retList.append((currentDateValue / lastDateValue) - 1)

print(r_retList)

#
nr_max_dd = []
nr_max_dd = min(rebalence_absolute)
print(nr_max_dd)

#
r_std_list = [0,r_retList[len(r_retList)-1]]
r_volatility = np.std(r_std_list,ddof=1)*math.sqrt(242)
print(r_volatility)

#
r_sharpe = rebalance_ARR/r_volatility
print(r_sharpe)


#月平衡净值

month_r_absolute = []
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].apply(lambda x:x.month)
for i in range (len(df['沪深300'])):
    if (df['Month'][i+1]==df['Month'][i]):
        absolute_value = (retList_300[i]+absolute_value_300[i]+retList_zz[i]+absolute_value_zz[i]+retList_au[i]+absolute_value_au[i])/3
        month_r_absolute.append(absolute_value)
    else:
        balance_value = (month_r_absolute[-1])/3
        absolute_value_300[i] = balance_value
        absolute_value_zz[i] = balance_value
        absolute_value_au[i] = balance_value
        i=i-1

print(month_r_absolute)

#

mr_ARR = month_r_absolute[-1]**(242/3490)-1
print("月平衡年化收益率： ",mr_ARR)

#
mr_retList = [0]
for i in range(1, 3488):
    currentDateValue = month_r_absolute[i]
    lastDateValue = month_r_absolute[i-1]
    mr_retList.append((currentDateValue / lastDateValue) - 1)

print(mr_retList)

#
mr_max_dd = []
mr_max_dd = min(month_r_absolute)
print("月平衡最大回撤： ",mr_max_dd)

mr_std_list = [0,mr_retList[len(mr_retList)-1]]
mr_volatility = np.std(mr_std_list,ddof=1)*math.sqrt(242)
print("月平衡波动率： ",mr_volatility)

mr_sharpe = mr_ARR/mr_volatility
print("月平衡夏普比率：",mr_sharpe)


