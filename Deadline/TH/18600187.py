PLAYER = 'x'
OPPONENT = 'o'
class Board:
    # 'x', 'o', '_'
    def __init__(self, board):
        self.board = board

    def is_moves_left(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    return True
        return False

    def evaluate(self):
        # checking for row
        for row in range(3):
            if self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]:
                if self.board[row][0] == PLAYER:
                    return +10
                elif self.board[row][0] == OPPONENT:
                    return -10

        # checking for column
        for col in range(3):
            if self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]:
                if self.board[0][col] == PLAYER:
                    return +10
                elif self.board[0][col] == OPPONENT:
                    return -10
        

        # checking diagonal 1
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == PLAYER:
                return +10
            else:
                return -10

        # checking diagonal 2
        # TODO: code
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == PLAYER:
                return +10
            else:
                return -10
            
        return 0

    def possible_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    moves.append((i, j))
        return moves

    def make_move(self, pos, value):
        i, j = pos
        self.board[i][j] = value

    def revert_move(self, pos):
        i, j = pos
        self.board[i][j] = '_'

    def is_blank(self, pos):
        i, j = pos
        return self.board[i][j] == '_'

    def show(self):
        for i in range(3):
            for j in range(3):
              print(self.board[i][j], end='')
            print('\n')


def minimax(board: Board, depth, isMaxPlayer, i, j):
    #check i < board.size()
    if i + 1 < 3:
        i = i + 1
    #check j < board.size()
    if j + 1 < 3:
        j = j + 1
    
    best_val = board.evaluate()
    # OPPONENT go next
    if isMaxPlayer == False:
        for i in range(3):
            for j in range(3):
                if board.is_blank((i, j)):
                    board.make_move((i, j), OPPONENT)
                    move_val = board.evaluate()
                    board.revert_move((i, j))
                    
                    if move_val > best_val:
                        best_val = move_val
        return best_val
    
    
    # Player go next
    if isMaxPlayer == True:
        for i in range(3):
            for j in range(3):
                if board.is_blank((i, j)):
                    board.make_move((i, j), PLAYER)
                    move_val = board.evaluate()
                    board.revert_move((i, j))
                    
                    if move_val < best_val:
                        best_val = move_val
        return -best_val
    pass

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board.is_blank((i, j)):
                board.make_move((i, j), PLAYER)
                move_val = minimax(board, 0, False, i , j)
                board.revert_move((i, j))

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    print(f"The value of the best Move is {best_val}")
    return best_move


if __name__ == "__main__":
    board = Board([
      ['x', 'o', 'x'], 
      ['o', 'o', 'x'], 
      ['_', '_', '_']])

    best_move = find_best_move(board)
    print(f"The optimal move is: {best_move}")