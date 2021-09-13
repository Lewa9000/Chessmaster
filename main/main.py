#!../env/bin/python -i
from string import ascii_lowercase
from itertools import product
from typing import Optional
from typing import Union
from typing import List
from typing import Tuple


class Piece:
    

    def __init__(self, color: Union['black', 'white']):
        assert color in ('white', 'black'),\
        '"color" should be "white" or "black"'
        self.__color = color
        

    def get_color(self):
        return self.__color

    def move(self):
        pass

    def capture(self, position: str):
        pass


class Pawn(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Rook(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass


class Board:


    __piece_on_cells = {}

    def __init__(self):
        self.__cols = tuple(ascii_lowercase[:8])
        self.__rows = tuple(str(row) for row in range(1, 9))
        self.arrange_pieces()


    def __find_free_cells(self):
        self.__free_cells = [f"{col}{row}"
                             for col, row in product(self.__cols, 
                                                     self.__rows
                                                     )
                             if f"{col}{row}" not in
                             self.__piece_on_cells.keys()
                            ]
        self.__free_cells.sort()



    def get_free_cells(self) -> List[str]:
        return self.__free_cells


    def get_piece_on_cells(self) -> dict:
        return self.__piece_on_cells


    def arrange_pieces(self):
        for color, row in (('white', '1'), ('black', '8')):
            self.__piece_on_cells.update(dict(zip(self.get_row(row),
                                                  [piece(color=color)
                                                   for piece in
                                                   [Rook, Knight, Bishop, 
                                                    Queen, King, Bishop, 
                                                    Knight, Rook]
                                                   ]
                                                  )
                                              )
                                          )
        for color, row in (('white', '2'), ('black', '7')):
            self.__piece_on_cells.update(dict(zip(self.get_row(row), 
                                                  [Pawn(color=color) 
                                                   for _ in range(8)
                                                   ]
                                                  )
                                               )
                                          )
        self.__find_free_cells()
        


    def get_col(self, col: str) -> Tuple[str]:
        if col not in self.__cols:
            raise ValueError('Invalid col name! '
                             f'Col name can be - {self.__cols}')
        else:
            return tuple(map(lambda x: f"{col}{x}", self.__rows))


    def get_row(self, row: str) -> Tuple[str]:
        if row not in self.__rows:
            raise ValueError('Invalid row name! '
                             f'Row name can be - {self.__rows}')
        else:
            return tuple(map(lambda x: f"{x}{row}", self.__cols))

                     
if __name__ == '__main__':
    board = Board()
    cells = board.get_free_cells()
    print(cells)


