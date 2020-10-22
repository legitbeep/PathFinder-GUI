import random

class RandomMaze:

	def __init__(self,SIZE):
		self.SIZE = SIZE
		self.ON = '.'
		self.OFF = '#'
		self.START = 'S'
		self.END = 'E'
		self.start = None
		self.end = None

	def check_neighbours( self, maze , cur ):
		x,y = cur

		coords = [  (x-2,y),
					(x+2,y),
					(x,y-2),
					(x,y+2)  ]

		valid = []
		for coord in coords :
			i , j = coord
			if i < 0 or j < 0 or i >= self.SIZE or j >= self.SIZE or maze[i][j] == self.ON :
				pass
			else :
				valid.append(coord)

		return valid


	def randomMaze(self):
	
		maze = [ [self.OFF for _ in range(self.SIZE)] for _ in range(self.SIZE) ]
		x,y = random.randint(0,self.SIZE-1),random.randint(0,self.SIZE-1)
		startx = x 
		starty = y
		maze[x][y] = self.START
		stack = [ (x,y) ]
		
		maxDist,endx,endy = 0,0,0

		while len(stack) > 0 :
			cur = stack.pop()
			x,y = cur
			valid = self.check_neighbours(maze,cur)
			if len(valid) > 0 :
				stack.append(cur)
				choose = random.randint( 0 , len(valid)-1 )
				i,j = valid[choose]
				curDist = (i-startx)**2 + (j-starty)**2 
				if curDist > maxDist:
					maxDist = curDist
					endx = i
					endy = j
				maze[i][j] = self.ON
				if i == x :
					if j == y+2 :
						maze[x][y+1] = self.ON
					else :
						maze[x][y-1] = self.ON
				elif j == y :
					if i == x+2:
						maze[x+1][y] = self.ON
					else :
						maze[x-1][y] = self.ON
				stack.append(valid[choose])
		maze[startx][starty] = self.START
		maze[endx][endy] = self.END
		self.start = (startx,starty)
		self.end = (endx,endy)
		return maze
