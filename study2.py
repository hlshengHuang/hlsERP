#-------------------------------------------------------------------------------
# Name:        妯″潡1
# Purpose:
#
# Author:      Administrator
#
# Created:     05/02/2017
# Copyright:   (c) Administrator 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import io
import os

def main():
    pass

if __name__ == '__main__':
    main()

f = open('test.txt','r+')
for line in f:
   # print(line,'')
    f.write('99')

s = os.sep
root = "F:\\SVNcheckout\\testdir" + s
for i in os.listdir(root):
    if os.path.isfile(os.path.join(root,i)):
        pass
       # print(i)


for root, dirs, files in os.walk(root):
    #遍历目录及目录下的文件
    f = open('readme.htm','w')
    ds = '--'

    for d in dirs:

       ds = ds.join('--')
       print(ds + d)
       f.write(ds + d)
       for name in files:
           print(ds + s + name)
           f.write(ds+s+name)

    f.close()





def ISIP(s):
    #return len([i for i in s.split('.') if (0<= int(i)<= 255)])== 4
    for i in s.split('.'):
         if (0<= int(i)<= 255):
            print(i)

# ISIP('100.100.100.200')


