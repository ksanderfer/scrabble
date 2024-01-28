from collections import defaultdict

#the expected value of a tile in scrabble
avgval = 1.88

#a mapping of coordinates to the multiplier of that space
board = {
(0,0): "TW",  (0,1): "1",   (0,2): "1",   (0,3): "DL",  (0,4): "1",   (0,5): "1",   (0,6): "1",   (0,7): "TW",  (0,8): "1",   (0,9): "1",   (0,10): "1",   (0,11): "DL",  (0,12): "1",   (0,13): "1",   (0,14): "TW",
(1,0): "1",   (1,1): "DW",  (1,2): "1",   (1,3): "1",   (1,4): "1",   (1,5): "TL",  (1,6): "1",   (1,7): "1",   (1,8): "1",   (1,9): "TL",  (1,10): "1",   (1,11): "1",   (1,12): "1",   (1,13): "DW",  (1,14): "1",
(2,0): "1",   (2,1): "1",   (2,2): "DW",  (2,3): "1",   (2,4): "1",   (2,5): "1",   (2,6): "DL",  (2,7): "1",   (2,8): "DL",  (2,9): "1",   (2,10): "1",   (2,11): "1",   (2,12): "DW",  (2,13): "1",   (2,14): "1",
(3,0): "DL",  (3,1): "1",   (3,2): "1",   (3,3): "DW",  (3,4): "1",   (3,5): "1",   (3,6): "1",   (3,7): "DL",  (3,8): "1",   (3,9): "1",   (3,10): "1",   (3,11): "DW",  (3,12): "1",   (3,13): "1",   (3,14): "DL",
(4,0): "1",   (4,1): "1",   (4,2): "1",   (4,3): "1",   (4,4): "DW",  (4,5): "1",   (4,6): "1",   (4,7): "1",   (4,8): "1",   (4,9): "1",   (4,10): "DW",  (4,11): "1",   (4,12): "1",   (4,13): "1",   (4,14): "1",
(5,0): "1",   (5,1): "TL",  (5,2): "1",   (5,3): "1",   (5,4): "1",   (5,5): "TL",  (5,6): "1",   (5,7): "1",   (5,8): "1",   (5,9): "TL",  (5,10): "1",   (5,11): "1",   (5,12): "1",   (5,13): "TL",  (5,14): "1",
(6,0): "1",   (6,1): "1",   (6,2): "DL",  (6,3): "1",   (6,4): "1",   (6,5): "1",   (6,6): "DL",  (6,7): "1",   (6,8): "DL",  (6,9): "1",   (6,10): "1",   (6,11): "1",   (6,12): "DL",  (6,13): "1",   (6,14): "1",
(7,0): "TW",  (7,1): "1",   (7,2): "1",   (7,3): "DL",  (7,4): "1",   (7,5): "1",   (7,6): "1",   (7,7): "ST",  (7,8): "1",   (7,9): "1",   (7,10): "1",   (7,11): "DL",  (7,12): "1",   (7,13): "1",   (7,14): "TW",
(8,0): "1",   (8,1): "1",   (8,2): "DL",  (8,3): "1",   (8,4): "1",   (8,5): "1",   (8,6): "DL",  (8,7): "1",   (8,8): "DL",  (8,9): "1",   (8,10): "1",   (8,11): "1",   (8,12): "DL",  (8,13): "1",   (8,14): "1",
(9,0): "1",   (9,1): "TL",  (9,2): "1",   (9,3): "1",   (9,4): "1",   (9,5): "TL",  (9,6): "1",   (9,7): "1",   (9,8): "1",   (9,9): "TL",  (9,10): "1",   (9,11): "1",   (9,12): "1",   (9,13): "TL",  (9,14): "1",
(10,0): "1",  (10,1): "1",  (10,2): "1",  (10,3): "1",  (10,4): "DW", (10,5): "1",  (10,6): "1",  (10,7): "1",  (10,8): "1",  (10,9): "1",  (10,10): "DW", (10,11): "1",  (10,12): "1",  (10,13): "1",  (10,14): "1",
(11,0): "DL", (11,1): "1",  (11,2): "1",  (11,3): "DW", (11,4): "1",  (11,5): "1",  (11,6): "1",  (11,7): "DL", (11,8): "1",  (11,9): "1",  (11,10): "1",  (11,11): "DW", (11,12): "1",  (11,13): "1",  (11,14): "DL",
(12,0): "1",  (12,1): "1",  (12,2): "DW", (12,3): "1",  (12,4): "1",  (12,5): "1",  (12,6): "DL", (12,7): "1",  (12,8): "DL", (12,9): "1",  (12,10): "1",  (12,11): "1",  (12,12): "DW", (12,13): "1",  (12,14): "1",
(13,0): "1",  (13,1): "DW", (13,2): "1",  (13,3): "1",  (13,4): "1",  (13,5): "TL", (13,6): "1",  (13,7): "1",  (13,8): "1",  (13,9): "TL", (13,10): "1",  (13,11): "1",  (13,12): "1",  (13,13): "DW", (13,14): "1",
(14,0): "TW", (14,1): "1",  (14,2): "1",  (14,3): "DL", (14,4): "1",  (14,5): "1",  (14,6): "1",  (14,7): "TW", (14,8): "1",  (14,9): "1",  (14,10): "1",  (14,11): "DL", (14,12): "1",  (14,13): "1",  (14,14): "TW"
}

