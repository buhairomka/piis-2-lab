import numpy as np

from sources import точність_побудови_маршруту

def check(matrix, ship_mask_with_pos):
    for point in ship_mask_with_pos:
        try:
            if matrix[point[1]][point[0]] == 2:
                # print('found')
                return 'found'
            elif matrix[point[1]][point[0]] == 3:
                return "back"
        except IndexError:
            return 'out'
    return False

visited = []
found = False
queue = []
def dfs(WIN, matrix, ship_mask_with_pos, path, curr):
    '''прохід дфс'''
    # WIN.set_at(curr, (255, 255, 255))
    # pygame.display.update()
    global found
    global visited
    if found:
        return path
    path = path
    curr = curr
    visited.append(curr)
    check_res = check(matrix, ship_mask_with_pos)
    if check_res == 'found':
        # print(curr)
        found = True
        # print('found')
        return path
    elif check_res == "back":
        # print(curr)
        # print('back')
        return path
    elif check_res == "out":
        # print(curr)
        # print('out')
        return path
    elif not check_res:
        # print(curr)
        # print('ідемо далі')
        path.append(curr)
        for i in [(0, -точність_побудови_маршруту),(-точність_побудови_маршруту, 0),  (точність_побудови_маршруту, 0),(0, точність_побудови_маршруту),]:
            new_curr = (curr[0] + i[0], curr[1] + i[1])
            new_ship_mask_with_pos = np.array([(h[0] + i[0], h[1] + i[1]) for h in ship_mask_with_pos],dtype=np.dtype('int64'))
            # new_ship_mask_with_pos = list(map(lambda coords: (coords[0] + i[0], coords[1] + i[1]), ship_mask_with_pos))
            if min(new_ship_mask_with_pos, key=lambda x: x[0])[0] < 0 or min(new_ship_mask_with_pos, key=lambda x: x[1])[1] < 0:
                continue
            elif found:
                continue
            elif check(matrix, new_ship_mask_with_pos) == 'out':
                continue
            # print(path)
            elif new_curr not in visited:
                path = dfs(WIN, matrix, new_ship_mask_with_pos, path, new_curr)
            else:
                continue
    return path

