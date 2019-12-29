# -*- coding: UTF-8 -*-

import os

# for python2
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

# import pdfminer.

# 获取指定目录下所有文件的列表
def getFileList(p):
    p = str(p)
    if p == "":
        return []

    # p = p.replace("/", "\\") #for windows
    # if p[-1] != "\\":
    #     p = p + "\\"

    if p[-1] != "/":
        p = p + "/"

    a = os.listdir(p)
    b = [x for x in a if os.path.isfile(p + x)]
    return b

# 获取指定目录下的所有子目录的列表
def getDirList(p):
    p = str(p)
    if p == "":
        return []

    # p = p.replace("/", "\\") #for windows
    # if p[-1] != "\\":
    #     p = p + "\\"
    if p[-1] != "/":
        p = p + "/"

    a = os.listdir(p)
    b = [x for x in a if os.path.isdir(p + x)]
    return b

# print getFileList('.')
# print getDirList('.')


# s_filename = 'VLDB2016.pdf'
# sourcedir = 'data'
# outputdir = 'result'
# # para1=' -P 1 -M 2.0 -L 0.5 -W 0.1 -F 0.0 '
def pdf2txt_onefile(s_filename,sourcedir,outputdir,para1):

    sourcedir = sourcedir+'/' + s_filename
    o_filename = (os.path.splitext(s_filename))[0] + '.txt'
    s_programe = "/mnt/hgfs/Desktop/ubuntu/xrh/python_patch/pdfminer/tools/pdf2txt.py"
    outputdir = outputdir +'/'+ o_filename


    s_para = ' -o ' + outputdir + ' '+para1+' ' + sourcedir
    cmd = s_programe + ' ' + s_para
    print ('cmd:', cmd)
    os.system(s_programe + ' ' + s_para)

# pdf2txt_onefile('VLDB2016.pdf','data','result',' -M 2.0 -L 0.5 -W 0.1 -F 0.0 ') the para for english

pdf2txt_onefile('chinese_sample1.pdf','data','result',' -M 2.0 -L 1.5 -W 0.1 -F -0.5 ') # the para for Chinese


def pdf2txt(targetdir,isEnglish=1):
    """
    把 targetdir 目录下的所有pdf都转换为 txt
    若 isEnglish=1 则采用 英语的参数进行转换
    若 isEnglish=0 则采用中文的参数
    :param targetdir:  
    :return: 
    """
    if targetdir is None:
        # 得到当前工作目录，即当前Python脚本工作的目录路径
        s = os.getcwd()
        targetdir=s # configure

    # print 'targetdir:',targetdir
    filename= os.listdir(targetdir+'/data')
    for s_filename in filename:
        if isEnglish==1:
            pdf2txt_onefile(s_filename,'data','result',' -M 2.0 -L 0.5 -W 0.1 -F 0.0 ')
        else:
            pdf2txt_onefile(s_filename, 'data', 'result', ' -M 2.0 -L 1.5 -W 0.1 -F -0.5 ')


# pdf2txt(None)

import codecs
import chardet
import re
def txt_trans_onefile(dir):
    file = open(dir,'rb') #NO.1 open the txt to check the coded format,in windows it is often gb2332
    data=file.read()
    detect = chardet.detect(data)
    if data[:3] == codecs.BOM_UTF8:
        data = data[3:]
    data=data.decode(detect['encoding'])
    # print data
    file.close()

    file = open('tmp.txt','wb') #NO.2 change the the coded format into utf-8 and eliminate the BOM in windows txt
    file.write(data.encode('utf-8'))
    file.close()

    file = open('tmp.txt', 'rb')
    alllines=file.readlines()
    print (alllines)
    for i in range(len(alllines)):
        # print line
        line=alllines[i]

        if re.match(r'^\n$|^\r\n$', line) is  None: #in some txt the end of the line is \n ; while others is \r\n
            line=re.sub('\n|\r\n', ' ', line) #string replace using regular
            alllines[i] = line

        # if line != '\n':
        #     line = line.replace('\n', '')
        #     alllines[i]=line
        #
        # if line!='\r\n':
        #     line = line.replace('\r\n', '')
        #     alllines[i] = line

    print (alllines)
    file.close()

    file = open('tmp.txt', 'wb')
    file.writelines(alllines)
    file.close()



# dir='result/VLDB2016.txt'
dir = 'result/chinese_sample1.txt'
# dir='笔记.txt'
txt_trans_onefile(dir)