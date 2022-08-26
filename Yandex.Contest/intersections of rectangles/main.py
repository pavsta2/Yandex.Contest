with open('input.txt') as f:
    num = int(f.readline())  #читаем из файла кол-во прямоугольников
    rec_list = []
    for i in range(num):
        rec_list.append([int(i) for i in f.readline().split(' ')])  #читаем из файла и создаем список из списков
set_list = []  #создаем итоговый список для работы
for j in rec_list:
    set_x = set()
    set_y = set()
    set_x.update(range(j[0], j[2] + 1))  #множество,содержащее все координаты х стороны прямоуголника
    set_y.update(range(j[1], j[3] + 1))  #множество,содержащее все координаты у стороны прямоуголника
    set_list.append((set_x, set_y))  #заполняем список кортежами с множествами

for rec in set_list:  #выбираем прямоугольник для сравнения
    n = 0
    for rec_compar in set_list:  #сравниваем со всеми прямоуголниками из списка, в том числе и с самим собой
        if len(rec[0] & rec_compar[0]) > 1 \
                and len(rec[1] & rec_compar[1]) > 1:  #пересечения множеств с координатами точек х и у должны быть больше 1
            n += 1
    n_result = n - 1  #вычитаем единицу, так как одна итерация была сравнением прямоугольника с самим собой же
    print(n_result)
