#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import os
from collections import Counter, defaultdict
from itertools import chain

################################################
#Pre Requisitos
################################################
# Python 2.7 ou 3.6
# Pip 20.1.1
################################################
# Bibliotecas
################################################
  # pip install Counter
  # pip install defaultdict
  # pip install chain
################################################

#Diretorio Raiz que será lido
pathOrigem = r"E:\test\ListFile"  #"/Users/Wilson/dev/demos/pagamentos"

#Nome do Arquivo de saída do ls
pathDestino = "./repo.txt"

#Nome do Arquivo resultado: no formato ->  path:/arquivo
pathResultListAll = "./resultListAll.json"

#Nome do Arquivo Agupado resultado: no formato JSON
pathResultGroup = "./resultGroup.json"

#Comandos Bash
#TODO: Pode evoluir para crar um .sh (Mac/Linux) ou .bat (Windows)
os.system("clear")
os.system("mkdir ./output")
os.system('ls -al -R -1 %s >> %s' %(pathOrigem, pathDestino))

#Processamento para Linux/Mac
fileList = []
fileOnlyList = []
f = open(pathDestino, "r")
content = f.readlines()
diretorio = ''
for l in content:
  if bool(l and l.strip()):
    lData = l[0]
    if (lData == '/'):
      diretorio = l[0:len(l)-1]
      fileList.append([diretorio, ''])
    elif (l[0:len(l)-1] != '.' and l[0:len(l)-1] != '..'  ):
      arquivo = l[0:len(l)-1]
      fileList.append([diretorio, arquivo])
      fileOnlyList.append(['', arquivo])

#Processamento do Agrupamento
counter = Counter(chain.from_iterable(fileOnlyList))
group = defaultdict(list)
for k, v in fileOnlyList:
    for i in v:
        group[i].append(k)

#Gravacao de arquivo para dos Dados Brutos
myfileAll = open(pathResultListAll, 'w')
for i in fileList:
  if (i[1] == ''):
    myfileAll.write(i[0] + '\n')
  else:
    myfileAll.write(i[0] + '/' + i[1] + '\n')
myfileAll.close()