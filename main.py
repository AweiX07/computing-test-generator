print("计算练习生成器")


def create_sum():
    import random
    a=random.randint(-100000,100000)
    b=random.randint(-100000,100000)
    c=random.randint(-100000,100000)
    d=random.randint(-100000,100000)
    k=a+b+c+d
    t=str(a)
    for i in (b,c,d):
        if i > 0:t+="+"+str(i)
        else:t+="-"+str(-i)
    t+=" ="
    return (t,str(k))

def create_nx():
    import random
    from fractions import Fraction
    while 1:
        l=[]
        for i in range(0,random.randint(5,10),1):
            l.append(random.randint(-100,100))
        xb=Fraction(sum(l),len(l))
        if not str(xb).isdigit():pass
        s=0
        for i in l:
            s+=(i-xb)**2
        s=Fraction(s,len(l))
        if str(s).isdigit() and s <= 1000:break
    return (""+str(l)+"\n   求这组数据的平均值和方差",str(xb)+";"+str(s))

mdic={"sum":create_sum,"nx":create_nx}


import sys
if len(sys.argv) != 3:
    print("需要两个参数：[模式] [数量]")
    exit(1)
if sys.argv[1] not in list(mdic):
    print("模式未定义")
    exit(1)
if not sys.argv[2].isdigit():
    print("数量未定义")
    exit(1)
num=int(sys.argv[2])
mod=mdic[sys.argv[1]]
del sys

import random
import time
import os
black=os.listdir()
del os
l="MATHTEST"
while 1:
    l="mathtest-"+time.strftime("%Y%m%d%H%M%S-")+str(random.randint(0,1000))+".txt"
    if l or "key-"+l not in black:break
del random
del time

print("开始生成并写入：\n试题文件："+l+"\n答案文件：key-"+l+"\n")
tf=open(l,"w",encoding="utf-8")
kf=open("key-"+l,"w",encoding="utf-8")
tf.write(l[:-4]+"\n")
kf.write("key-"+l[:-4]+"\n")

t="EMPTY"
k="EMPTY"
for i in range(1,num+1,1):
    t,k=mod()
    print("写入："+t+" |answer: "+k,end="   ")
    tf.write("\n\nQ"+str(i)+" "+t)
    kf.write("\n\nQ"+str(i)+" "+k)
    print("[完成]")

tf.close()
kf.close()
print("\n-------------------------------\n生成完毕：共"+str(i)+"道题目")
exit(0)
