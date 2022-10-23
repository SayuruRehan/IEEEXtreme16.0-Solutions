# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
# import numpy
# import scipy

def remove_xml(text):
    res = ""
    flag = True
    for l in text:
        if l == '<' :
            flag = False
        if (flag):
            res += l
        if l == '>':
            flag = True

    return res

p = get_number()
n = get_number()
R,C = input().split(',')
R,C = int(R),int(C)
SorL = get_word()
lines = []
for i in range(p):
    lines.append(input())
raw_xml =""
for j in range(n):
    raw_xml += input()
