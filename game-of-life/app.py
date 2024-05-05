import sys

class Board:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.board = ['b'*x for _ in range(y)]

  def setPattern(self, pattern):
    split = pattern.split('$')
    return split

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
      output += '\n'
      prev = ''

  if count == 1: output += prev  
  else:          output += str(count) + prev

  return output

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


if __name__ == "__main__":
  print(sys.argv[1])