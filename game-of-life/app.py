import sys

class Board:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.board = [['.' for _ in range(x)] for _ in range(y)]

if __name__ == "__main__":
  print(sys.argv[1])