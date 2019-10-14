# A*搜寻算法
# open_list: 可达到的点集合
# close_list: 已到达的点集合
# F: 从起点到某个格子，再从该格子到终点的总距离预估
# G: 从起点到当前格子的距离
# H: 从当前格子到终点的距离
# F = G + H
# 迷宫需要是一个规则的矩形


maze = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


def print_format(array_list, path):
    for i_index, i in enumerate(array_list):
        for j_index, j in enumerate(i):
            if contain_grid(path, i_index, j_index):
                print('*', end=' ')
            else:
                print(j, end=' ')
        print()


class Grid(object):
    # 设置每一个点的基本信息
    def __init__(self, x, y):
        self.x = x  # x轴坐标
        self.y = y  # y轴坐标
        self.f = 0  # g和h的综合评估， f = g + h
        self.g = 0  # 从起点走到该位置的步数
        self.h = 0  # 从当前格子到终点的步数
        self.parent = None  # 前一个结点的位置信息

    def init_grid(self, parent, end_grid):
        self.parent = parent
        if parent is not None:
            self.g = parent.g + 1
        else:
            self.g = 1
        # 曼哈顿距离求h值
        self.h = abs(self.x - end_grid.x) + abs(self.y - end_grid.y)
        self.f = self.g + self.h


def contain_grid(grids, x, y):
    for item in grids:
        if item.x == x and item.y == y:
            return True
    return False


def is_valid_grid(x, y, open_list, close_list):
    # open_list 可达到的点的集合
    # close_list 已经达到的点的集合
    # x,y越界判断
    if x < 0 or x > len(maze) or y < 0 or y > len(maze[0]):
        return False
    # 障碍物判断
    if maze[x][y] == 1:
        return False
    # 是否存在于open_list或者close_list中
    if contain_grid(open_list, x, y) or contain_grid(close_list, x, y):
        return False
    return True


def find_neighbors(grid, open_list, close_list):
    neighbors = []
    # 上下左右四个方向
    if is_valid_grid(grid.x, grid.y - 1, open_list, close_list):
        neighbors.append(Grid(grid.x, grid.y - 1))
    if is_valid_grid(grid.x, grid.y + 1, open_list, close_list):
        neighbors.append(Grid(grid.x, grid.y + 1))
    if is_valid_grid(grid.x - 1, grid.y, open_list, close_list):
        neighbors.append(Grid(grid.x - 1, grid.y))
    if is_valid_grid(grid.x + 1, grid.y, open_list, close_list):
        neighbors.append(Grid(grid.x + 1, grid.y))
    return neighbors


def find_min_grid(open_list):
    # 发现可达点中的最小f值点，如果存在相同的则任取一个
    min_grid = open_list[0]
    for item in open_list:
        if min_grid.f > item.f:
            min_grid = item
    return min_grid


def a_star_search(start, end):
    open_list = []
    close_list = []
    open_list.append(start)

    while len(open_list):
        current_grid = find_min_grid(open_list)
        open_list.remove(current_grid)
        close_list.append(current_grid)

        neighbors = find_neighbors(current_grid, open_list, close_list)
        for item in neighbors:
            item.init_grid(current_grid, end)
            open_list.append(item)

        for item in open_list:
            if item.x == end.x and item.y == end.y:
                return item

    return None


if __name__ == '__main__':
    print_format(maze, [])
    start = Grid(3, 1)
    end = Grid(3, 5)
    result_grid = a_star_search(start, end)

    path = []
    while result_grid is not None:
        path.append(Grid(result_grid.x, result_grid.y))
        result_grid = result_grid.parent

    print("======================================")
    print_format(maze, path)
