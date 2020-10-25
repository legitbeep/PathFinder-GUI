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

		self.colors = { "S" : "#F2D015",
					   "E" : "#FF395D" ,
					   "." : "white",
					   "#" : "#223749"}
		self.visitedColors = { "S" : "#F2D015",
							   "E" : "#FFA200" ,
							   "." : "#00FF86" ,
							   "#" : "#0099FF"}
		self.weights = { "S" : 0,
						"E" : 0,
						"." : 1,
						"#" : 100}


		self.weight = self.weights[self.val]
		self.color = self.colors[ maze[r][c] ]
		self.visitedColor = self.visitedColors[ maze[r][c] ]

	def visit(self):
		if self.val != 'S' and self.val != 'E' : 
			pass
		else :
			self.visited = True
	def __str__(self):
		return str(self.x) + " " + str(self.y) 

	def __lt__(self,other):
		return self.weight < other.weight