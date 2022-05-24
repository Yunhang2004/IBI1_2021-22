marks=[45,36,86,57,53,92,65,45]
L=sorted(marks)
print(L)

#Create a boxplot
import matplotlib.pyplot as plt
import numpy as np
marks=[45,36,86,57,53,92,65,45]
plt.boxplot(marks,
	    vert=False,
	    notch=False,
	    meanline=True,
            showfliers=True,
            boxprops={'color':'green'},
            whiskerprops={'color':'blue'},
            capprops={'color':'blue'},
		)
plt.title('The distribution of IBI1 practical marks')
plt.xlabel('Marks for the eight IBI1 practicals') 
plt.show()

#Calculate the mean
total=0
for i in L:
	total+=i
average=total/8
print(average)

#The average is 59.875, it was less than 60%, so Rob failed this ICA.

