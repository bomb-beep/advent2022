import numpy as np

x_offset = 500
xmin,xmax = x_offset,x_offset
ymax = 0
grid = np.array([[3]])
print(grid.shape)
output = open("output.txt","w")

def draw_wall(wall):
	global grid
	prevx = None
	prevy = None
	for x,y in wall:
		if prevx:
			start,end = (min(prevx,x)-x_offset,min(prevy,y)),(max(prevx,x)-x_offset+1,max(prevy,y)+1)
			for i in range(start[0],end[0]):
				for j in range(start[1],end[1]):
					grid[i,j] = 1
		prevx = x
		prevy = y

	

def expand_grid(xmin,xmax,ymax):
	global grid,x_offset

	if xmin < x_offset:
		insert = np.zeros((x_offset - xmin,grid.shape[1]))
		grid = np.append(insert,grid,axis = 0)
		x_offset = xmin
	if xmax > x_offset + grid.shape[0]:
		insert = np.zeros((xmax - (grid.shape[0] + x_offset),grid.shape[1]))
		grid = np.append(grid,insert,axis = 0)
	if ymax > grid.shape[1] +1:
		insert = np.zeros((grid.shape[0], ymax - grid.shape[1] +1))
		grid = np.append(grid,insert,axis = 1)

	grid[:,-1] = 1

	

def drop_sand():
	global grid,xmin,xmax
	grid[grid==4] = 0
	sand = np.where(grid == 3)
	pot_pos = [[0,1],[-1,1],[1,1]]
	settled = False
	while not settled:
		settled = True
		if not grid[sand]:
			grid[sand] = 4
		try:
			for element in pot_pos:
				new_pos = (int(sand[0]+element[0]),int(sand[1]+element[1]))
				if new_pos[0] + x_offset in range(x_offset,xmax):
					if grid[new_pos] in [0,4]:
						sand = new_pos
						settled = False
						break
				else:
					old_offset = x_offset
					expand_grid(min(x_offset,new_pos[0]+x_offset),max(xmax,new_pos[0]+x_offset+1),ymax)
					sand = (sand[0] + old_offset - x_offset,sand[1])
					new_pos = (int(sand[0]+element[0]),int(sand[1]+element[1]))
					if grid[new_pos] in [0,4]:
						sand = new_pos
						settled = False
						break
		except IndexError:
			print("Index Error",grid.shape,sand,new_pos)
			output.write(f"Index Error{grid.shape}, {sand}, {new_pos[0] + x_offset}, {xmax}\n")

			print_grid()
		if settled:
			if grid[sand] not in [1,2,3]:
				grid[sand] = 2
			else:
				return False
			return sand
		elif sand[1] > ymax:
			return False

			
		

def print_grid():
	output.write("\n")
	for y in range(grid.shape[1]):
		line = ""
		for x in range(grid.shape[0]):
			if grid[x,y] == 1:
				line += "#"
			elif grid[x,y] == 2:
				line += "O"
			elif grid[x,y] == 3:
				line += "+"
			elif grid[x,y] == 4:
				line += "~"
			else:
				line += "."
		output.write(line+"\n")
		print(line)


rocks = open("input.txt").read().split("\n")

walls = []

for line in rocks:
	wall = []
	for coord in line.split(" -> "):
		x,y = coord.split(",")
		wall.append((int(x),int(y)))
		xmin = min(wall[-1][0],xmin)
		xmax = max(wall[-1][0],xmax)
		ymax = max(wall[-1][1],ymax)
	walls.append(wall)


xmax += 1
ymax += 2
expand_grid(xmin,xmax,ymax)
for wall in walls:
	draw_wall(wall)

counter = 0
while drop_sand():
	counter += 1
	if counter % 100 == 0:
		print(counter)
	

print_grid()
print(len(grid[grid == 2]))
output.close()