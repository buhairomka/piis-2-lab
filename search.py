import numpy as np
import pygame

from sources import WIDTH, HEIGHT, точність_побудови_маршруту, SHIP_IMG, serach_method
from matplotlib import pyplot as plt
import sys

sys.setrecursionlimit(999999999)
field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]


def check(matrix, ship_mask_with_pos):
    for point in ship_mask_with_pos:
        try:
            if matrix[point[1]][point[0]] == 5:
                return 1
            elif matrix[point[1]][point[0]] == 1:
                return 2
        except IndexError:
            return 2


visited = []
found = False


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
    elif not check_res:
        # print(curr)
        # print('ідемо далі')
        path.append(curr)
        for i in [(0, -точність_побудови_маршруту), (-точність_побудови_маршруту, 0), (точність_побудови_маршруту, 0),
                  (0, точність_побудови_маршруту), ]:
            new_curr = (curr[0] + i[0], curr[1] + i[1])
            new_ship_mask_with_pos = np.array([(h[0] + i[0], h[1] + i[1]) for h in ship_mask_with_pos],
                                              dtype=np.dtype('int64'))
            # new_ship_mask_with_pos = list(map(lambda coords: (coords[0] + i[0], coords[1] + i[1]), ship_mask_with_pos))
            if min(new_ship_mask_with_pos, key=lambda x: x[0])[0] < 0 or \
                    min(new_ship_mask_with_pos, key=lambda x: x[1])[1] < 0:
                continue
            elif found:
                break
            elif check(matrix, new_ship_mask_with_pos) == 'out':
                continue
            # print(path)
            elif new_curr not in visited:
                path = dfs(WIN, matrix, new_ship_mask_with_pos, path, new_curr)
            else:
                continue
    return path


queue = []
poped_queue = []


def restore_path(pq):
    pq = pq.reverse()
    path = []
    curr = pq[0]
    for i in pq:
        if (abs(i[0] - curr[0]) == 1 and i[1] == curr[1]) or (abs(i[1] - curr[1]) == 1 and i[0] == curr[0]):
            path.append(i)
    return path


path = []


def bfs(WIN, matrix, ship_mask_with_pos, current, player):
    '''прохід бфс'''
    global found, path, visited, queue
    queue.append(current)
    curr = current
    while len(queue) != 0 and not found:
        # print(curr,queue)
        curr = queue[0]
        # print(curr)
        visited.append(curr)
        # WIN.set_at(curr, (255, 255, 255))
        #
        # pygame.display.update()
        if found:
            queue.append(curr)
            # print('found ok')
            path = restore_path(poped_queue)
            # print(poped_queue)
            return poped_queue
        visited.append(curr)
        
        for i in [(0, -точність_побудови_маршруту), (-точність_побудови_маршруту, 0), (точність_побудови_маршруту, 0),
                  (0, точність_побудови_маршруту)]:
            new_curr = (curr[0] + i[0], curr[1] + i[1])
            new_ship_mask_with_pos = [(int(h[0] + i[0] + new_curr[0] - SHIP_IMG.get_width() / 2),
                                       int(h[1] + i[1] + new_curr[1] - SHIP_IMG.get_height() / 2)) for h in
                                      player.mask.outline()]
            
            # for i in new_ship_mask_with_pos:
            #     WIN.set_at(i, (0, 255, 255))
            # print("matrix")
            # draw_matrix(matrix)
            # print(matrix)
            # print("new_ship_mask_with_pos")
            # print(new_ship_mask_with_pos)
            # quit(0)
            check_res = check(matrix, new_ship_mask_with_pos)
            # print(check_res)
            # print(check_res, ' ---- check res')
            # if min(new_ship_mask_with_pos, key=lambda x: x[0])[0] < 0 or min(new_ship_mask_with_pos, key=lambda x: x[1])[1] < 0:
            #     continue
            if check_res == 'back':
                # print('back')
                visited.append(new_curr)
            elif check(matrix, new_ship_mask_with_pos) == 'found':
                # print('found')
                poped_queue.append(curr)
                poped_queue.append(new_curr)
                found = True
                # print(poped_queue)
                return poped_queue
            elif new_curr not in visited:
                # print('false')
                queue.append(new_curr)
        
        poped_queue.append(queue.pop(0))
    
    return []


######################################################
#        #     #####   #####      #      #####       #
#       # #    ###       #       # #     #    #      #
#      # # #       ##    #      # # #    ####        #
#     #     #  #####     #     #     #   #   ##      #
######################################################
class Node():
    """A node class for A* Pathfinding"""
    
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self, other):
        return self.position == other.position


