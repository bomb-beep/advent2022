import numpy as np

x_offset = 500
grid = np.array([[3]])
print(grid.shape)

def draw_wall(wall):
	for x,y in wall:
		pass

def expand_grid(xmin,xmax,ymax):
	global grid,x_offset
	if xmin < x_offset:
		insert = np.zeros((x_offset - xmin,grid.shape[1]))
		grid = np.append(insert,grid,axis = 0)
		x_offset = xmin
	if xmax > x_offset + grid.shape[0] +1:
		insert = np.zeros((xmax - (grid.shape[0] + x_offset) +1,grid.shape[1]))
		grid = np.append(grid,insert,axis = 0)
	if ymax > grid.shape[1] +1:
		insert = np.zeros((grid.shape[0], ymax - grid.shape[1] +1))
		grid = np.append(grid,insert,axis = 1)

# def draw_wall(wall):
# 	global grid,x_offset
# 	prevx,prevy = None,None
# 	for x,y in wall:
# 		#print(grid.shape)
# 		if x < x_offset:
# 			dif = x_offset - x
# 			x_offset = x
# 			insert = np.zeros((dif,grid.shape[1]))
# 			grid = np.append(insert,grid,axis=0)
# 			#print(insert,grid,grid.shape)
# 		elif x > grid.shape[0] + x_offset:
# 			print("insert right",x_offset,grid.shape[0],x)
# 			dif = x - (grid.shape[0] + x_offset)
# 			insert = np.zeros((dif +1,grid.shape[1]))
# 			grid = np.append(grid,insert,axis=0)
# 		#print(grid.shape)
# 		if y > grid.shape[1]:
# 			print("resize")
# 			print(grid)
# 			print_grid()
# 			grid.resize((grid.shape[0],y+1))
# 			print("__")
# 			print(grid)
# 			print_grid()

# 		if prevx:
# 			xes = sorted((x-x_offset,prevx - x_offset))
# 			ys = sorted((y,prevy))
# 			for row in range(xes[0],xes[1]+1):
# 				for col in range(ys[0],ys[1]+1):
# 					print(row,col)
# 					grid[row,col] = 1
# 			# print(xes[0],xes[1],ys[0],ys[1])
# 			# print(grid[xes[0]:xes[1]+1,ys[0]:ys[1]+1])
# 			# grid[xes[0]:xes[1]+1,ys[0]:ys[1]+1] = 1
# 		prevx,prevy = x,y

def print_grid():
	for y in range(grid.shape[1]):
		line = ""
		for x in range(grid.shape[0]):
			if grid[x,y] == 1:
				line += "#"
			elif grid[x,y] == 2:
				line += "O"
			elif grid[x,y] == 3:
				line += "+"
			else:
				line += "."
		print(line)


rocks = open("test_input.txt").read().split("\n")
#rocks = ["498,4 -> 498,6 -> 496,6"]

xmin,xmax = x_offset,x_offset
ymax = 0

walls = []

for line in rocks:
	print(np.where(grid==3))
	wall = []
	for coord in line.split(" -> "):
		#print(coord)
		x,y = coord.split(",")
		wall.append((int(x),int(y)))
		xmin = min(wall[-1][0],xmin)
		xmax = max(wall[-1][0],xmax)
		ymax = max(wall[-1][1],ymax)
	walls.append(wall)
	#draw_wall(wall)
	#print_grid()

expand_grid(xmin,xmax,ymax)
for wall in walls:
	draw_wall(wall)
print(x_offset + np.where(grid==3)[0],np.where(grid==3)[1])

print(x_offset,grid.shape)
#print(grid)
print_grid()