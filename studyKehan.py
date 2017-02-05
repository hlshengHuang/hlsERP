# _*_ coding: utf-8 _*_
#-------------------------------------------------------------------------------
# Name:        studyKehan.py
# Purpose       test study python
#
# Author:     Lawrence
#
# Created:     01/12/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import datetime
import sys, math
import time, os, sched
import random
import pandas as pd


def main():
    print('welcome to exec main()....')
    pass

if __name__ == '__main__':
    main()

# --#

def hash_fraction(m, n):
    """Compute the hash of a rational number m / n.

    Assumes m and n are integers, with n positive.
    Equivalent to hash(fractions.Fraction(m, n)).

    """
    P = sys.hash_info.modulus
    # Remove common factors of P.  (Unnecessary if m and n already coprime.)
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
        # pow(n, P-2, P) gives the inverse of n modulo P.
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value

def hash_float(x):
    """Compute the hash of a float x."""

    if math.isnan(x):
        return sys.hash_info.nan
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())

def hash_complex(z):
    """Compute the hash of a complex number z."""

    hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    M = 2**(sys.hash_info.width - 1)
    hash_value = (hash_value & (M - 1)) - (hash_value & M)
    if hash_value == -1:
        hash_value = -2
    return hash_value
#-----------------------------------------------

now = datetime.datetime.now()




print(os.name)


def listAppend(i):
    a =[1,2,3]
    a.append(i)
    return a

def insertion_sort(list):         # insert sort
    for index in range(1,len(list)):
        value = list[index]
        i = index - 1
        while i>=0 and (value < list[i]):
            list[i+1] = list[i]
            list[i] = value
            i = i - 1

#generate fibonacci series
def fib(n):
    a,b = 0, 1
    while a < n:
        print(a,end=' ')
        a, b = b, a + b

#generate fibonacci series, return a list
def fib2(n):
    result = []
    a,b = 0, 1
    while a < n:
        result.append(a)   # 缂備焦绋戦ˇ顖炲箖?result = result + [a]
        a,b = b, a + b
    return result
# using: f = fib2(10)

def test_input(x):
    print("what do you like")
    a = input("Enter any content:") # 闁哄鐗婇幐鎼佸矗閸℃瑢鍋撳☉娆樻畼妞ゆ垳鐒︾粙澶愬矗婢跺妲繛鏉戝悑绾板秵鎱ㄩ妶澶嬬叆婵炲棙鐟х粈澶愭煠閺夎儻瀚版繝鈧悮绁攖hon3婵炴垶鎼╅崢鑲╂閵忥紕闄勯柦妯侯槹閸曢箖鎮峰▎娆戝埌闁哥姴鎳忕粋宥夊幢濮樿京顔愭繛鎴炴惄娴滎亜螞閼哥绱?
    print("I like ",a)


def test_k():
    d = {'name1':'pytontab','name2':'.','name3':'com'}
    for key in d:
        print (key,'value:',d[key])

    food = ['apples', 'oranges', 'cats']
    for i in food:
        print('I like to eat ' + i)
        print('aaa %s')


def test_grp(n):  #满足x^2+y^2<=100的整数对(x,y)有多少, n=10
    result = []
    for x in range(-n,n+1):
        #print(x)
        for y in range(-n,n+1):
            if((x*x + y*y)<=n*n):
                result.append((x,y))  # #如果想要得到一个元组（(x, y)），必须要加上括号
    print( len(result))
   # return result

#冒泡排序
def sort_bubble(x,n):
    # x is list, n is lthe length of x
    for i in range(n):
        for j in range(n-1):
            if x[j] > x[j+1]:
                t = x[j]
                x[j] = x[j+1]
                x[j+1] = t

# test for sort_bubble()
#x = [9,4,3,5,1]
#sort_bubble(x,5)
#print(x)
#将一个数插入到已经排好序的有序数据中，从而得到一个新的，个数加一的有序数据
# insert sort  # x is list, n is lthe length of x
def sort_insert(x,n):
    i = 1
    while i < n:
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key
        i += 1
#test
x = [9,4,3,5,1]
#sort_insert(x,5)
#print(x)


# 每一次从待排序的数据中选择最小（大）的一个，存放在系列的起始位置
def sort_select(num):
    length = len(num)
    for i in range(length):
        tmpNum = i
        for j in range(i,length):
            if num[tmpNum] > num[j]:
                num[tmpNum],num[j] = num[j],num[tmpNum]

    print(num)
    return num


#sort_select(x)


#快速排序，通过一趟排序将要排序的数据分割成两个独立的部分，其中一部分比了一部分所有数据都小
def sort_quick(num):
    length = len(num)
    if length <=1:
        return num
    tmpi = random.randint(0,length-1)
    tmp = num[tmpi]
    left = []
    right= []
    for i in range(0,length):
        if num[i] > tmp:
            right.append(num[i])
        else:
            left.append(num[i])
    return sort_quick(left) + sort_quick(right)

#print(sort_quick(x))

#归并排序：将当前序列分成多个序列分别排序，直到只有一个元素为止
def sort_merge(num):
    result = []
    length = len(num)
    if length <= 1:
        return num
    left = sort_merge(num[:,math.floor[length/2]])
    right = sort_merge(num[math.floor[length/2],:])
    #sort_merge(num[:math.fl])

    while len(left) > 0 and len(right):
        if left(0) <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    else:
        result.extend(right)

    return result

#sort_merge(x)

#print(sort_merge(x))















