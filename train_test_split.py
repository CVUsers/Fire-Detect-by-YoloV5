import os
import random
import re
import sys
def rename():
    path = 'datas/Annotations/'
    fileList = os.listdir(path)  # 待修改文件夹
    print("修改前：" + str(fileList))  # 输出文件夹中包含的文件
    currentpath = os.getcwd()  # 得到进程当前工作目录
    os.chdir(path)  # 将当前工作目录修改为待修改文件夹的位置
    num = 1  # 名称变量
    for fileName in fileList:  # 遍历文件夹中所有文件
        pat = ".+\.(jpg|jpeg|JPG|xml)"  # 匹配文件名正则表达式
        pattern = re.findall(pat, fileName)  # 进行匹配
        print('pattern[0]:', pattern)
        print('num：', num, 'filename:', fileName)
        os.rename(fileName, ('fire' + str(fileName)))  # 文件重新命名
        num = num + 1  # 改变编号，继续下一项
    print("---------------------------------------------------")
    os.chdir(currentpath)  # 改回程序运行前的工作目录
    sys.stdin.flush()  # 刷新
    print("修改后：" + str(os.listdir(path)))  # 输出修改后文件夹中包含的文件
rename()
# trainval_percent = 0.1  # 可自行进行调节
# train_percent = 1
# xmlfilepath = './data/images'
# total_xml = os.listdir(xmlfilepath)
# num = len(total_xml)
# list = range(num)
# tv = int(num * trainval_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list, tv)
# train = random.sample(trainval, tr)
# ftest = open('./data/test.txt', 'w')
# ftrain = open('./data/train.txt', 'w')
#
# for i in list:
#     name = total_xml[i] + '\n'
#     if i in trainval:
#         if i in train:
#             ftest.write('data/images/' + name)
#     else:
#         ftrain.write('data/images/' + name)
# ftrain.close()
# ftest.close()
