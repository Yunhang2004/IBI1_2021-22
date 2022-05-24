import re
seq ="ATGCAATCGACTACGATCAATCGAGGGCC"
print(len(re.findall("GAATTC",seq))+1)
