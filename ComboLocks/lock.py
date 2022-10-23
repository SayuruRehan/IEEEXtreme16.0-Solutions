import sys
        
# sys.stdin = open('combo-locks-input.txt','r')

# words = []
# while (True):
#     try:
#         word = input()
#         words.append(word)
#     except (EOFError):
#         break

for i in range(8):
    print('aiueo',end='')
    cnt = 5
    for j in range(0,26):
        c = f"{chr(ord('a')+j)}"
        if (c in 'aiueo'): continue
        if (cnt < 10): 
            print(c,end='')
            cnt += 1
    print()
