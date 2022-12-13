raw_map = open("input.txt").read()
grid_map = [[]]
signposts = []
seeker_count = 0
shortest_path = 0

def seeker(x,y,steps):
	global signposts,seeker_count,shortest_path
	#steps += 1
	signposts[x][y] = steps
	height = grid_map[x][y]
	if height == 83:
		height = 97
	if grid_map[x][y] == 69:
		print(steps)
		if not shortest_path or steps < shortest_path:
			shortest_path = steps
		return
	
	for (newx,newy),dir in adjacent_tiles(x,y).items():
		if newx in range(len(grid_map)) and newy in range(len(grid_map[newx])):
			newheight = grid_map[newx][newy]
			#print(newx,newy,newheight,height)
			if newheight == 69:
				newheight = 122
			if (signposts[newx][newy] == -1 or signposts[newx][newy] > steps) and newheight <= height +1:
				seeker(newx,newy,steps+1)

	seeker_count += 1
	if seeker_count % 1000000 == 0:
		print("shortest path",shortest_path,"tiles searched",seeker_count)

def adjacent_tiles(x,y):
	return {
		(x,y-1):"<",
		(x,y+1):">",
		(x-1,y):"^",
		(x+1,y):"v",
	}

# class Seeker:
#     def __init__(self,start):
#         self.x = start[0]
#         self.y = start[1]

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
		signposts[row].append(-1)

#print(signposts)
for row in range(len(grid_map)):
	for col in range(len(grid_map[row])):
		if grid_map[row][col] == 83:
			#print(row,col)
			seeker(row,col,0)
#print(signposts)

