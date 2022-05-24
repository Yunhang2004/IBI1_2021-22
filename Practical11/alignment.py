import pandas as pd

blosum=pd.read_excel('BLOSUM-2.xlsx',index_col=0)
seq1=input("Please input sequence1: ")
seq2=input("Please input sequence2: ")
f1=open(seq1,"r")
f2=open(seq2,"r")
flist1=f1.readlines()
flist2=f2.readlines()
f1.close()
f2.close()
seq1_name=flist1[0][1:].replace("\n","")
seq2_name=flist2[0][1:].replace("\n","")
seq1_seq=flist1[1].replace("\n","")
seq2_seq=flist2[1].replace("\n","")

scolist=[]
m=0
for i in range(len(seq1_seq)):
    if seq1_seq[i]==seq2_seq[i]:
        m+=1
    scolist.append(blosum.loc[seq1_seq[i],seq2_seq[i]])
score=sum(scolist)
per=m/len(seq1_seq)
#print(scolist)

print("{}\n{}".format(seq1_name,seq1_seq))
print("{}\n{}".format(seq2_name,seq2_seq))
print("Alignment score:",score)
print("Percentage of identical amino acids:{:.2f}%".format(per*100))

'''
human & mouse:  1490,96.54%
human & random: -351,2.77%
mouse & random: -348,3.11%
From these data, we can infer that evolutionarily closer proteins are encoded by similar genes. Human and mouse DLX5 proteins are evolutionarily close, and their genes are similar. The DLX5 protein is evolutionarily distant to the random protein, and their genes are largely different.

'''


