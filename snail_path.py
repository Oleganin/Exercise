def snail_path(matrix, move = 1):
    """
    Return list in snail path direction,
    if "move" == 1 (clocwise),
    else if "move" == -1 (counter-clockwise)
    """
    if move == -1:
        direct = ['down', 'right', 'up', 'left']
    elif move == 1:
        direct = ['right', 'down', 'left', 'up']
    else:
        raise TypeError('"move" must be "1" or "-1"')
    horizon_max = len(matrix[-1])-1
    horizon_min = 0
    vertical_max = len(matrix)-1
    vertical_min = 0
    result = []
    horizont_count = 0
    vertical_count = 0
    count = 0
    while count != len(matrix[-1])*len(matrix):
        result.append(matrix[vertical_count][horizont_count])
        count += 1
        if direct[0] == 'down':
            vertical_count += 1
            if vertical_count == vertical_max:
                if move == 1:
                    horizon_max -= 1
                elif move == -1:
                    horizon_min +=1
                direct.append(direct.pop(0))
        elif direct[0] == 'up':
            vertical_count -= 1
            if vertical_count == vertical_min:
                if move == 1:
                    horizon_min +=1
                elif move == -1:
                    horizon_max -= 1
                direct.append(direct.pop(0))
        elif direct[0] == 'left':
            horizont_count -= 1
            if horizont_count == horizon_min:
                if move == 1:
                    vertical_max -= 1
                elif move == -1:
                    vertical_min += 1
                direct.append(direct.pop(0))
        elif direct[0] == 'right':
            horizont_count += 1
            if horizont_count == horizon_max:
                if move == 1:
                    vertical_min += 1
                elif move == -1:
                    vertical_max -= 1
                direct.append(direct.pop(0))
    return result

print(snail_path([[ 1, 2],
                  [ 3, 4]]) ==
      [1,2,4,3])

print(snail_path([[ 1, 2, 3],
                  [ 4, 5, 6],
                  [ 7, 8, 9]]) ==
      [1,2,3,6,9,8,7,4,5])

print(snail_path([[ 1, 2, 3, 4],
                  [ 5, 6, 7, 8]]) ==
      [1,2,3,4,8,7,6,5])

print(snail_path([[ 1, 2, 3, 4, 5],
                  [ 6, 7, 8, 9,10],
                  [11,12,13,14,15]]) ==
      [1,2,3,4,5,10,15,14,13,12,11,6,7,8,9])

print(snail_path([[ 1, 2, 3, 4, 5],
                  [ 6, 7, 8, 9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20],
                  [21,22,23,24,25]]) ==
      [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13])
