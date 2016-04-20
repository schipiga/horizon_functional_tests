from .base import Ui


class Row(Ui):

    def __init__(self, locator, container=None, **kwgs):
        super(Row, self).__init__(locator, container)
        self._kwgs = kwgs

    @property
    @cached
    def web_element(self):
        rows = self.container.find_elements(*self.locator)
        for row in rows:
            cells = row.find_elements(*self.cell_locator)


class Col(Ui):
    pass


class Cell(Ui):
    
    @property
    @cached
    def web_element(self):
        cells = self.container.find_elements(*self.locator)
        return cells[self._index]


class Table(Ui):

    _registered_cells = None

    @classmethod
    def register_cells(cls, *cells):
        if not cls._registered_cells:
            cls._registered_cells = []
        cls._registered_cells.extend(cells)


class VTable(Table):

    _row_names = None
    _registered_rows = None

    @classmethod
    def register_rows(cls, *rows):
        if not cls._registered_rows:
            cls._registered_rows = []
        cls._registered_rows.extend(rows)

    def row(self, **kwgs):
        return Row(self._row_locator, container=self, **kwgs)


class HTable(Table):

    _registered_cols = None

    @classmethod
    def register_cols(cls, *cols):
        if not cls._registered_cols:
            cls._registered_cols = []
        cls._registered_cols.extend(cols)


def register_rows(*rows):

    def wrapper(cls):
        cls.register_rows(*rows)
        return cls

    return wrapper


def register_cols(*cols):

    def wrapper(cls):
        cls.register_cols(*cols)
        return cls

    return wrapper


def register_cells(*cells):

    def wrapper(cls):
        cls.register_cells(*cells)
        return cls

    return wrapper
