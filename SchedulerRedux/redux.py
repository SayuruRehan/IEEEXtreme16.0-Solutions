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
import numpy
import scipy

N = get_number()
M = get_number()

arr = []
for i in range(N):
    arr.append(get_number())

if M == 1:
    sumerg = 0
    for j in range(N):
        sumerg += pow(2,arr[j],1000000007)
    print(sumerg % (10**9 + 7))
else:
    arr.sort(reverse=True)
    
    hmm = {}
    for val in arr:
        hmm[val] = 0
    maxx = arr[0]
    time = []
    time.append(maxx)
    for i in range(0,len(arr)):
        hmm[arr[i]] += 1
        j = arr[i]

        while(hmm[j] == 2 and j != maxx):
            hmm[j] = 0
            j += 1
            if (j in hmm):
                hmm[j] += 1
            else:
                hmm[j] = 1
        if(hmm[maxx] == M):
            if i != len(arr) -1:
                time.append(arr[i+1])
                hmm[maxx] -= M
                maxx = arr[i+1]
                
    sum = 0

    for item in time:
        sum += pow(2,item,10**9 + 7)
    print(sum % (10**9 + 7))
