#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     30/03/2017
# Copyright:   (c) Administrator 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

# initialize data to be stored in files, pickles, shelves
# records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}
# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
if __name__ == '__main__': # when run as a script
    for key in db:
        print(key, '=>\n ', db[key])