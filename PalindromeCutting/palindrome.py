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
from xml.etree.ElementTree import QName

from requests import get
# import numpy
# import scipy


n = get_number()
m = get_number()

res = 0
# from numpy import power
for i in range(2,n+1,2):
    res += (pow(m, i//2))
print(res)
