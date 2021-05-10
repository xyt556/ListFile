# ListFile
<h2>功能：</h2>

获取当前文件夹下的所有文件。

<h2>使用场景：</h2>

可以利用此脚本快速获取某网站源码下的所有文件，利用御剑或者是dirsearch这类工具，进行目录和文件扫描，测试未授权访问漏洞。


可用此脚本整理出属于自己的目录和文件扫描字典。
         
<h2>脚本参数说明：</h2>

脚本含两个参数

第一个参数代表你想要获取文件路径的根目录；

第二个代表文件类型。

<h2>示例：</h2>
这是一个thinkphp的项目，我想要获取它当前目录和子目录下的文件

此时复制它的路径，并添加\

![avatar](https://github.com/KOFighting/ListFile/blob/main/1620681317(1).jpg)

<h3>假如我只想要php类型文件</h3>


python3 ListFile.py E:\1\thinkphp-master\ php


![avatar](https://github.com/KOFighting/ListFile/blob/main/1620680922(1).jpg)

<h3>假如我想获取全部文件和目录的路径</h3>

python3 ListFile.py E:\1\thinkphp-master\ *


![avatar](https://github.com/KOFighting/ListFile/blob/main/1620681082(1).jpg)


获取后的文件和目录将保存在file.txt中

![avatar](https://github.com/KOFighting/ListFile/blob/main/1620681167(1).jpg)
