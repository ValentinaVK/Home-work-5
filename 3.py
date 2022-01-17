from sys import getsizeof

tutors = [

    'Иван', 'Анастасия', 'Петр', 'Сергей',

    'Дмитрий', 'Борис', 'Елена'

]

klasses = [

    '9А', '7В', '9Б', '9В', '8Б', '10А', #'10Б', '9А'

]


def index():

    len_klasses = len(klasses)

    return ((tut, klasses[i]) if i < len_klasses else (tut, None)
            for i, tut in enumerate(tutors))


gen = index()
print("Тип данных",type(gen),"\n")
print("Размер",getsizeof(gen), "\n")

for i in gen:
    print(i,"\n")