from app import Board, RLEFileHandler

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
  
  def test_Board_pattern_parse(self):
    board = Board()
    pattern = board.setPattern('oo')
    assert pattern == ['oo']

  def test_Board_pattern_parse_newLine(self):
    board = Board()
    pattern = board.setPattern('o$o')
    assert pattern == ['o', 'o']

  def test_Board_pattern_parse_pads_dead_cells_x(self):
    board = Board(3, 1)
    pattern = board.setPattern('oo')
    assert pattern == ['oob']

  def test_Board_pattern_parse_pads_dead_cells_y(self):
    board = Board(1, 3)
    pattern = board.setPattern('o$o')
    assert pattern == ['o','o','b']

  def test_Board_to_string(self):
    board = Board(2, 2, 'oo$oo')
    string = str(board)
    assert string == 'oo$oo'

  def test_remove_extra_lines_x(self):
    board = Board(3, 3, 'ooo$bbo$bbb')
    board.removeExtra()
    assert str(board) == 'ooo$bbo'

    
  def test_remove_extra_lines_y(self):
    board = Board(3, 3, 'boo$bbo$bob')
    board.removeExtra()
    assert str(board) == 'oo$bo$ob'

  def test_remove_extra_lines_y(self):
    board = Board(3, 3, 'oob$bbb$bob')
    board.removeExtra()
    assert str(board) == 'oo$bb$bo'

  def test_generator(self):
    board = Board(3, 3, 'bbb$bob$bbb')
    generated = Board.generate(board.board)
    assert generated == ['bbbbb', 'bbbbb', 'bbbbb', 'bbbbb', 'bbbbb']

  def test_generator_more_complex(self):
    board = Board(3, 3, 'bbb$boo$boo')
    generated = Board.generate(board.board)
    assert generated == ['bbbbb', 'bbbbb', 'bboob', 'bboob', 'bbbbb']

  def test_generator_moving_shape(self):
    board = Board(3, 3, 'boo$oob$bob')
    generated = Board.generate(board.board)
    assert generated == ['bbbbb', 'booob', 'bobbb', 'boobb', 'bbbbb']

  def test_generator_moving_shape(self):
    board = Board(3, 3, 'ooo$obb$oob')
    generated = Board.generate(board.board)
    assert generated == ['bbobb', 'boobb', 'obbob', 'boobb', 'bbbbb']
  
  def test_generator_bigger_size(self):
    board = Board(4, 4, 'bbbb$oobb$oobb$bbbb')
    generated = Board.generate(board.board)
    assert generated == ['bbbbbb', 'bbbbbb', 'boobbb', 'boobbb', 'bbbbbb', 'bbbbbb']
    


class TestDecoding:
  def test_Decoding(self):
    encoded = '2o2b'
    decoded = RLEFileHandler.decode(encoded)
    assert decoded == 'oobb'

  def test_Decoding_Linechange(self):
    encoded = '2o$2b'
    decoded = RLEFileHandler.decode(encoded)
    assert decoded == 'oo$bb'


class TestEndoding:
  def test_Simple_Encode(self):
    string = 'oo'
    encoded = RLEFileHandler.encode(string)
    assert encoded == '2o'
  
  def test_Singular_Encode(self):
    string = 'o'
    encoded = RLEFileHandler.encode(string)
    assert encoded == 'o'

  def test_multiple_letters_Encode(self):
    string = 'ooooboo'
    encoded = RLEFileHandler.encode(string)
    assert encoded == '4ob2o'

  def test_linechange_Encode(self):
    string = 'oo$bb'
    encoded = RLEFileHandler.encode(string)
    assert encoded == '2o$2b'


class TestRLEReader:
  def test_returns_x_and_Y(self):
    x, y, _ = RLEFileHandler.rleReader("testpattern.rle")
    assert x == 3
    assert y == 3

  def test_returns_pattern(self):
    _, _, pattern = RLEFileHandler.rleReader("testpattern.rle")
    assert pattern == 'b2o$2ob$bo'