import os
import sys


def get_path(path):
    flag = True         #设置标志位，True代表当前目录还有子目录
    dir_list = [path]       #初始化一个目录列表,代表当前目录的子目录有哪些
    file_list = []          #存放已经存在的文件列表路径
    while flag:
        for i in range(0,len(dir_list)):
            file_path = dir_list.pop()
            try:
                files = os.listdir(file_path)   #获取当前目录下的文件和目录列表
                for file in files:
                    file_list.append(file_path+file)
                    if "." not in file:
                        dir_list.append(file_path+file+'/')
            except:                             #当目录下没有文件时，抛出异常
                pass
        if len(dir_list) <= 0:
            flag = False
    return file_list        
def save_file(path):
    file_list = get_path(path)
    for file in file_list:
        file = file.replace(path,'/')#去除根目录
        print(file)
        with open('file.txt','a')as f:
            f.write(file+'\n')
            f.close()

if __name__ == '__main__':
    path = sys.argv[1]
    if '\\' in path:
        path = path.replace('\\','/')
    save_file(path)    