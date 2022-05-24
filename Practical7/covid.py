import pandas as pd
covid_data=pd.read_csv('full_data.csv')

print(covid_data.iloc[10:20,[0,2]])
location=[False,True,False,False,True,False]
print(covid_data.loc[(covid_data['location']=='Afghanistan'),location])

a=[True,False,True,True,False,False] # date new_cases new_deaths
b=[False,False,True,False,False,False] # new_case
c=[False,False,False,True,False,False] # new_deaths
china_new_data=covid_data.loc[(covid_data['location']=='China'),a]
china_new_cases=covid_data.loc[(covid_data['location']=='China'),b]
china_new_deaths=covid_data.loc[(covid_data['location']=='China'),c]

import numpy as np

print(np.mean(china_new_cases,axis=0))
print(np.mean(china_new_deaths,axis=0))


import matplotlib.pyplot as plt

plt.boxplot(china_new_cases,
	    vert=False,
	    meanline=True,
	    showfliers=True,
		)
plt.title('New Cases in China')
plt.show()


plt.boxplot(china_new_deaths,
	    vert=False,
	    meanline=True,
	    showfliers=True,
		)
plt.title('New Deaths in China')
plt.show()

plt.plot(china_new_data['date'],china_new_data['new_cases'],'yo')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.title('New Cases in China over Time')
plt.show()

#Hypothesis:b(blue),r(red) are colors, while + and o indicate the shape of the dots.(I found this funny hahaha)
plt.plot(china_new_data['date'],china_new_data['new_deaths'],'ro')
plt.xlabel('Date')
plt.ylabel('New Deaths')
plt.title('New Deaths in China over Time')
plt.show()

#question.txt
p=[True,False,True,False,True,False] # date new_cases total_cases
spain=covid_data.loc[(covid_data['location']=='Spain'),p]

plt.plot(spain['date'],spain['new_cases'],'bo')
plt.xlabel('Date')
plt.ylabel('New cases')
plt.title('New Cases in Spain over Time')
plt.show()

plt.plot(spain['date'],spain['total_cases'],'bo')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('Total Cases in Spain over Time')
plt.show()
