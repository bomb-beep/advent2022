import numpy as np

x_offset = 500
xmin,xmax = x_offset,x_offset
ymax = 0
grid = np.array([[3]])
print(grid.shape)
output = open("output","w")

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
	#xmin,xmax,ymax = int(xmin),int(xmax),int(ymax)
	output.write("expand {} {} {} {}\n".format(grid.shape,x_offset,xmin,xmax))

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
	output.write("expanded {} {} {} {}\n".format(grid.shape,x_offset,xmin,xmax))

	

def drop_sand():
	global grid,xmin,xmax
	grid[grid==4] = 0
	sand = np.where(grid == 3)
	pot_pos = [[0,1],[-1,1],[1,1]]
	settled = False
	#print(type(sand[0]))
	while not settled:
		settled = True
		if not grid[sand]:
			grid[sand] = 4
		try:
			for element in pot_pos:
				#print(sand,element)
				new_pos = (int(sand[0]+element[0]),int(sand[1]+element[1]))
				print(sand,new_pos, grid[new_pos])
				output.write(f"{new_pos[0]+x_offset},{new_pos[1]}, {x_offset}, {xmax}\n")
				if new_pos[0] + x_offset in range(x_offset,xmax+1):
					#print(new_pos)
					if grid[new_pos] in [0,4]:
						sand = new_pos
						settled = False
						break
					#return False
					#print(new_pos,type(new_pos),type(new_pos[0]))
				else:
					old_offset = x_offset
					expand_grid(min(x_offset,new_pos[0]+x_offset),max(xmax,new_pos[0]+x_offset+1),ymax)
					#xmin,xmax = min(xmin,new_pos[0]+x_offset),max(xmax,new_pos[0]+x_offset+1)
					sand = (sand[0] + old_offset - x_offset,sand[1])
					new_pos = (int(sand[0]+element[0]),int(sand[1]+element[1]))
					if grid[new_pos] in [0,4]:
						sand = new_pos
						settled = False
						break
					#print("expanded",new_pos[0]+x_offset,xmin,xmax)
		except IndexError:
			print("Index Error",grid.shape,sand,new_pos)
			output.write(f"Index Error{grid.shape}, {sand}, {new_pos}\n")
			#print(np.where(grid == 1))

			print_grid()
		#print(sand)
		if settled:
			output.write(f"settled {sand[0]+x_offset},{sand[1]}\n")
			if grid[sand] not in [1,2,3]:
				grid[sand] = 2
			else:
				return False
			return sand
		elif sand[1] > ymax:
			return False
		# if sand[1] == 1:
		# 	print(sand[0] + x_offset,sand[1])
		
			
		

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


rocks = open("test_input.txt").read().split("\n")
#rocks = ["498,4 -> 498,6 -> 496,6"]

walls = []

for line in rocks:
	#print(np.where(grid==3))
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

xmax += 1
ymax += 2
print(xmin,xmax,ymax)
expand_grid(xmin,xmax,ymax)
print(np.where(grid == 1))
for wall in walls:
	draw_wall(wall)
#print(x_offset + np.where(grid==3)[0],np.where(grid==3)[1])

print(x_offset,grid.shape)
#print(grid)
while drop_sand():
	print_grid()
print(x_offset,grid.shape)

print_grid()
print(len(grid[grid == 2]))
output.close()