# -*- coding: utf-8 -*-

import math, random,time
import threading
import tkinter as tk
import re
#import uuid

Fireworks=[]
maxFireworks=8
height,width=600,600

class firework(object):
    def __init__(self,color,speed,width,height):
        #uid=uuid.uuid1()
        self.radius=random.randint(2,4)  #���Ӱ뾶Ϊ2~4����
        self.color=color   #������ɫ
        self.speed=speed  #speed��1.5-3.5��
        self.status=0   #���̻�δ��ը������£�status=0����ը��status>=1����status>100ʱ���̻�����������ֹ
        self.nParticle=random.randint(20,30)  #��������
        self.center=[random.randint(0,width-1),random.randint(0,height-1)]   #�̻������������
        self.oneParticle=[]    #ԭʼ�������꣨100%״̬ʱ��
        self.rotTheta=random.uniform(0,2*math.pi)  #��Բƽ����ת��

        #��Բ�������̣�x=a*cos(theta),y=b*sin(theta)
        #ellipsePara=[a,b]

        self.ellipsePara=[random.randint(30,40),random.randint(20,30)]   
        theta=2*math.pi/self.nParticle
        for i in range(self.nParticle):
            t=random.uniform(-1.0/16,1.0/16)  #����һ�� [-1/16,1/16) �������
            x,y=self.ellipsePara[0]*math.cos(theta*i+t), self.ellipsePara[1]*math.sin(theta*i+t)    #��Բ��������
            xx,yy=x*math.cos(self.rotTheta)-y*math.sin(self.rotTheta),  y*math.cos(self.rotTheta)+x*math.sin(self.rotTheta)     #ƽ����ת����
            self.oneParticle.append([xx,yy])
        
        self.curParticle=self.oneParticle[0:]     #��ǰ��������
        self.thread=threading.Thread(target=self.extend)   #�����̶߳���
        

    def extend(self):         #����Ⱥ״̬�仯�����߳�
        for i in range(100):
            self.status+=1    #����״̬��ʶ
            self.curParticle=[[one[0]*self.status/100, one[1]*self.status/100] for one in self.oneParticle]   #��������Ⱥ����
            time.sleep(self.speed/50)
    
    def explode(self):
        self.thread.setDaemon(True)    #���ֳ���Ϊ�ػ��߳�
        self.thread.start()          #�����߳�
            

    def __repr__(self):
        return ('color:{color}\n'  
                'speed:{speed}\n'
                'number of particle: {np}\n'
                'center:[{cx} , {cy}]\n'
                'ellipse:a={ea} , b={eb}\n'
                'particle:\n{p}\n'
                ).format(color=self.color,speed=self.speed,np=self.nParticle,cx=self.center[0],cy=self.center[1],p=str(self.oneParticle),ea=self.ellipsePara[0],eb=self.ellipsePara[1])


def colorChange(fire):
    rgb=re.findall(r'(.{2})',fire.color[1:])
    cs=fire.status
    
    f=lambda x,c: hex(int(int(x,16)*(100-c)/30))[2:]    #������������70%ʱ����ɫ��ʼ����˥��
    if cs>70:
        ccr,ccg,ccb=f(rgb[0],cs),f(rgb[1],cs),f(rgb[2],cs)
    else:
        ccr,ccg,ccb=rgb[0],rgb[1],rgb[2]
        
    return '#{0:0>2}{1:0>2}{2:0>2}'.format(ccr,ccg,ccb)



def appendFirework(n=1):   #�ݹ������̻�����
    if n>maxFireworks or len(Fireworks)>maxFireworks:
        pass
    elif n==1:
        cl='#{0:0>6}'.format(hex(int(random.randint(0,16777215)))[2:])   # ����һ��0~16777215��0xFFFFFF�������������Ϊ�����ɫ
        a=firework(cl,random.uniform(1.5,3.5),width,height)
        Fireworks.append( {'particle':a,'points':[]} )   #����������ʾ�б���particle��Ϊһ���̻����󣬡�points��Ϊÿһ��������ʾʱ�Ķ��������
        a.explode()
    else:
        appendFirework()
        appendFirework(n-1)


def show(c):
    for p in Fireworks:                #ÿ��ˢ����ʾ���Ȱ����е���������ȫ��ɾ��
        for pp in p['points']:
            c.delete(pp)
    
    for p in Fireworks:                #����ÿ���̻����󣬼�������ÿ�����ӵ���ʾ����
        oneP=p['particle']
        if oneP.status==100:        #״̬��ʶΪ100��˵���̻���������
            Fireworks.remove(p)     #�Ƴ���ǰ�̻�
            appendFirework()           #����һ���̻�
            continue
        else:
            li=[[int(cp[0]*2)+oneP.center[0],int(cp[1]*2)+oneP.center[1]] for cp in oneP.curParticle]       #������Ϊԭ�����Բƽ�Ƶ����Բ��������
            color=colorChange(oneP)   #�����̻���ǰ״̬���㵱ǰ��ɫ
            for pp in li:
                p['points'].append(c.create_oval(pp[0]-oneP.radius,  pp[1]-oneP.radius,  pp[0]+oneP.radius,  pp[1]+oneP.radius,  fill=color))  #�����̻�ÿ������

    root.after(50, show,c)  #�ص���ÿ50msˢ��һ��

if __name__=='__main__':
    appendFirework(maxFireworks)
    
    root = tk.Tk()
    cv = tk.Canvas(root, height=height, width=width)
    cv.create_rectangle(0, 0, width, height, fill="black")

    cv.pack()

    root.after(50, show,cv)
    root.mainloop()
