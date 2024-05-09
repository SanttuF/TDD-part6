import sys

class Board:
  def __init__(self, x=0, y=0, pattern = ''):
    self.x = x
    self.y = y
    self.board = self.setPattern(pattern)

  def setPattern(self, pattern):
    split = pattern.split('$')
    for i in range(len(split)):
      current = split[i]
      if len(current) < self.x:
        split[i] += 'b' * (self.x - len(current))

    while(len(split) < self.y):
      split.append('b'*self.x)

    return split

  def removeExtra(self):
    while(self.board[0] == 'b'*len(self.board[0])):
      self.board.pop(0)
      self.x -= len(self.board[0])

    while(self.board[-1] == 'b'*len(self.board[-1])):
      self.board.pop(-1)
      self.x -= len(self.board[0])

    while(set([self.board[i][0] for i in range(len(self.board))]) == {'b'}):
      for i in range(len(self.board)):
        self.board[i] = self.board[i][1:]
        self.y -= len(self.board)

    while(set([self.board[i][-1] for i in range(len(self.board))]) == {'b'}):
      for i in range(len(self.board)):
        self.board[i] = self.board[i][:-1]
        self.y -= len(self.board)
  
  def __str__(self):
    return '$'.join(self.board)
  
  def simulate(self, n):
    for _ in range(n):
      r = Board.generate(self.board)
      self.board = r
      self.x = len(self.board[0])
      self.y = len(self.board)
      self.removeExtra()
  
  @staticmethod
  def generate(board):
    newBoard = ['b'*(len(board[0]) + 2) for _ in range(len(board) + 2)]
    helpBoard = board[:]
    helpBoard.insert(0, 'b'*len(helpBoard[0]))
    helpBoard.append('b'*len(helpBoard[0]))
    helpBoard.insert(0, 'b'*len(helpBoard[0]))
    helpBoard.append('b'*len(helpBoard[0]))

    for i in range(len(helpBoard)):
      helpBoard[i] = 'bb' + helpBoard[i] + 'bb'

    for y, row  in enumerate(newBoard):
      for x, cell in enumerate(row):
        neighbors = 0

        for j in range(-1, 2):
          for i in range(-1, 2):
            if(helpBoard[y+1+j][x+1+i] == 'o'):
              if not (j == 0 and i == 0):
                neighbors += 1
      
        if helpBoard[y+1][x+1] == 'b':
          if(neighbors == 3):
            newBoard[y] = newBoard[y][:x] + 'o' + newBoard[y][x+1:]
        else:
          if(neighbors < 2 or neighbors > 3):
            newBoard[y] = newBoard[y][:x] + 'b' + newBoard[y][x+1:]
          else:
            newBoard[y] = newBoard[y][:x] + 'o' + newBoard[y][x+1:]

    return newBoard



class RLEFileHandler:
  
  @staticmethod
  def decode(code):
    output = ''
    num = 1
    for i in code:
      if (i == '$'):
        output += '$'
      elif(i.isnumeric()):
        num = int(i)
      else:
        output += i * num
        num = 1
    return output

  @staticmethod
  def encode(code):
    output = ''
    count = 1
    prev = ''

    for i in code:
      if(i == prev):
        count += 1
        continue

      if count == 1: output += prev  
      else:          output += str(count) + prev

      prev = i
      count = 1

      if(i == '$'):
        output += '$'
        prev = ''

    if count == 1: output += prev  
    else:          output += str(count) + prev

    return output

  @staticmethod
  def rleReader(file):
    x, y = 0,0
    pattern = ''
    f = False
    with open(file, 'r') as rleFile:
      for line in rleFile:
        if (line[0] == '#'):
          continue

        if(not f):
          xi = line.find('x') + 4
          yi = line.find('y') + 4
          x = int(line[xi])
          y = int(line[yi])
          f = True
          continue

        pattern = line[:-1]
    return (x, y, pattern)


def run(file, n):
  (x, y, pattern) = RLEFileHandler.rleReader(file)
  decoded = RLEFileHandler.decode(pattern)
  board = Board(x, y, decoded)
  board.simulate(n)
  encoded = RLEFileHandler.encode(str(board))
  return encoded

if __name__ == "__main__":
  file, n = sys.argv[1], int(sys.argv[2])
  print(run(file, n))

    # board = Board(3, 3, 'boo$oob$bob')
    # board.simulate(8)
