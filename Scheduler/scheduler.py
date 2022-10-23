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
        try:
            return int(data)
        except ValueError:
            return float(data)
    except:
        pass
    

# numpy and scipy are available for use
#import numpy
#import scipy
from xml.etree.ElementTree import QName

jobn = get_number()
workers = get_number()

jobs = []
for _ in range(jobn):
    jobs.append(get_number())

timetable = [0]*workers

for job in jobs[::-1]:
    timetable = sorted(timetable)
    timetable[0] += (pow(2,job))
timetable = sorted(timetable)
print(timetable[-1]%(pow(10,9)+7))
