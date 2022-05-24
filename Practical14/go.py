#from xml.dom.minidom import parse
#import xml.dom.minidom
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
tree = ET.parse("go_obo.xml")
root = tree.getroot()
nodes = root.findall("term")
print("The totle number of terms:",len(nodes))

ids = [i.text for i in root.findall("term/id")] 
defstrs = [i.text for i in root.findall("term/def/defstr")] 
ls = []
for node in nodes:
    a = []
    is_as = node.findall("is_a")
    for is_a in is_as: 
        a.append(is_a.text)
    ls.append(a)        
#print(ls) # child nodes 
#print(ids)
#print(defstrs) # defstrs 

ids_t = []
ls_t = []
for i in range(len(defstrs)):
    if "translation" in defstrs[i]:
        ids_t.append(ids[i])
        ls_t.append(ls[i])
#        print(ids_t) # id trans
#        print(ls_t) # child node trans
        
d = {}
d_t = {}
d = dict(zip(ids,ls))
d_t = dict(zip(ids_t,ls_t))
#print('1',d) #
#print('2',d_t) # 

def Count(ID,dic):
    if ID not in dic:
        return 0
    elif dic[ID] == []:
        return 0
    else:
        count = len(dic[ID])
        for i in dic[ID]:
            count += Count(i,dic)
        return count

dic = {}
dic_t = {}

for ID in d.keys():
    dic[ID] = Count(ID,d)
#print('3',dic)#

for ID in d_t.keys():
    dic_t[ID] = Count(ID,d_t)
#print('4',dic_t)#

ave = sum(list(dic.values()))/len(list(dic.keys()))
ave_trans = sum(list(dic_t.values()))/len(list(dic_t.keys()))       
print("ave:{:.2f}\nave_trans:{:.2f}".format(ave,ave_trans))

# figure 1
plt.figure()
plt.title("The distribution of child nodes across terms in the Gene Ontology",fontsize = 10)
plt.xlabel("term",fontsize = 14)
plt.ylabel("child node",fontsize = 14)
#x_values = list(range(len(d_trans.keys())))
x_values = list(dic.keys())
y_values = list(dic.values())
plt.scatter(x_values,y_values,s=10)
#plt.savefig("Figure_1.png",dpi=1500,bbox_inches='tight')
#plt.savefig("Figure_1.svg")
#plt.bar(x_values,y_values,color="blue",width=0.5)

# figure 2
plt.figure()
plt.title("The distribution of child nodes across terms associated with 'translation'",fontsize = 10)
plt.xlabel("term",fontsize = 14)
plt.ylabel("child node",fontsize = 14)
x_valuest = list(dic_t.keys())
y_valuest = list(dic_t.values())
plt.scatter(x_valuest,y_valuest,s=20)
# plt.scatter(x_valuest,y_valuest,c=y_valuest,cmap='Blues',edgecolor='none',s=20)
plt.bar(x_valuest,y_valuest,color="blue",width=0.5)
#plt.savefig("Figure_2.png",dpi=1500,bbox_inches='tight')
#plt.savefig("Figure_2.svg")
plt.show()
