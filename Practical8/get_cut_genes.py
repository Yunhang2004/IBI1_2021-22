import re

fi=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
fo=open("cut_genes.fa","w")
seq={}
for line in fi:
    if line.startswith('>'):
        name=re.findall(r"(?<=gene:)\S+",line)[0]
        seq[name]=''
    else:
        seq[name]+=line.replace('\n','').strip()
fi.close()

_str=[]
for key in seq.keys():
    if "GAATTC" in seq[key]:
        _str.append(">{:<10s}\t{}\n{}\n".format(key,len(seq[key]),seq[key]))
fo.writelines(_str)
fo.close()
