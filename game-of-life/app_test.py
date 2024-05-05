from app import Board

def test_Board_exists():
  board = Board()
  assert board is not None

def test_Board_has_size():
  board = Board(1, 2)
  assert board.x == 1
  assert board.y == 2