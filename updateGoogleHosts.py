__author__ = 'Administrator'

from bs4 import BeautifulSoup
import urllib.request
import os.path
import datetime

url = 'http://www.360kb.com/kb/2_122.html'


data = urllib.request.urlopen(url).read()

data.decode('utf-8')

soup = BeautifulSoup(data)

lstItems = soup.find_all(id='storybox')

arHostLine=[]
for item in lstItems:
    #print(item.text)
    lines = item.text.split('\n')
    bStart = False
    for item in lines:
        if len(item) < 2:
            continue
        if '#Google Services START' in item:
            bStart = True
        if bStart:
            arHostLine.append(item)
            #print(item)

#print(arHostLine)


inputHostsFile = open(r'C:\WINDOWS\system32\drivers\etc\HOSTS', 'r')
oldHostsLines = inputHostsFile.readlines()
inputHostsFile.close()

outputHostsFile = open(r'C:\WINDOWS\system32\drivers\etc\HOSTS', 'w')
bStartGoogle = False
for line in oldHostsLines:
    if '#Google Services START' in line and '#$' not in line:
        bStartGoogle = True
    if '#Google Services END' in line and '#$' not in line:
        bStartGoogle = False
        #outputHostsFile.write('#$ ' + line)
        continue
    if bStartGoogle:
        #line = '#$ '+ line
        continue
    outputHostsFile.write(line)

outputHostsFile.write('\n')
outputHostsFile.write("#****************************************"+'\n')
outputHostsFile.write('# modify hosts time:'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n')
outputHostsFile.write('#****************************************'+'\n')
for line in arHostLine:
    outputHostsFile.write(line+'\n')


outputHostsFile.close()
print('modify success.')
