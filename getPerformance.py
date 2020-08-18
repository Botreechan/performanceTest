import os
import re
import time
from multiprocessing import Process
from threading import Thread

from matplotlib import animation
from matplotlib import pyplot as plt

import _thread


def getTotalPss(pname,times,interval):
    i = 0
    while True:    
        if i<times:
            lines = os.popen("adb shell dumpsys meminfo "+pname).readlines() #逐行读取
            for line in lines:
                if re.findall("TOTAL", line): # 找到TOTAL 这一行
                    lis = line.split(" ")  #将这一行，按空格分割成一个list
                    while '' in lis:       # 将list中的空元素删除
                        lis.remove('')
                    if not os.path.exists("totalMem.csv"):
                        os.system(r"touch 'totalMem.csv'")  #检测csv文件是否存在，不在则创建
                    
                    with open("totalMem.csv","at")as f1:
                        f1.write(str(round(int(lis[1])/1024.0,2))+","+str(i)+"\n")  #保留2位小数，并写入本地csv
                    time.sleep(interval)
                    i+=1
        else:
            break
    # return lis[1] #返回总共内存使用


# def getCpu(pname,times,interval):
#     n = 0
#     while True:
#         if n<times:
#             print(n)
#             li = os.popen("adb shell top -m 10 -n 1 -s cpu").readlines()
#             for line in li:
#                 if re.findall(pname,line):
#                     cuplist = line.split(" ")
#                     if cuplist[-1].strip() == pname:
#                         while '' in cuplist:       # 将list中的空元素删除
#                             cuplist.remove('')
#                         if not os.path.exists("totalCpu.csv"):
#                             os.system(r"touch 'totalCpu.csv'")   #检测csv文件是否存在，不在则创建

#                         with open("totalCpu.csv","at")as f1:
#                             f1.write(str(cuplist[4].strip('%'))+","+str(n)+"\n") #保留2位小数，并写入本地csv
#                         time.sleep(interval)
#                         print(n)
#                         n+=1
#                         # return float(cuplist[4].strip('%')) #去掉百分号，返回一个float
#         else:
            # break





# def getCpu(pname,times,interval):

#     li = os.popen("adb shell top -m 10 -n 1 -s cpu").readlines()
#     for line in li:
#         if re.findall(pname,line):
#             cuplist = line.split(" ")
#             if cuplist[-1].strip() == pname:
#                 while '' in cuplist:       # 将list中的空元素删除
#                     cuplist.remove('')
#                 if not os.path.exists("totalCpu.csv"):
#                     os.system(r"touch 'totalCpu.csv'")   #检测csv文件是否存在，不在则创建

#                 with open("totalCpu.csv","at")as f1:
#                     f1.write(str(cuplist[4].strip('%'))+","+str(n)+"\n") #保留2位小数，并写入本地csv
#                 time.sleep(interval)

                # return float(cuplist[4].strip('%')) #去掉百分号，返回一个float



pname = "com.xbcx.gdwx3"

getTotalPss(pname,500,1)
# getCpu(pname,10,1)

# _thread.start_new_thread(getCpu, (pname,5,1))  

# _thread.start_new_thread(mem_thread, ())


# print(getTotalPss(pname,10,1))
# print(getCpu(pname,10,1))




# fig = plt.figure()
# ax1 = fig.add_subplot(2,1,1,xlim=(0, 100), ylim=(0, 150))
# ax2 = fig.add_subplot(2,1,2,xlim=(0, 100), ylim=(0, 100))
# line, = ax1.plot([], [], lw=2)
# line2, = ax2.plot([], [], lw=2)
# x = []
# y= []
# y2 = []
# def init():
#     line.set_data([], [])
#     line.set_data([], [])
#     return line,line2
# def getx():
#     t = "0"
#     return t

# def animate(i):
#     x.append(int(getx())+i)
#     y.append(int(getTotalPss(name))/1024) #每执行一次去获取一次值加入绘制的data中
#     y2.append(getCpu(name))
#     print(x,y)
#     line.set_data(x,y)
#     line2.set_data(x,y2)
#     return line,line2

# anim1 = animation.FuncAnimation(fig, animate, init_func=init,  frames=1000, interval=30)
# plt.show()




# print(getTotalPss(name))
# print(getCpu(name))
