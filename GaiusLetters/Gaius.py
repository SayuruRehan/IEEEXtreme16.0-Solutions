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

from xml.etree.ElementTree import QName
def decode(w):
    r = ""
    for i in w:
        if (ord(i)<=ord('Z') and ord(i)>=ord('A')):
            r+= chr(((ord(i)-ord('A')%26)+14)%26+ord('A'))
        elif (ord(i)<=ord('z') and ord(i)>=ord('a')):
            r+= chr(((ord(i)-ord('a')%26)+14)%26+ord('a'))
        else:r+=i
    return r

res =""

a = input()

# print(a)
res = decode(a)

print(res)