#a mapping of letters to a mapping of points and quantity of tiles
tiles = {
    "A": {"points": 1, "quantity": 9}, 
    "B": {"points": 3, "quantity": 2}, 
    "C": {"points": 3, "quantity": 2}, 
    "D": {"points": 2, "quantity": 4}, 
    "E": {"points": 1, "quantity": 12}, 
    "F": {"points": 4, "quantity": 2}, 
    "G": {"points": 2, "quantity": 3}, 
    "H": {"points": 4, "quantity": 2}, 
    "I": {"points": 1, "quantity": 9}, 
    "J": {"points": 8, "quantity": 1}, 
    "K": {"points": 5, "quantity": 1}, 
    "L": {"points": 1, "quantity": 4}, 
    "M": {"points": 3, "quantity": 2}, 
    "N": {"points": 1, "quantity": 6}, 
    "O": {"points": 1, "quantity": 8}, 
    "P": {"points": 3, "quantity": 2}, 
    "Q": {"points": 10, "quantity": 1}, 
    "R": {"points": 1, "quantity": 6}, 
    "S": {"points": 1, "quantity": 4}, 
    "T": {"points": 1, "quantity": 6}, 
    "U": {"points": 1, "quantity": 4}, 
    "V": {"points": 4, "quantity": 2}, 
    "W": {"points": 4, "quantity": 2}, 
    "X": {"points": 8, "quantity": 1}, 
    "Y": {"points": 4, "quantity": 2}, 
    "Z": {"points": 10, "quantity": 1}, 
    "_": {"points": 0, "quantity": 2},
    None: {"points": 0, "quantity": 0}
}

game_score = 0

def get_points(tile: str) -> int:
    return tiles.get(tile).get("points")

def get_quantity(tile: str) -> int:
    return tiles.get(tile).get("quantity")

def create_board(is_empty: bool) -> list:
    '''
    Input: Size, the dimension of the square matrix
    Output: a Size * Size matrix of zeros
    '''
    if(is_empty):
        inner_list = []
        outer_list = []

    else:
        new_inner = []
        new_outer = []

    for itr in range(15):
        if(is_empty):
            inner_list.append(None)
        else:
            new_inner.append(False)
    for outer in range(15):
        if(is_empty):
            outer_list.append(inner_list)
        else:
            new_outer.append(new_inner)
    if(is_empty):
        return outer_list
    else:
        return new_outer

def play_word(word: str, current_board: list, start_coord: tuple, orientation: str) -> int:
    board_copy = [row.copy() for row in current_board]
    
    offset = 0
    word = word.upper()
    row = start_coord[0]
    column = start_coord[1]
    for letter in word:
        if(orientation == "horizontal"):
            board_copy[row][column+offset] = letter
        elif(orientation == "vertical"):
            board_copy[row+offset][column] = letter
        offset += 1
    global game_score 
    game_score = game_score + turn_score(word, board_copy, start_coord, orientation)
    return board_copy

def base_score(current_board: list, start_coord: tuple, orientation: str) -> int:
    score = 0
    row = start_coord[0]
    column = start_coord[1]
    offset = 1
    base_multiplier = 1
    if(orientation == "horizontal"):
        while(current_board[row][column-offset] != None):
            score += get_points(current_board[row][column])
            offset+=1
        offset = 0
        while(current_board[row][column+offset] != None):
            score += get_points(current_board[row][column+offset])
            curr_coord = (row, column+offset)
            if(board.get(curr_coord) == "TW"):
                base_multiplier *= 3
            if(board.get(curr_coord) == "DW"):
                base_multiplier *= 2
            if(board.get(curr_coord) == "ST"):
                base_multiplier *= 2
            if(board.get(curr_coord) == "TL"):
                score += (get_points(current_board[row][column+offset]) * 2)
            if(board.get(curr_coord) == "DL"):
                score += get_points(current_board[row][column+offset])
            offset+=1
    return score * base_multiplier

def turn_score(word: str, current_board: list, start_coord: tuple, orientation: str) -> int:
    '''
    Input: a board
    Output: the score for the most recent turn
    '''
    score = 0
    score += base_score(current_board, start_coord, orientation)
    if len(word) == 7:
        score += 50
    return score



test_board = create_board(True)
new_board = create_board(False)
test_board = play_word("test", test_board, (0,0), "horizontal")
test_board = play_word("ing", test_board, (0,4), "horizontal")
print(game_score)