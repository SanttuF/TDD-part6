from app import Board, decode, encode, rleReader

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
  def test_Decoding(self):
    encoded = '2o2b'
    decoded = decode(encoded)
    assert decoded == 'oobb'

  def test_Decoding_Linechange(self):
    encoded = '2o$2b'
    decoded = decode(encoded)
    assert decoded == 'oo\nbb'

class TestEndoding:   
  def test_Simple_Encode(self):
    string = 'oo'
    encoded = encode(string)
    assert encoded == '2o'
  
  def test_Singular_Encode(self):
    string = 'o'
    encoded = encode(string)
    assert encoded == 'o'

  def test_multiple_letters_Encode(self):
    string = 'ooooboo'
    encoded = encode(string)
    assert encoded == '4ob2o'

  def test_linechange_Encode(self):
    string = 'oo$bb'
    encoded = encode(string)
    assert encoded == '2o\n2b'

class TestRLEReader:
  def test_returns_x_and_Y(self):
    x, y = rleReader("testpattern.rle")
    assert x == 3
    assert y == 3