def astar(WIN, maze, start, end_center, mask):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    
    # Initialize both open and closed list
    open_list = []
    closed_list = []
    
    # Add the start node
    open_list.append(start_node)
    counter= 200
    # Loop until you find the end
    while len(open_list) > 0 and counter>0:
        counter-=1
        # Get the current node
        current_node = open_list[0]
        
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        # WIN.set_at(current_node.position, (255, 255, 0))
        # pygame.display.update()
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        # Found the goal
        
        # for i in [(h[0] + current_node.position[0]-int(SHIP_IMG.get_width()/2), h[1] + current_node.position[1]) for h in mask]:
        #     WIN.set_at(i,(255,124,10))
        
        if check(maze,[(h[0] + current_node.position[0] - int(SHIP_IMG.get_width() / 2), h[1] + current_node.position[1]-int(SHIP_IMG.get_height() / 2) ) for h in mask]) == 1:
            # print('found')
            
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path
        
        # Generate children
        children = []
        for new_position in [(0, -12), (0, 12), (-12, 0), (12, 0), (-12, -12), (-12, 12), (12, -12),
                             (12, 12)]:  # Adjacent squares
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            # Make sure within range
            if node_position[0] > WIDTH - 1 or node_position[0] < 1 or node_position[1] > HEIGHT - 1 or node_position[
                1] < 1:
                continue
            # Make sure walkable terrain
            # Create new node
            new_node = Node(current_node, node_position)
            # Append
            children.append(new_node)
        
        # Loop through children
        for child in children:
            new_ship_mask_with_pos = [
                (h[0] + child.position[0] - int(SHIP_IMG.get_width() / 2), h[1] + child.position[1]-int(SHIP_IMG.get_height() / 2)) for h in mask]
            if check(maze, new_ship_mask_with_pos) == 2:
                # print('continiue terrarian')
                continue
            if min(new_ship_mask_with_pos, key=lambda x: x[0])[0] < 0 or \
                    min(new_ship_mask_with_pos, key=lambda x: x[1])[1] < 0:
                continue
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            
            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = (abs((child.position[0] - end_center[0])) + (abs(child.position[1] - end_center[1])))**1/2
            child.f = child.g + child.h
            
            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            
            # Add the child to the open list
            
            for to_visit_node in open_list:
                if to_visit_node == child and to_visit_node.g < child.g:
                    continue
            # WIN.set_at(child.position, (0, 255, 0))
            # pygame.display.update()
            
            open_list.append(child)


def search(WIN, player, chicks, eggs, method):
    global field, visited, queue, path, found, line, poped_queue
    
    lines = []
    for GOAL in chicks:
        field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
        for chicken in chicks:
            for point in chicken.mask.outline():
                field[point[1] + int(chicken.y)][point[0] + int(chicken.x)] = 1
        for point in GOAL.mask.outline():
            field[point[1] + int(GOAL.y)][point[0] + int(GOAL.x)] = 5
        pos = []
        for i in player.mask.outline():
            # print(player.mask.outline())
            if serach_method == 'dfs':
                pos.append((int(i[0]) + int(player.x), int(i[1]) + int(player.y)))
            elif serach_method == 'bfs' or serach_method == 'star':
                pos.append((int(i[0]), int(i[1])))
        # print(((max(player.mask.outline(), key=lambda coords: coords[0])[0] +
        #                                   min(player.mask.outline(), key=lambda coords: coords[0])[0]) // 2 + int(
        #     player.x),
        #                                  (max(player.mask.outline(), key=lambda coords: coords[1])[1] +
        #                                   min(player.mask.outline(), key=lambda coords: coords[1])[1]) // 2 + int(
        #                                      player.y)))
        for egg in eggs:
            for point in egg.mask.outline():
                try:
                    field[point[1] + int(egg.y)][point[0] + int(egg.x)] = 1
                except IndexError:
                    continue
        if method == 'dfs':
            line = dfs(WIN, field, pos, [], ((max(player.mask.outline(), key=lambda coords: coords[0])[0] +
                                              min(player.mask.outline(), key=lambda coords: coords[0])[0]) // 2 +
                                             int(player.x),
                                             (max(player.mask.outline(), key=lambda coords: coords[1])[1] +
                                              min(player.mask.outline(), key=lambda coords: coords[1])[1]) // 2 + int(
                                                 player.y)))
        elif method == 'bfs':
            line = bfs(WIN, field, pos, ((max(player.mask.outline(), key=lambda coords: coords[0])[0] +
                                          min(player.mask.outline(), key=lambda coords: coords[0])[0]) // 2 +
                                         int(player.x),
                                         (max(player.mask.outline(), key=lambda coords: coords[1])[1] +
                                          min(player.mask.outline(), key=lambda coords: coords[1])[1]) // 2 + int(
                                             player.y)), player)
        elif method == 'star':
            line = astar(WIN, field, (int(player.x + player.image.get_width() / 2), int(player.y+player.image.get_height()/2)), (int(GOAL.x + GOAL.image.get_width() / 2), int(GOAL.y + GOAL.image.get_height() / 2)), pos)
        poped_queue = []
        if line:
            lines.append(line)
        found = False
        visited = []
        queue = []
        path = []
    
    #
    # with open('matrix.txt', 'w') as testfile:
    #     for row in field:
    #         testfile.write(' '.join([str(a) for a in row]) + '\n')
    # draw_matrix(field)
    # for line in lines:
    #     for i in line:
    #         WIN.set_at((i[0], i[1]), (255, 0, 0))
    found = False
    return lines


def draw_matrix(field):
    x = [0, WIDTH]
    y = [0, HEIGHT]
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] > 0:
                x.append(int(j))
                y.append(int(HEIGHT - i))
    plt.scatter(x, y)
    plt.show()

# draw_matrix(field)
