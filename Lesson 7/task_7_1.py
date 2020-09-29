class Cell:
    cells: int

    def __init__(self, cells: int):
        self.cells = cells

    def __str__(self):
        return str(self.cells)

    def __int__(self):
        return self.cells

    def __add__(self, cells: 'Cell'):
        return Cell(self.cells + cells.cells)

    def __sub__(self, cells: 'Cell'):
        if (result := self.cells - cells.cells) < 0:
            return "Р Р°Р·РЅРёС†Р° РјРµРЅСЊС€Рµ РЅСѓР»СЏ"
        else:
            return Cell(result)

    def __mul__(self, cells: 'Cell'):
        return Cell(self.cells * cells.cells)

    def __truediv__(self, cells: 'Cell'):
        return Cell(self.cells - cells.cells)

    @staticmethod
    def make_order(cell: 'Cell', n: int):
        fullrow, lastrow = divmod(cell.cells, n)
        return '\n'.join([str('*') * n for _ in range(0, fullrow)]) + '\n' + '*' * lastrow


cell0 = Cell(5)
cell1 = Cell(10)
cell2 = Cell(12)
print('cell0 + cell2', cell0 + cell2)
print('cell1 - cell2', cell1 - cell2)
print('cell2 - cell1', cell2 - cell1)
print('cell0 * cell1', cell0 * cell1)
print('cell1 / cell0', cell1 / cell0)
print(cell1.make_order(cell1, 4))