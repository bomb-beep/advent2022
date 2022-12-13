import sys

raw_map = open("input.txt").read()
grid_map = [[]]
signposts = []
paths = []

def seeker(x,y,tail = {}):
	global paths
	tail[(x,y)] = ""
	height = grid_map[x][y]
	#print((x,y),height,tail)
	calls = 0
	if signposts[x][y] and len(signposts[x][y]) <= len(tail):
		return
	else:
		signposts[x][y] = tail.copy()

	if height == 83:
		height = 97
	elif height == 69:
		#print(tail,len(tail))
		#draw_path(tail)
		paths.append(tail)
		return
	for (new_x,new_y),dir in adjacent_tiles(x,y).items():
		if new_x in range(len(grid_map)) and new_y in range(len(grid_map[new_x])):
			new_height = grid_map[new_x][new_y]
			if grid_map[new_x][new_y] == 69:
				new_height = 122

			if not (new_x,new_y) in tail and new_height <= height+1:
				tail[(x,y)] = dir
				calls += 1
				seeker(new_x,new_y,tail=tail.copy())
#	print(calls)#,x,y)
	#return None

def draw_path(path):
	for key,value in path.items():
		grid_map[key[0]][key[1]] = value
	
def adjacent_tiles(x,y):
	return {
		(x,y-1):"<",
		(x,y+1):">",
		(x-1,y):"^",
		(x+1,y):"v",
	}

for line in raw_map.split("\n"):
	for char in line:
		grid_map[-1].append(ord(char))
	grid_map.append([])

while [] in grid_map:
	grid_map.remove([])

print(len(grid_map),len(grid_map[0]))
for row in range(len(grid_map)):
	#print(grid_map[row])
	signposts.append([])
	for col in range(len(grid_map[row])):
		signposts[row].append([])

for row in range(len(grid_map)):
	for col in range(len(grid_map[row])):
		if grid_map[row][col] == 83:
			seeker(row,col)
			
paths = sorted(paths,key=lambda x: len(x))
# for path in paths:
# 	print(len(path)-1)
# print(len(paths))
# for path in paths:
# 	print(len(path),path)
# 	draw_path(path)
draw_path(paths[0])
# for row in grid_map:
# 	line = ""
# 	for col in row:
# 		if type(col) == int:
# 			line += (chr(col))
# 		else:
# 			line += col
# 	print(line)

print(len(paths[0])-1)