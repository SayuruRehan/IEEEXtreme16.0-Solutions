from numpy import array


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    return int(data)


#! name : (paided, received)
# persons: dict = {"Alice": [1, 0], "Bob": [0, 1], "Chuck ": [
#     1, 0], "Dave ": [1, 1], "Eve ": [0, 1]}


def isfree(persons: dict, name: str):
    if (persons[name][0] == persons[name][1]):
        return False
    else:
        return True


def isneedToPay(persons: dict, name: str):
    if (persons[name][0] < persons[name][1]):
        return True
    else:
        return False


def isneedMeal(persons: dict, name: str):
    if (persons[name][0] > persons[name][1]):
        return True
    else:
        return False


# def balanceMeals(persons: dict):
#     for name in persons:
#         if (isneedMeal(persons, name)):
#             print("Need to pay", name)
#             for claveAux in persons:
#                 if (claveAux != name):
#                     if (isfree(persons, claveAux)):
#                         print("Free", claveAux)
#                         persons[claveAux][0] += 1
#                         persons[name][1] += 1
#                         break

def myTreat(dict):
    cantMeals = 0
    cantDays = 0

    for clave in dict:
        cantDaysAux = 0
        compradas = dict[clave][0]
        comidas = dict[clave][1]
        falta = comidas-compradas  # negativo falta comer

        # Caso1: falta comer
        if (falta < 0):

            # cuantas le faltan
            faltan = compradas - comidas
            for claveAux in dict:
                if (clave != claveAux):
                    compradasAux = dict[claveAux][0]
                    comidasAux = dict[claveAux][1]
                    faltaAux = comidasAux-compradasAux  # negativo falta comer

                    # buys
                    if (faltaAux > 0):
                        # cuantas me puede dar
                        while faltan > 0 and dict[claveAux][0] < dict[claveAux][1]:
                            dict[claveAux][0] += 1
                            dict[clave][1] += 1

                            cantMeals += 1
                            cantDaysAux += 1
                            if (cantDays < cantDaysAux):
                                cantDays = cantDaysAux

                            faltan -= 1

                    if (faltan == 0):
                        break

    return cantMeals, cantDays


def addPerson(persons: dict, name: str, paidedMeals: int = 0):
    if (name not in persons):
        persons.update({name: [paidedMeals, 0]})


def paidMealsfor(persons: dict, paid_name: str, recieve_name: str):
    persons[paid_name] = [persons[paid_name][0] + 1, persons[paid_name][1]]
    persons[recieve_name] = [persons[recieve_name][0],
                             persons[recieve_name][1] + 1]


# ------------------------------------
T: int = int(input())
array: list = []

for i in range(T):
    M: int = int(input())
    persons: dict = {}
    for j in range(M):
        input_parser = parser()
        person_who_paid = get_word()
        N = get_number()
        addPerson(persons, person_who_paid)  # add person if not exist
        for k in range(N):
            name = get_word()
            addPerson(persons, name)  # add person if not exist
            paidMealsfor(persons, person_who_paid, name)
    array.append(persons)
for i in array:
    res = myTreat(i)
    print(res[0], res[1])
