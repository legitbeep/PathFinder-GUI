class Tile :

	def __init__(self,r,c,tsize,maze):

		self.neighbours = []
		self.visited = False

		self.val = maze[r][c]
		self.x = r 
		self.y = c

		self.x1 = self.x * tsize
		self.x2 = self.x1 + tsize
		self.y1 = self.y * tsize
		self.y2 = self.y1 + tsize

		self.colors = { "S" : "#4EFF00",
					   "E" : "#FF395D" ,
					   "." : "white",
					   "#" : "#223749"}
		self.visitedColors = { "S" : "#4EFF00",
							   "E" : "#FFA200" ,
							   "." : "#00FF86" ,
							   "#" : "#0099FF"}

		self.color = self.colors[ maze[r][c] ]
		self.visitedColor = self.visitedColors[ maze[r][c] ]

	def visited(self):
		if maze[x][y] != 'S' and maze[x][y] != 'E' : 
			pass
		else :
			self.visited = True
