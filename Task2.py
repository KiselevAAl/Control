def dlina():
    q = int(input('Введите длину x: '))
    w = int(input('Введите длину y: '))
    e = int(input('Введите длину z: '))
    if q == w:
        return 'Этот треугольник равнобедренный'
    elif q == w and w == e and q == e:
        return'Этот треугольник является равносторонним'
    else:
        return 'Этот треугольник разносторонний'

dlina_treugol = dlina()


