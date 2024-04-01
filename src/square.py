class Square:

    def __init__(self, row, color, piece=None):
        self.row = row
        self.color = color
        self.piece = piece

    def has_piece(self):
        return self.piece != None