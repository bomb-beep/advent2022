import sys

raw_map = open("input.txt").read()
grid_map = [[]]
signposts = []
step = 0
current_tiles = set()

def adjacent_tiles(x,y):
	return {
		(x,y-1),
		(x,y+1),
		(x-1,y),
		(x+1,y),
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
		signposts[row].append(0)

for row in range(len(grid_map)):
	for col in range(len(grid_map[row])):
		if grid_map[row][col] == 83 or grid_map[row][col] == 97:
			
			current_tiles.add((row,col))

while True:
    for x,y in current_tiles:
        if grid_map[x][y] == 69:
            print(step)
            sys.exit()
        signposts[x][y] = 1

    new_tiles = set()
    for x,y in current_tiles:
        height = grid_map[x][y]
        if height == 83:
            height = 97

        for newx,newy in adjacent_tiles(x,y):
            if newx in range(len(grid_map)) and newy in range(len(grid_map[newx])):
                newheight = grid_map[newx][newy]
                #print(newx,newy,newheight,height)
                if newheight == 69:
                    newheight = 122

                if not signposts[newx][newy] and (newx,newy) not in current_tiles and newheight <= height+1:
                    new_tiles.add((newx,newy))
    current_tiles = new_tiles
    step += 1