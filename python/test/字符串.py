from ctypes import sizeof
from math import floor
from random import random, uniform


def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[::-1]
    output = ' '.join(inputWords)
    return output



if __name__ == "__main__":
    input = 'aaa bbb ccc'
    rw = reverseWords(input)
    # print(rw)
    #
    # a = set('abracadabra')
    # print(a)
    # b = set('alacazam')
    # print(b)
    # print(a-b)
    print(int(round(random(),3)*1000))
    print(floor(uniform(100,999)))
    print(random())

    print("我是%s"%('wdad'))
    list=['HI']*4
    print(list)
    list.append('hi')
    print(list)
    del list[4]
    print(list)
    del list
    list= ['1', 'he']
    print(list)
    for x in list:print(x,)
    d= {'age': 8,'name':'xxx'}
    print(str(d))
    print(d)
    a,b=2,2
    a,b=b+1,a+b
    print(a,b)

    k={'a':1,'b':2,'c':3,'d':4}
    for key,value in k.items():
        print(key,value)

