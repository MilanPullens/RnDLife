import numpy as np
import pandas as pd
import sys

if (str.isdigit(sys.argv[1])):
 search = int(sys.argv[1])
else:
 search = sys.argv[1]
inxls = "data/"+sys.argv[2]+".xlsx"

excel = pd.read_excel(open(inxls, 'rb')).to_numpy()
col1 = [item[0] for item in excel]
col2 = [item[1] for item in excel]
match = [col2[i] for i in range(len(col1))if col1[i]==search]
offset = 100-(match[0]/0.90)
#print(col1)
#print(col2)
#print(search)
print(match)
print(round(offset,1))

exit()
