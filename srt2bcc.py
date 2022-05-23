import re
import json
import os
import time
import datetime

def srt2bcc(srtf,code):
    bccf = srtf.strip()[0:-3]+"bcc"
    start(bccf)
    count1 = 1
    count2 = 2
    stime = 1
    etime = 1
    num = 1
    content = ""
    print(code)
    with open(os.path.join('./inf', srtf), 'r', encoding=code) as f:
        counttt=len(open(os.path.join('./inf', srtf),'r',encoding=code).readlines())-1
        for index, value in enumerate(f.readlines()):
            #print (index,count1,count2)
            value = value.strip('\n')
            #print (index,count1,count2)
            if value == str(num):
                count1 = index+1
                count2 = count1+1
                num = num+1
            elif index==count1:
                st1 = value.strip().split(':')[0]
                st2 = value.strip().split(':')[1]
                st3 = value.strip().split(':')[2].split(',')[0]
                st4 = value.strip().split(':')[2].split(',')[1].split()[0]
                et1 = value.strip().split(':')[2].split()[2]
                et2 = value.strip().split(':')[3]
                et3 = value.strip().split(':')[4].split(',')[0]
                et4 = value.strip().split(':')[4].split(',')[1]
                #stime = str(st1 * 60 + st2)+ "." + str(st3);
                #etime = str(et1 * 60 + et2)+ "." + str(et3);
                #print (st1,st2,st3,et1,et2,et3)
                stime = str(int(st1) * 3600 + int(st2) * 60 + int(st3))+ "." + st4;
                etime = str(int(et1) * 3600 + int(et2) * 60 + int(et3))+ "." + et4;
                #print(int(st1),int(st2),int(st3),int(et1),int(et2),int(et3))
                #count1=count1+4
            elif index==count2:
                #content = value.strip()[3:-4]
                content = value
                #count2=count2+4
                #dic = {"from":float(stime),"to":float(etime),"location":2,"content":content}
                #write1(json.dumps(dic,ensure_ascii=False).replace(" ", "")+",",bccf)
            elif value=="":
                dic = {"from":float(stime),"to":float(etime),"location":2,"content":content}
                write1(json.dumps(dic,ensure_ascii=False).replace(" ", "")+",",bccf)
            elif index == counttt:
                content = content+"\n"+value
                dic = {"from":float(stime),"to":float(etime),"location":2,"content":content}
                write1(json.dumps(dic,ensure_ascii=False).replace(" ", "")+",",bccf)
            elif value :
                #content = value.strip()[3:-4]
                content = content+"\n"+value
                #print(content)
                #count2=count2+4
                #dic = {"from":float(stime),"to":float(etime),"location":2,"content":content}
                #write1(json.dumps(dic,ensure_ascii=False).replace(" ", "")+",",bccf)
            #print(index == counttt)
    f.close()
    end(bccf)
    return bccf
                #print (json.dumps(dic,ensure_ascii=False))

def doit(zimu):
    #srtf = "in.srt"          #srt文件名
    t = time.time()
    bccf = "out.bcc"         #bcc文件名
    srtf = str(int(round(t * 1000)))+"in.srt"
    with open(srtf,"a", encoding='utf-16') as z:
        z.write(zimu)
    start(bccf)
    srt2bcc(srtf)
    end(bccf)

def write1(srt,bccf):
    with open(os.path.join('./outf', bccf),"a", encoding='utf-8') as o:
        o.write(srt)
        #o.closee()

def start(bccf):
    with open(os.path.join('./outf', bccf),"w", encoding='utf-8') as o:
        o.write('{"font_size":0.4,"font_color":"#FFFFFF","background_alpha":0.5,"background_color":"#9C27B0","Stroke":"none","body":[')
        #o.closee()



def end(bccf):
    with open(os.path.join('./outf', bccf),"a", encoding='utf-8') as o:
        o.seek(0,2)                 # end of file
        size=o.tell()    # the size...
        o.truncate(size-1)
        o.write(']}')
        o.close()

def readit():
    with open("out3.bcc", 'r', encoding='utf-16') as s:
        shuchu = s.read()
        s.close()
    return shuchu

#srtf = "in.srt"          #srt文件名
#bccf = "out.bcc"         #bcc文件名

#keep(zimu)
#start(bccf)
#srt2bcc("2.srt")
#end(bccf)
