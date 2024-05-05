import sys

class Board:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.board = [['.' for _ in range(x)] for _ in range(y)]

def decode(code):
  output = ''
  num = 1
  for i in code:
    if (i == '$'):
      output += '\n'
    elif(i.isnumeric()):
      num = int(i)
    else:
      output += i * num
      num = 1
  return output


if __name__ == "__main__":
  print(sys.argv[1])