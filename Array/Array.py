def array(array_info: list) -> list:
    arrayN: list = [0]*array_info[0][0]
    i = 0
    while i < array_info[0][1]:
        # for i in range(array_info[0][1]):
        actSum = 0
        for j in range(array_info[i+1][0], array_info[i+1][1]):
            actSum += arrayN[j]
        if (actSum % array_info[0][2] == array_info[i+1][2]):
            i += 1
            continue
        else:
            arrayN[array_info[i+1][0]] += 1
            i -= 1
        i += 1
    print(arrayN)


array([[5, 1, 7], [2, 3, 3]])
array([[20, 5, 19], [2, 7, 15], [5, 19, 0], [3, 6, 1], [6, 9, 1], [7, 19, 17]])
