from Matrix import Matrix
import random

class GoldRush(Matrix):
    COIN = '_$$_'
    WALL = '_WALL_'
    EMPTY = '  .  '
    PLAYER1 = 'player1'
    PLAYER2 = 'player2'
    MIN_COIN = 10
    WINNER_POINTS = 100
    DIRECTIONS = {'down' : [1,0], 'up':[-1,0], 'right':[0,1], 'left':[0,-1]}
    SCORE_PER_COIN = 10

    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.win = ""
        self.player1_score = 0
        self.player2_score = 0
        self.coins = 0
        
    def _set_coinOrDot(self,col,row):
        rand_element = self.COIN if random.randint(0, 1) else self.EMPTY
        self.matrix[col][row] = rand_element
        return 1 if rand_element == self.COIN else 0


    def _generete_random_board(self):
        for row in range(self.rows):
            self.matrix.append([self.WALL]*self.cols)
            for col in range(self.cols):
                if row % 2 != 0:
                    self.coins += self._set_coinOrDot(row,col)
            rand = random.randint(1, 2)
            for col in range(1, self.cols, rand):
                rand += 1
                self.coins += self._set_coinOrDot(row,col)

    def load_board(self):
        self.matrix = []
        if self.rows == 0 and self.cols == 0:
            return
        self._generete_random_board()
        self.matrix[0][0] = self.PLAYER1
        self.matrix[-1][-1] = self.PLAYER2

        if self.coins < self.MIN_COIN:
            self.coins = 0
            return self.load_board()
        return self.matrix

    def _check_win(self, player):
        player_num = player[-1]
        score = getattr(self, f"player{player_num}_score")
        if score == self.WINNER_POINTS:
            self.win = player
            return self.win

    

    def _move(self, curr_row, curr_col, player, delta_row, delta_col):
        other_player = self.PLAYER1 if player == self.PLAYER2 else self.PLAYER2
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return

        if self.matrix[new_row][new_col] not in [self.WALL, other_player]:
            if self.matrix[new_row][new_col] == self.COIN:
                self._add_score(player)
            self.matrix[curr_row][curr_col] = self.EMPTY
            self.matrix[new_row][new_col] = player

        return self._check_win(player)

    def move_player(self, player, direction):
        curr_row, curr_col = None, None

        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break

        self._move(curr_row, curr_col, player, self.DIRECTIONS[direction][0], self.DIRECTIONS[direction][1])

    def _add_score(self, player):
        player_num = player[-1]
        score_attr = f"player{player_num}_score"
        setattr(self, score_attr, getattr(self, score_attr) + self.SCORE_PER_COIN)
        print(getattr(self, score_attr))
