# Specification
#  a b c
# 1 | |
#  -+-+--
# 2 | |
#  -+-+--
# 3 | |


class TicTacToeBoard:

    def __init__(self):
        self._board = [[' ' for i in range(3)] for j in range(3)]
        self._winner = None

    def __repr__(self):
        rep = ' a b c\n'
        rep += '1{0}|{1}|{2}\n'.format(self._board[0][0],
                                       self._board[1][0],
                                       self._board[2][0])
        rep += ' -+-+--\n'
        rep += '2{0}|{1}|{2}\n'.format(self._board[0][1],
                                       self._board[1][1],
                                       self._board[2][1])
        rep += ' -+-+--\n'
        rep += '3{0}|{1}|{2}\n'.format(self._board[0][2],
                                       self._board[1][2],
                                       self._board[2][2])
        return rep

    def set(self, x, y, mark):
        self._board[x][y] = mark

    def get(self, x, y):
        return self._board[x][y]

    def is_over(self):
        if self._check('o'):
            self._winner = 'o'
            return True
        if self._check('x'):
            self._winner = 'x'
            return True
        return False

    def _check(self, mark):
        for i in range(3):
            num_row = 0
            num_column = 0

            for j in range(3):
                if self.get(i, j) == mark:
                    num_row += 1
                if self.get(j, i) == mark:
                    num_column += 1
            if num_row == 3:
                return True
            if num_column == 3:
                return True
        return False

    def get_winner(self):
        return self._winner


class TicTacToeGame:

    def __init__(self):
        self._board = TicTacToeBoard()
        self._max_num_turn = 3 * 3

    def start(self):
        num_turn = 0
        print(self._board)

        while num_turn < self._max_num_turn and not self._board.is_over():

            mark = 'o' if num_turn % 2 == 0 else 'x'
            x = None
            y = None

            while True:
                print('Turn for {0}. Please input location'.format(mark))
                loc_str = input()

                if loc_str == 'quit' or loc_str == 'q':
                    print('End this game')
                    break

                x = ord(loc_str[0]) - ord('a')
                y = ord(loc_str[1]) - ord('1')

                if x < 0 or x > 2 or y < 0 or y > 2:
                    print('location must be {abc}{123}')
                    continue

                if self._board.get(x, y) == ' ':
                    break
                else:
                    print('{0} is taken.'.format(loc_str))

            if x is None and y is None:
                break

            self._board.set(x, y, mark)
            print(self._board)

            num_turn += 1

        winner = self._board.get_winner()
        if winner:
            print('winner: {0}'.format(winner))


if __name__ == '__main__':
    board = TicTacToeBoard()
    game = TicTacToeGame()
    game.start()
