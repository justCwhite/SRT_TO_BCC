import re
import json
import os



def srt2bcc(srtf):
    count1 = 1
    count2 = 2
    stime = 1
    etime = 1
    content = ""
    with open(srtf, 'r', encoding='utf-8') as f:
        for index, value in enumerate(f.readlines()):
            if index==count1:
                st1 = value.strip()[3:5]
                st2 = value.strip()[6:8]
                st3 = value.strip()[9:12]
                et1 = value.strip()[20:22]
                et2 = value.strip()[23:25]
                et3 = value.strip()[26:29]
                stime = str(int(st1) * 60 + int(st2))+ "." + st3;
                etime = str(int(et1) * 60 + int(et2))+ "." + et3;
                count1=count1+4
            elif index==count2:
                content = value.strip()[3:-4]
                count2=count2+4
                dic = {"from":float(stime),"to":float(etime),"location":2,"content":content}
                write(json.dumps(dic,ensure_ascii=False).replace(" ", "")+",",srtf)
                #print (json.dumps(dic,ensure_ascii=False))



def write(srt,srtf):
    with open("out3.bcc","a", encoding='utf-8') as o:
        o.write(srt)
        #o.closee()

def start(bccf):
    with open("out3.bcc","a", encoding='utf-8') as o:
        o.write('{"font_size":0.4,"font_color":"#FFFFFF","background_alpha":0.5,"background_color":"#9C27B0","Stroke":"none","body":[')
        #o.closee()



def end(bccf):
    with open("out3.bcc","a", encoding='utf-8') as o:
        o.seek(0,2)                 # end of file
        size=o.tell()               # the size...
        o.truncate(size-1)
        o.write("]}")
        #o.closee()

srtf = "in.srt"          #srt文件名
bccf = "out.bcc"         #bcc文件名

start(bccf)
srt2bcc(srtf)
end(bccf)
