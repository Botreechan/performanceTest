import csv 
import matplotlib.pyplot as plt
import numpy as np

# from readCsv import *



fig = plt.figure(dpi=128, figsize=(10, 6))  
ax1 = fig.add_subplot(111) 

ax1.set_title('memory')

plt.xlabel('times')  
  
plt.ylabel('memory(M)')  


with open('totalMem.csv', 'r') as f:
    reader = csv.reader(f)
    # print(type(reader))
    t,m=[],[]
    for row in reader:
        mem = float(row[0])
        times = float(row[1])
        t.append(times)
        m.append(mem)


x = t
y = m

print(y)
print(t)
plt.plot(x,y,label='Frist line',color='r')


plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
