import sys
import numpy as np

class LifeGame:
    def __init__(self, n_col=10, n_row=10):
        """
        """
        self.n_col = n_col
        self.n_row = n_row
        self.field = np.zeros((n_row, n_col))
        self.count_field = np.zeros((n_row, n_col))
        self.t = 0
        self.field_txt = ""

    def set_cell(self, seed):
        """
        """
        np.random.seed = seed
        for r in range(self.n_row):
            for c in range(self.n_col):
                self.field[r, c] = np.random.choice((0, 1))
        self.count_cell()

    def count_cell(self):
        """
        """
        for r in range(self.n_row):
            for c in range(self.n_col):
                if r == 0:

    def show(self):
        """
        """
        for r in range(self.n_row):
            for c in range(self.n_col):
                if self.field[r, c] == 0.:
                    self.field_txt += "□"
                else:
                    self.field_txt += "■"
                self.field_txt += " "
            self.field_txt += "\n"

    def clear(self):
        self.field_txt = ""
        sys.stdout.flush()

