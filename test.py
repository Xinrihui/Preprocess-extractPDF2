# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

############### Python 编码转换与中文处理 #####################

# Part1

# unicode 转为 gb2312,utf-8等,使用 encode(encoding)
# s = u'中国' #unicode
# print s
# s_gb = s.encode('gb2312')
# print s_gb
#
# # utf-8,GBK转换为 unicode 使用 unicode(s,encoding) 或者 s.decode(encoding)
# # s_unicode=unicode(s_gb,'gb2312')
# s_unicode=s_gb.decode('gb2312')
# print  s_unicode
#
# s = '中国'
# su = u'中国'
# # s为unicode先转为utf-8
# # 因为s为所在的.py(# -*- coding=UTF-8 -*-)编码为utf-8
# s_unicode = s.decode('UTF-8')
# assert (s_unicode == su)
# # s转为gb2312:先转为unicode再转为gb2312
# s.decode('utf-8').encode('gb2312')
#
# s = '中国'
# s.encode('gb2312') # 这里会发生一个异常：Python 会自动的先将 s 解码为 unicode ，然后再编码成 gb2312。因为解码是python自动进行的，我们没有指明解码方式，python 就会使用 sys.defaultencoding 指明的方式来解码。很多情况下 sys.defaultencoding 是 ANSCII，如果 s 不是这个类型就会出错。

#part2

# import codecs
# import chardet
# dir='笔记.txt'
#
# data = open(dir).read()
# detect= chardet.detect(data)
# if data[:3] == codecs.BOM_UTF8:
#     data = data[3:]
# print data.decode(detect['encoding'])
###########################################

###########change file name ############
# import os
# path='.'
# print os.listdir(path)
#
# # os.rename('\xe7\xac\x94\xe8\xae\xb0.txt','abc.txt')
#
# os.rename('abc.txt','\xe7\xac\x94\xe8\xae\xb0.txt')
# dir='笔记.txt'

#####################

import subprocess


# r = subprocess.call(['cat', '\xe7\xac\x94\xe8\xae\xb0.txt'])
# r=subprocess.call(['cat', u'笔记.txt'])
r=subprocess.call(['cat', '笔记.txt'])
print('Exit code:', r)

# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# # print(output.decode('utf-8'))
# print('Exit code:', p.returncode)