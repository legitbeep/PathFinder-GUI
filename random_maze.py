import random

SIZE = 10
ON = '.'
OFF = '#'
START = 'S'
END = 'E'
class RandomMaze:
	def check_neighbours( self, maze , cur ):
		x,y = cur

		coords = [  (x-2,y),
					(x+2,y),
					(x,y-2),
					(x,y+2)  ]

		valid = []
		for coord in coords :
			i , j = coord
			if i < 0 or j < 0 or i >= SIZE or j >= SIZE or maze[i][j] == ON :
				pass
			else :
				valid.append(coord)

		return valid


	def randomMaze(self):
	
		maze = [ [OFF for _ in range(SIZE)] for _ in range(SIZE) ]
		x,y = random.randint(0,SIZE-1),random.randint(0,SIZE-1)
		startx = x 
		starty = y
		maze[x][y] = START
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
				maze[i][j] = ON
				if i == x :
					if j == y+2 :
						maze[x][y+1] = ON
					else :
						maze[x][y-1] = ON
				elif j == y :
					if i == x+2:
						maze[x+1][y] = ON
					else :
						maze[x-1][y] = ON
				stack.append(valid[choose])
		maze[startx][starty] = START
		maze[endx][endy] = END
		print(maxDist)
		return maze
