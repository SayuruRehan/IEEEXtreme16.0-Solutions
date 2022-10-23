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
budget = get_number()

p = get_number()
P = {}
for _ in range(p):
    name = get_word()
    price = get_number()
    P[name] = price

g = get_number()
G = {}
for _ in range(g):
    name = get_word()
    price = get_number()
    G[name] = price
s = get_number()
S = {}
for _ in range(s):
    name = get_word()
    price = get_number()
    S[name] = price

f = get_number()
F = {}
for _ in range(f):
    name = get_word()
    price = get_number()
    F[name] = price

c = get_number()
C = {}
for _ in range(c):
    name = get_word()
    price = get_number()
    C[name] = price
max = 0
DT = []
for c in C:
    for f in F:
        for s in S:
            for g in G:
                for p in P:
                    tmp = P[p]+G[g]+S[s]+F[f]+C[c]
                    if ( tmp > max and tmp < budget):
                        DT = [p,g,s,f,c]
                        max =tmp
for i in DT:
    print (i)

