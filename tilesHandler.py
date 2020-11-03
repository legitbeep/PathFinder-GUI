from tile import Tile

class Display():

	def __init__(self,canvas,SIZE,TSIZE,maze):

		self.size = SIZE
		self.tsize = TSIZE

		self.maze = maze
		self.canvas = canvas
		self.tiles= {}
		self.listTiles = []
		self.start = None
		self.end = None

		self.fillTiles()
		self.fillNeighbours()
		self.displayMaze()

	def fillTiles(self):

		for r in range(self.size):
			for c in range(self.size):
				t = Tile(r,c,self.tsize,self.maze)
				if self.maze[r][c] == 'S':
					self.start = t
				if self.maze[r][c] == 'E':
					self.end = t

				self.tiles[r,c] = t
				self.listTiles.append(t)
	def fillNeighbours(self):

		for coord , tile in self.tiles.items():
			x,y = coord

			# Top left corner :
			if x == 0 and y == 0:
				self.add_neighbours(tile, self.tiles[x+1, y])       # Under
				self.add_neighbours(tile, self.tiles[x, y+1])       # Right
			
			elif x == 0 and y == self.size - 1 :
				self.add_neighbours(tile, self.tiles[x, y-1])       # Left
				self.add_neighbours(tile, self.tiles[x+1, y])       # Under

			elif x == self.size-1 and y == 0:
				self.add_neighbours(tile, self.tiles[x - 1, y])     # Over
				self.add_neighbours(tile, self.tiles[x, y + 1])     # Right

			elif x == self.size-1 and y == self.size-1:
				self.add_neighbours(tile, self.tiles[x - 1, y])     # Over
				self.add_neighbours(tile, self.tiles[x, y - 1])     # Left

			elif x == 0:
				self.add_neighbours(tile, self.tiles[x + 1, y])     # Under
				self.add_neighbours(tile, self.tiles[x, y + 1])     # Right
				self.add_neighbours(tile, self.tiles[x, y - 1])	    # Left

			elif y == self.size-1:
				self.add_neighbours(tile, self.tiles[x + 1, y])     # Under
				self.add_neighbours(tile, self.tiles[x - 1, y])     # Over
				self.add_neighbours(tile, self.tiles[x, y - 1])     # Left

			elif x == self.size-1:
				self.add_neighbours(tile, self.tiles[x - 1, y])     # Over
				self.add_neighbours(tile, self.tiles[x, y - 1])     # Left
				self.add_neighbours(tile, self.tiles[x, y + 1])     # Right

			# Left border
			elif y == 0:
				self.add_neighbours(tile, self.tiles[x - 1, y])     # Over
				self.add_neighbours(tile, self.tiles[x + 1, y])     # Under
				self.add_neighbours(tile, self.tiles[x, y + 1])     # Right
			
			# Elsewhere in the maze.
			else:
				self.add_neighbours(tile, self.tiles[x - 1, y])     # Over
				self.add_neighbours(tile, self.tiles[x + 1, y])     # Under
				self.add_neighbours(tile, self.tiles[x, y + 1])     # Right
				self.add_neighbours(tile, self.tiles[x, y - 1])     # Left
	
	def add_neighbours(self, tile1,tile2):

		if tile2.val != '#':
			if tile2 not in tile1.neighbours:
				tile1.neighbours.append(tile2)
		if tile1.val != '#':
			if tile1 not in tile2.neighbours:
				tile2.neighbours.append(tile1)

	def displayMaze(self):
		

		for r in range(self.size):
			for c in range(self.size):
				t = self.tiles[r,c]
				self.displayTile(t,t.color,"#38B8BB")


	
	def displayTile(self,tile,color,outline):
		self.canvas.create_rectangle(tile.x1, tile.y1, tile.x2, tile.y2, fill = color , outline=outline)
		self.canvas.update()

	def redrawTile(self,tile,color,outline):
		if tile != self.start and tile != self.end :
			self.canvas.create_rectangle(tile.x1, tile.y1, tile.x2,tile.y2,fill=color,outline=outline)
			self.canvas.update()

	def constructPath(self,cameFrom,start,end):
		cur = end
		path = [cur]
		while cur != start :
			cur = cameFrom[cur]
			path.append(cur)
		path.append(start)
	#	path.reverse()
		return path

	def distance(tile1,til2):
		x1,y1 = (tile1.x,tile1.y)
		x2,y2 = (tile2.x,tile.y)
		return abs(x1-x2) + abs(y1-y2)


