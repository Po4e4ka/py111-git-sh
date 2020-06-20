def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    if shape[0] < point[0] or shape[1] < point[1]:
        print('Точка выходит за пределы поля')
        return 0
    result_mass = []
    for l in range(shape[0]):
        result_mass.append([])
        for i in range(shape[1]):
            if l == i == 0:
                result_mass[l].append(1)
            else:
                result_mass[l].append(0)
            if l > 0:
                if i - 2 >= 0 and                       result_mass[l-1][i-2] > 0:
                    result_mass[l][i] +=                result_mass[l-1][i-2]*2
                if l - 1 > 0 and i-1 >= 0 and           result_mass[l-2][i-1] > 0:
                    result_mass[l][i] +=                result_mass[l-2][i-1]*2
                if i + 2 < shape[1] and                 result_mass[l-1][i+2] > 0:
                    result_mass[l][i] +=                result_mass[l-1][i+2]*2
                if l - 1 > 0 and i + 1 < shape[1] and   result_mass[l-2][i+1] > 0:
                    result_mass[l][i] +=                result_mass[l-2][i+1]*2

    return result_mass[point[0]][point[1]]

