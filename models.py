import time
import random
import sys


class Table():
    def __init__(self, size=(5,3)):
        self.grid = []
        self.size = size
        for y in range(size[0]):
            row = []
            
            for x in range(size[1]):
                current_cell = Cell(self, (x,y))
                alive_percent = 5

                if random.randint(0, alive_percent) == 1:
                    current_cell.live()

                row.append(current_cell)

            self.grid.append(row)


    def next_gen(self):
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                cell = self.coords2cell(x,y)
                neighbors = cell.get_neighbors()
                n_alives = 0

                for neighbor in neighbors:
                    if neighbor.is_alive:
                        n_alives += 1

                if not cell.is_alive:
                    if n_alives == 3:
                        cell.live()
                else:
                    if n_alives < 2 or n_alives > 3:
                        cell.die()


    def run(self, sleep):
        while True:
            self.next_gen()
            self.render()
            time.sleep(sleep)


    def coords2cell(self, x, y):
        return self.grid[y][x]


    def render(self):
        s = "\n".join([str(elem) for elem in self.grid])
        sys.stdout.write(s)
        sys.stdout.flush()
        sys.stdout.write("\b"*len(s))



class Cell():
    def __init__(self, table, position):
        self.is_alive = False
        self.table = table
        self.pos = position


    def live(self):
        self.is_alive = True


    def die(self):
        self.is_alive = False


    def get_neighbors(self):
        neighbors = []
        sx = self.pos[0] - 1  # Startx: one x before this cells position
        sy = self.pos[1] - 1  # Starty: one y before this cells position

        for y in range(sy, sy + 3):
            if y < 0 or y >= self.table.size[0]:
                continue

            for x in range(sx, sx+3):
                if x < 0 or x >= self.table.size[1]:
                    continue

                coords = (x,y)
                if coords == self.pos:
                    continue

                cell = self.table.coords2cell(x,y)
                neighbors.append(cell)

        return neighbors


    def __repr__(self):
        if self.is_alive:
            return "X"
        else:
            return "O"
        