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
  
  def __str__(self):
    return '$'.join(self.board)


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


def simulate(file):
  (x, y, pattern) = RLEFileHandler.rleReader(file)
  decoded = RLEFileHandler.decode(pattern)
  board = Board(x, y, decoded)
  encoded = RLEFileHandler.encode(str(board))
  return encoded

if __name__ == "__main__":
  file = sys.argv[1]
  print(simulate(file))