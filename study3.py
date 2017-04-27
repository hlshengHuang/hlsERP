#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     20/03/2017
# Copyright:   (c) Administrator 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000.0, 'hardware']

# print(bob[0].split()[-1]) # what's bob's last name

# sue[2] *= 1.25  # give sue a 25% raise
# print(sue)

people = [bob,sue]   # reference in list of lists
for person in people:
    print(person)
    person[2] *= 1.20 # give each a 20% raise

for person in people: print(person[2])  # check new pay

pays = [person[2] for person in people] # collect all pay

pays = map((lambda x: x[2]), people) # ditto (map is a generator in 3.X)
list(pays)

sum(person[2] for person in people) # generator expression, sum built-in

people.append(['Tom', 50, 0, None])




