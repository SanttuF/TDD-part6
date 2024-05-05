from app import Board, decode, encode

class TestBoard:
  def test_Board_exists(self):
    board = Board()
    assert board is not None

  def test_Board_has_size(self):
    board = Board(1, 2)
    assert board.x == 1
    assert board.y == 2

  def test_Board_has_board(self):
    board = Board(4, 5)
    assert board.board is not None
    assert len(board.board) == 5
    assert len(board.board[0]) == 4

class TestDecoding:
  def testDecoding(self):
    encoded = '2o2b'
    decoded = decode(encoded)
    assert decoded == 'oobb'

  def testDecodingLinechange(self):
    encoded = '2o$2b'
    decoded = decode(encoded)
    assert decoded == 'oo\nbb'

class testEndoding:
  def testSimpleEncode(self):
    string = 'oo'
    encoded = encode(string)
    assert encoded == '2o'