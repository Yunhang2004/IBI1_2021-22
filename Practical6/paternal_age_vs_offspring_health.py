import matplotlib.pyplot as plt

#Create a dictionary to record the data
effect={'30':1.03,'35':1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,'60':1.42,'65':1.55,'70':1.72,'75':1.94}
print(effect)

#Create a scatter plot to describe the data
#x axis: paternal age
#y axis: relative risk for CHD
#Give a title, label the x and y axis
x_values=list(effect.keys())
y_values=list(effect.values())
plt.scatter(x_values,y_values,s=50)
plt.title('Paternal Age vs Offspring Health')
plt.xlabel('Paternal Age')
plt.ylabel('Relative Risk for CHD')
plt.show()


paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
for i in paternal_age:
	effect[paternal_age[i]]=chd[i]
input('Paternal age: ')
print(chd[i])
