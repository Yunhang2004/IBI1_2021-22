import matplotlib.pyplot as plt

#Create a dictionary to record the data
effect={'30':1.03,'35':1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,'60':1.42,'65':1.55,'70':1.72,'75':1.94}
print(effect)

#Create a scatter plot to describe the data
x_values=list(effect.keys())
y_values=list(effect.values())
plt.scatter(x_values,y_values,s=50)
plt.title('Paternal Age vs Offspring Health')
plt.xlabel('Paternal Age')
plt.ylabel('Relative Risk for CHD')
plt.show()


