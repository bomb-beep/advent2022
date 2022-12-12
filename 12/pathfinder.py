import sys

raw_map = open("test_input.txt").read()
grid_map = [[]]

def seeker(x,y,tail = set()):
	tail.add((x,y))
	height = grid_map[x][y]
	print((x,y),tail)
	if height == 83:
		height = 97
	elif height == 69:
		print(tail,len(tail))
		return tail
	for new_x,new_y in adjacent_tiles(x,y):
		if new_x in range(len(grid_map)) and new_y in range(len(grid_map[new_x])):
			new_height = grid_map[new_x][new_y]
			if grid_map[new_x][new_y] == 69:
				new_height = 122

			if not (new_x,new_y) in tail and new_height < height+1:
				seeker(new_x,new_y,tail=tail)

	return None
	
def adjacent_tiles(x,y):
	return {
		(x-1,y),
		(x+1,y),
		(x,y-1),
		(x,y+1)
	}

for line in raw_map.split("\n"):
	for char in line:
		grid_map[-1].append(ord(char))
	grid_map.append([])

while [] in grid_map:
	grid_map.remove([])

for row in grid_map:
	print(row)

for row in range(len(grid_map)):
	for col in range(len(grid_map[row])):
		if grid_map[row][col] == 83:
			seeker(row,col)