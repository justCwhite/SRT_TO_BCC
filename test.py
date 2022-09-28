import srt2bcc
import re
import chardet
import os
#neirong = ""
#with open("test.srt", 'r', encoding='utf-8') as s:
#	neirong = s.read()
#s.close()
#srt2bcc.doit(neirong)
file = '1.srt'
with open(os.path.join('./inf', file),'rb') as t:
	data = t.read()
	code = chardet.detect(data)['encoding']
	if code == 'GB2312':
		code = 'GBK'
	#print(code)
	srt2bcc.srt2bcc(file,code)
