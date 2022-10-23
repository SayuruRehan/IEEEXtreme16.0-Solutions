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

# import scipy
jobn = get_number()
workers = get_number()

jobs = []
for _ in range(jobn):
    jobs.append(get_number())
# print(jobs)
timetable = [0]*workers
timetable = timetable.sort()

# print(jobs)
for job in jobs[::-1]:
    timetable = timetable.sort()
    timetable[0] += (pow(2,job))
timetable = timetable.sort()
print(timetable[-1]%(pow(10,9)+7))

    
