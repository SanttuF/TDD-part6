from app import Board

def test_Board_exists():
  board = Board()
  assert board is not None

def test_Board_has_size():
  board = Board(1, 2)
  assert board.x == 1
  assert board.y == 2

def test_Board_has_board():
  board = Board(4, 5)
  assert board.board is not None
  assert len(board.board) == 5
  assert len(board.board[0]) == 4