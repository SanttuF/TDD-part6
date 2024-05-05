from app import Board

def test_Board_exists():
  board = Board()
  assert board is not None