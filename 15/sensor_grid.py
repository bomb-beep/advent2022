import regex as re
import numpy as np
xmin,xmax,ymin,ymax = None,None,None,None
grid = np.array((0,0))
sensors = set()
beacons = set()

def print_grid():
	line = "   "
	for x in range(xmin,xmax+1):
		if x % 10 == 0:
			line += str(int(x/10))
		else:
			line += " "
	print(line)
	line = "   "
	for x in range(xmin,xmax +1):
		if x%5 == 0:
			line += str(x%10)
		else:
			line += " "
	print(line)

	for y in range(ymax - ymin +1):
		if 0 <= y + ymin < 10:
			line = f" {y+ymin} "
		else:
			line = f"{y+ymin} "
		for x in range(xmax - xmin +1):
			if grid[x][y] == 0:
				line += "."
			elif grid[x,y] == 1:
				line += "#"
			elif grid[x,y] == 2:
				line += "S"
			elif grid[x,y] == 3:
				line += "B"
		print(line)

def expand_grid(tile):
	global grid,xmin,ymin
	if tile[0] < xmin:
		insert = np.zeros((xmin-tile[0],grid.shape[1]))
		grid = np.append(insert,grid,axis=0)
		xmin = tile[0]
	elif tile[0] >= xmin+grid.shape[0]:
		insert = np.zeros((tile[0]-xmax,grid.shape[1]))
		grid = np.append(grid,insert,axis=0)
	if tile[1] < ymin:
		insert = np.zeros((grid.shape[0],ymin-tile[1]))
		grid = np.append(insert,grid,axis=1)
		ymin = tile[1]
	elif tile[1] >= ymin+grid.shape[1]:
		insert = np.zeros((grid.shape[0],tile[1]-ymax))
		grid = np.append(grid,insert,axis=1)
	

def nearest_beacon(sensor):
	global grid
	# x = sensor[0]-xmin
	# y = sensor[1] - ymin
	searched_tiles = {sensor}
	border_tiles = {sensor}

	found = False
	while not found:
		new_tiles = set()
		for tile in border_tiles:
			for adj in adjacent_tiles(tile):
				if adj[0] - xmin in range(len(grid)) and adj[1] -ymin in range(len(grid[0])):
					new_tiles.add(adj)
				else:
					print("expand!",adj)
					#old_xmin,old_ymin = xmin,ymin
					expand_grid(adj)
					#adj = (adj[0] + old_xmin - xmin,adj[1] + old_ymin - ymin)
					print("expanded!",adj)
					new_tiles.add(adj)

		new_tiles = new_tiles.difference(searched_tiles)

		for tile in new_tiles:
			conv_tile = (tile[0] - xmin,tile[1] - ymin)
			if grid[conv_tile] == 0:
				grid[conv_tile] = 1
			elif grid[conv_tile] == 3:
				found = True
		searched_tiles.update(new_tiles)
		border_tiles = new_tiles

def adjacent_tiles(tile):
	ret = set()
	for x in range(tile[0]-1,tile[0]+2):
		ret.add((x,tile[1]))
	for y in range(tile[1]-1, tile[1]+2):
		ret.add((tile[0],y))
	ret.remove(tile)
	return ret

for line in open("test_input.txt").read().strip().split("\n"):
	m = re.search("Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)",line)
	if m:
		print("sensor = {}, beacon = {}".format((m.group("sx"),m.group("sy")),(m.group("bx"),m.group("by"))))
		sx,sy,bx,by = int(m.group("sx")),int(m.group("sy")),int(m.group("bx")),int(m.group("by"))
		if xmin == None or sx < xmin or bx < xmin:
			xmin = min(sx,bx)
		if xmax == None or sx > xmax or bx > xmax:
			xmax = max(sx,bx)
		if ymin == None or sy < ymin or by < ymin:
			ymin = min(sy,by)
		if ymax == None or sy > ymax or by > ymax:
			ymax = max(sy,by)

		sensors.add((sx,sy))
		beacons.add((bx,by))

print((xmin,xmax),(ymin,ymax))

grid = np.zeros((xmax-xmin+1,ymax-ymin+1))

print(len(grid),len(grid[0]))
print("sensors")
for sensor in sensors:
	print(sensor,sensor[0]+xmin,sensor[1]+ymin)
	grid[sensor[0]-xmin][sensor[1]-ymin] = 2
print("beacons")

for beacon in beacons:
	print(beacon,beacon[0]+xmin,beacon[1]+ymin)
	grid[beacon[0]-xmin][beacon[1]-ymin] = 3



for sensor in sensors:
	nearest_beacon(sensor)
# nearest_beacon((20,14))
# nearest_beacon((12,14))

print((xmin,grid.shape[0]+xmin),(ymin,grid.shape[1]+ymin))
print_grid()
#print(len(grid[grid[:,2000000-ymin] != 0]) - len(grid[grid[:,2000000-ymin] == 3]))
####B######################